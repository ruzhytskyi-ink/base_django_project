"""Defines the URL-schemas for learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    # '' — marshrutize to the URL (http://localhost:8000/)
    # views.index — call app/views func index()
    # name='index' — route name for use in the code

    # List of topics page
    path('topics/', views.topics, name='topics'),

    # Page with detailed info on a specific topic
    path('topics/<int:topic_id>/', views.topic, name='topic'), #id saves in argument: topic_id
    # <int:topic_id> - as pattern Django like instruction to parce URL

    # Adding new topic page
    path('new_topic', views.new_topic, name='new_topic'),

    # Adding new entry page
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # Adding editing entry page
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    ]