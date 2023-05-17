import sqlite3
from PIL import Image
from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import PostForm, AnswerForm
from .models import Post

#главная страница
def main_view(request):
    return render(request, 'main.html')

#отправка поста
def post_view(request):
    search_query = request.GET.get('search', '')
    posts = Post.objects.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('post_success')
    else:
        form = PostForm()

    return render(request, 'post.html', {'form': form, 'posts': posts})

#отправка запроса после валидации
def post_success_view(request): 
    return render(request, 'post_success.html')

# отправка ответа на пост
def answer_view(request, post_id):
    post = Post.objects.get(pk=post_id)

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.post = post
            answer.save()
            return redirect('answer_success')
    else:
        form = AnswerForm()

    return render(request, 'answer.html', {'form': form, 'post': post})

# успешная отправка ответа
def answer_success_view(request):
    return render(request, 'answer_success.html')

#страница о нас
def about_view(request):
    return render(request, 'about.html')

#страница с контактами
def contact_view(request):
    return render(request, 'contact.html')

def search_res_view(request):
    search_query = request.GET.get('search', '')
    posts = Post.objects.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))
    return render(request, 'search_res.html', {'posts': posts, 'search_query': search_query})