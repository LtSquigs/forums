from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=200)
    restricted = models.BooleanField(default=False)
    allowed_groups = models.ManyToManyField(Group)
    # views?
    # posts?

class Topic(models.Model):
    board = models.ForeignKey(Board)
    title = models.CharField(max_length=200, default='')
    deleted = models.BooleanField(default=False)
    anchored = models.BooleanField(default=False)
    anchoredToFeed = models.BooleanField(default=False)
    locked = models.BooleanField(default=False)

    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()

    # views ?
    posts = models.IntegerField(default=0)

    #firstMessage/lastMessage?

class Message(models.Model):
    topic = models.ForeignKey(Topic)
    author = models.ForeignKey(User)
    content = models.TextField(default='')
    deleted = models.BooleanField(default=False)
    
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()