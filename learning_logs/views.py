from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
    """Homepage of Learning Logs"""
    return render(request, 'learning_logs/index.html')

@login_required #check if user logged in the system (if no -> redirect to loggging in page)
def topics(request):
    """Display list of topics"""
    # topics = Topic.objects.order_by('date_added') ## A query is sent to the database to retrieve Topic objects sorted by atribute
    topics = Topic.objects.filter(owner=request.user).order_by('date_added') # updated var to retrieve from the database only 
                                                            # those Topic objects whose owner attribute matches the current user
    context = {'topics': topics} # dict becomes vars in HTML 
                                 # (where dict key = var name in html to represent values of dict recieved as Topic objects)
    return render(request, 'learning_logs/topics.html', context)

@login_required #check if user logged in the system (if no -> redirect to loggging in page)
def topic(request, topic_id):
    """Display one topic and all it's entries"""
    topic = Topic.objects.get(id=topic_id) # get() - to recieve specified topic by id
    # Checking that the topic belongs to the current user.
    if topic.owner != request.user:
        raise Http404
       
    entries = topic.entry_set.order_by('-date_added') # .entry_set - related manager which load Records related to this topic
                                                      # sort with symbol '-' means reversed sort to display last entries in top    
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required #check if user logged in the system (if no -> redirect to loggging in page)
def new_topic(request):
    """Set a new topic"""
    if request.method != 'POST':
        # Data not sent; create empty topic
        form = TopicForm()
    else:
        # Data sent POST; process data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False) # new topic must be changed before commiting to DB
            new_topic.owner = request.user # current user assigned for atribute owner
            new_topic.save() #save new instance of the topic
            return redirect('learning_logs:topics')
    
    # display empty or invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required #check if user logged in the system (if no -> redirect to loggging in page)
def new_entry(request, topic_id):
    """Adds a new enrty on a specific topic"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.owner:
        raise Http404
    
    if request != 'POST':
        # data not sent; create an empty form
        form = EntryForm()
    else:
        # Data sent POST; process data\
        form = EntryForm(data=request.POST) #create instance populated with POST data from the request object
        if form.is_valid():
            new_entry = form.save(commit=False) # without saving to the database for the time being
            new_entry.topic = topic # assign topic from datebase for atribute topic of ogject new_entry
            new_entry.save() # save entry with correct associated topic
            return redirect('learning_logs:topic', topic_id=topic_id) # view name to which control is passed, 
                                                                      # and an argument for this view
        
    # Display empty or invalid form
    context = {'topic': topic, 'form':form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required #check if user logged in the system (if no -> redirect to loggging in page)
def edit_entry(request, entry_id):
    """Edit an existing entry"""
    entry = Entry.objects.get(id=entry_id) #get entry object which we want to change
    topic = entry.topic #asociated with topic

    if request != 'POST':
        # Initial query; the form is populated with data from the current record.
        form = EntryForm(instance=entry) #create form with data of existing record of entry
    else:
        # Data sent POST; process data
        """User see his existing data and can update it"""
        form = EntryForm(instance=entry, data=request.POST) # create an inctanse of existing entry
                                                            # updated with data from 'request.POST'      
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic_id) # why&&&

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)




