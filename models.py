from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Create your models here.
class Board(models.Model):
	name = models.CharField(max_length=200)
	restricted = models.BooleanField(default=False)
	allowed_groups = models.ManyToManyField(Group)

class Topic(models.Model):
	board = models.ForeignKey(Board)
	title = models.CharField(max_length=200, default='')
	deleted = models.BooleanField(default=False)


class Message(models.Model):
	topic = models.ForeignKey(Topic)
	author = models.ForeignKey(User)
	content = models.TextField(default='')
	deleted = models.BooleanField(default=False)