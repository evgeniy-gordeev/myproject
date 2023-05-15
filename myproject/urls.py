from django.contrib import admin
from django.urls import path
from .views import main_view, post_view, post_success_view, about_view, contact_view

urlpatterns = [
    path('', main_view, name='main'),
    path('post.html', post_view, name='post'),
    path('post/success/', post_success_view, name='post_success'),
    path('about.html', about_view, name='about'),
    path('contact.html', contact_view, name='contact'),
]