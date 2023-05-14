from django.db import models

class Post(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='post_images', null=True, blank=True)

class Answer(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='answers')
    text = models.TextField()
    image = models.ImageField(upload_to='answer_images', null=True, blank=True)