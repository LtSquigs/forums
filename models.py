from django.db import models

# Create your models here.
class Board(models.Model):
	name = models.CharField(max_length=200)
	restricted = models.BooleanField(default=false)
	allowed_groups = models.ManyToManyField(models.Group)

class Topic(models.Model):
	board = models.ForeignKey(Board)
	title = models.CharField(max_length=200, default='')
	deleted = models.BooleanField(default=false)


class Message(models.Model):
	topic = models.ForeignKey(Topic)
	author = models.ForeignKey(models.User)
	content = models.TextField(default='')
	deleted = models.BooleanField(default=false)