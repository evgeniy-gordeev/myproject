from django.shortcuts import render, redirect
from .forms import PostForm

def post_view(request): #отправка запроса
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            # Сохраните текст в базу данных
            # ...
            # Перенаправьте пользователя на другую страницу
            return redirect('post_success')
    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})

def post_success_view(request): #отправка запроса после валидации
    return render(request, 'post_success.html')