from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'portfolio_app'
urlpatterns = [
    path('home/', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    # ex: /polls/5/results/
    path('work/', views.work, name='work'),
    # ex: /polls/5/vote/
    path('contact', views.contact, name='contact'),
]

