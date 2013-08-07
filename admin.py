from django.contrib import admin
from forms.models import Board
from forms.models import Topic
from forms.models import Message

admin.site.register(Board)
admin.site.register(Topic)
admin.site.register(Message)