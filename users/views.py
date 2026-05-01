from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # display empty registration form
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Logging in and redirecting to home page
            login(request, new_user)
            return redirect('learning_logs:index')

    # display empty or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context) #path of template without 'users/templates'