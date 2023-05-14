import sqlite3
from PIL import Image
from django.shortcuts import render, redirect
from .forms import PostForm

def post_view(request): #отправка запроса
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            text = form.cleaned_data['text']
            image = form.cleaned_data['image']
            
            # Сохраните текст и изображение в базу данных
            conn = sqlite3.connect('db.sqlite3')  # Подключаемся к базе данных
            cursor = conn.cursor()
            cursor.execute("INSERT INTO posts (text, image) VALUES (?, ?)", (text, image.read()))
            conn.commit()  # Сохраняем изменения в базе данных
            conn.close()  # Закрываем соединение с базой данных
            
            # Перенаправьте пользователя на другую страницу
            return redirect('post_success')
    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})


def post_success_view(request): #отправка запроса после валидации
    return render(request, 'post_success.html')