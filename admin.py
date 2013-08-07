from django.contrib import admin
from forums.models import Board
from forums.models import Topic
from forums.models import Message

admin.site.register(Board)
admin.site.register(Topic)
admin.site.register(Message)