from django.http import HttpResponse
from django.template import RequestContext, loader

from forums.models import Topic
from forums.models import Board

def index(request):

    latest_topics_list = Topic.objects.order_by('-date_updated')[:20]
    board_list = Board.objects.all()

    template = loader.get_template('forums/index.html')

    context = RequestContext(request, {
        'latest_topics_list' : latest_topics_list,
        'board_list' : board_list
    })
    
    return HttpResponse(template.render(context))
