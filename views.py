from django.http import HttpResponse
from django.template import RequestContext, loader

from forums.models import ForumTopic

def index(request):

    latest_topics_list = ForumTopic.objects.order_by('-date_updated')[:20]
    template = loader.get_template('forums/index.html')

    context = RequestContext(request, {
        'latest_topics_list' : latest_topics_list
    })
    
    return HttpResponse(template.render(context))