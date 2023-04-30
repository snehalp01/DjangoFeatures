from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name 

class Topic(models.Model):
    subject = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now_add=True)
    # if board has topics associated with it. Board can not be deleted
    board = models.ForeignKey(Board, related_name="topics", on_delete=models.PROTECT) 
    starter = models.ForeignKey(User, related_name="topics", on_delete=models.CASCADE)

class Post(models.Model):
    message = models.TextField()
    topic = models.ForeignKey(Topic, related_name="posts", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name="posts",on_delete=models.CASCADE)
    # '+' sign in related field indicates we dont need reverse relationships 
    updated_by = models.ForeignKey(User, null = True, related_name="+", on_delete=models.CASCADE)