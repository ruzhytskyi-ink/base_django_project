"""Define URL schemes for users"""

from django.urls import path, include
from . import views

app_name = 'users' # Django infrastructure can distinguish these URLs from URLs of other apps
urlpatterns = [
    # Include URL autorization by default
    path('', include('django.contrib.auth.urls')),

    # Registration page
    path('register/', views.register, name='register'),
]