from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, AnswerForm
from django.http import HttpResponse
from .models import Post, Answer

def index(request):
    return HttpResponse("Привет, мир!")


def post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post(text=form.cleaned_data['text'], image=form.cleaned_data['image'])
            post.save()
            return redirect('post_success')
    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})


def answer_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST, request.FILES)
        if form.is_valid():
            answer = Answer(text=form.cleaned_data['text'], image=form.cleaned_data['image'], post=post)
            answer.save()
            return redirect('answer_success')
    else:
        form = AnswerForm()
    return render(request, 'answer.html', {'form': form, 'post': post})


def post_success_view(request):
    return render(request, 'post_success.html')


def answer_success_view(request):
    return render(request, 'answer_success.html')
