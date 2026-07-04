from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Poll, Option, Vote
from .forms import PollForm

def home(request):
    polls = Poll.objects.filter(is_public=True).order_by('-created_at')
    return render(request, 'polls/home.html', {'polls': polls})

@login_required
def create_poll(request):
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            poll = form.save(commit=False)
            poll.created_by = request.user
            poll.save()
            options = request.POST.getlist('options')
            for option_text in options:
                if option_text.strip():
                    Option.objects.create(poll=poll, text=option_text)
            return redirect('polls:poll_detail', pk=poll.pk)
    else:
        form = PollForm()
    return render(request, 'polls/create_poll.html', {'form': form})

def poll_detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    user_vote = None
    if request.user.is_authenticated:
        user_vote = Vote.objects.filter(poll=poll, user=request.user).first()
    return render(request, 'polls/poll_detail.html', {'poll': poll, 'user_vote': user_vote})

@login_required
def vote(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    if request.method == 'POST':
        option_id = request.POST.get('option')
        if not option_id:
            messages.error(request, 'Please select an option.')
            return redirect('polls:poll_detail', pk=pk)
        option = get_object_or_404(Option, pk=option_id)
        Vote.objects.get_or_create(poll=poll, user=request.user, defaults={'option': option})
        return redirect('polls:results', pk=pk)

def results(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    options = poll.options.all()
    total_votes = poll.votes.count()
    results_data = []
    for option in options:
        count = option.votes.count()
        percent = (count / total_votes * 100) if total_votes > 0 else 0
        results_data.append({'option': option, 'count': count, 'percent': round(percent, 1)})
    return render(request, 'polls/results.html', {'poll': poll, 'results_data': results_data, 'total_votes': total_votes})