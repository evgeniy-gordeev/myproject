from django import forms
from .models import Post, Answer

class PostForm(forms.ModelForm):
    image = forms.ImageField()
    class Meta:
        model = Post
        fields = ('title', 'content', 'image')

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('content',)