import sqlite3
from PIL import Image
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import PostForm, AnswerForm
from .models import Post

#главная страница
def main_view(request):
    sort_by = request.GET.get('sort_by', '-created_at')  # По умолчанию сортируем по дате создания (новые вопросы сверху)
    search_query = request.GET.get('search', '')  # Получаем поисковый запрос из параметра 'search' или пустую строку, если параметр не указан
    questions = Post.objects.filter(title__icontains=search_query).order_by(sort_by)
    context = {'questions': questions, 'sort_by': sort_by, 'search_query': search_query}
    paginator = Paginator(questions, 5)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    context['page'] = page
    return render(request, 'main.html', context)

#меню
def about_view(request):
    return render(request, 'main/menu/about.html')

def contact_view(request):
    return render(request, 'main/menu/contact.html')

#вопросы
def questions_view(request):
    return render(request, 'questions.html')

def question_detail(request, post_id):
    question = get_object_or_404(Post, pk=post_id)
    return render(request, 'main/questions/question_detail.html', {'question': question})

def answer_view(request, post_id):
    post = Post.objects.get(pk=post_id)

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.post = post
            answer.save()
            return redirect(reverse('question_detail', kwargs={'post_id': post_id}))
    else:
        form = AnswerForm()

    return render(request, 'main/questions/answer.html', {'form': form, 'post': post})


#добавить вопрос
from django.contrib import messages

def post_view(request):
    search_query = request.GET.get('search', '')
    posts = Post.objects.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            if 'image' in request.FILES:
                post.image = request.FILES['image']
            post.save()
            return redirect('main')
        else:
            print(form.errors)  # Вывод ошибок формы в консоль
            messages.error(request, 'Ошибка при создании поста.')  # Отображение сообщения об ошибке пользователю
    else:
        form = PostForm()

    return render(request, 'main/questions_add/post.html', {'form': form, 'posts': posts})