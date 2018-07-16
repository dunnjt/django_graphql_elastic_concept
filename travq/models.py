from django.db import models

# Create your models here.
class CoreMetrics(models.Model):
    data = models.TextField(blank=True)

class Questions(models.Model):
    question = models.TextField(default="")
    answers = models.TextField()

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    point = models.IntegerField()
    questions = models.ForeignKey(Questions, related_name='user', on_delete=models.CASCADE)

class Answers(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    score = models.IntegerField()
    isApproved = models.BooleanField()

class Tags(models.Model):
    tag = models.TextField(default="")
