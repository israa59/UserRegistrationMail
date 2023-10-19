from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.core.mail import send_mail 
from register_mail import settings
from django.contrib import messages

from .tasks import send_registration_email

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "You just now registered.")
            
            send_registration_email.delay(user.email)

            return redirect('register.html')
    else:
        form = UserRegisterForm()
    return render(request, 'mail/register.html', {'form': form})

