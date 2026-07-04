from django.urls import path
from .import views

app_name='polls'

urlpatterns=[
    path('',views.home,name='home'),
    path('create/',views.create_poll,name='create_poll'),
    path('<int:pk>/',views.poll_detail,name='poll_detail'),
    path('<int:pk>/vote/',views.vote,name='vote'),
    path('<int:pk>/results/',views.results,name='results'),
]