from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

    #главная
    path('', views.main_view, name='main'),

    #меню
    path('main/menu/about.html', views.about_view, name='about'),
    path('main/menu/contact.html', views.contact_view, name='contact'),

    #questions
    path('main/questions/questions.html', views.questions_view, name='questions'),
    path('main/questions/questions/<int:post_id>/', views.question_detail, name='question_detail'),
    path('delete_answer/<int:answer_id>/', views.delete_answer, name='delete_answer'),
    path('answer/<int:post_id>/', views.answer_view, name='answer'),

    #add question
    path('main/questions_add/post.html', views.post_view, name='post'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)