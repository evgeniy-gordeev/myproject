from django import forms

class PostForm(forms.Form):
    text = forms.CharField(label='Введите текст', widget=forms.Textarea)