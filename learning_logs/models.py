from django.db import models

class Topic(models.Model):
    """Topic the user is studying"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True) #set current date and time

    def __str__(self):
        """Return string representation of the model"""
        return self.text
    
class Entry(models.Model):
    """Info user revied on the topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # atribute 'topic' use key instace to conect models
                                                               # argument 'on_delete=...CASCADE' use to delete all entires related to this topic
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:                         #additional info about managing class Entry
        verbose_name_plural = 'entries' #a special attribute that instructs Django to use the plural form 'Entries'

    def __str__(self):
        """Return string representation of the model"""
        return f"{self.text[:50]}..."