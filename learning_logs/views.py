from django.shortcuts import render
from .models import Topic

def index(request):
    """Homepage of Learning Logs"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Display list of topics"""
    topics = Topic.objects.order_by('date_added') #A query is sent to the database to retrieve Topic objects sorted by atribute
    context = {'topics': topics} # dict becomes vars in HTML 
                                 # (where dict key = var name in html to represent values of dict recieved as Topic objects)
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Display one topic and all it's entries"""
    topic = Topic.objects.get(id=topic_id) # get() - to recieve specified topic by id
    entries = topic.entry_set.order_by('-date_added') # .entry_set - related manager which load Records related to this topic
                                                      # sort with symbol '-' means reversed sort to display last entries in top    
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)