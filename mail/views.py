from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.core.mail import send_mail 
from register_mail import settings
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "You just now registered.")
            subject = 'Registration Confirmation'
            message = 'Thank you for registering!'
            from_email = settings.EMAIL_HOST_USER 
            recipient_list = [user.email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            return redirect('mail/register.html')
    else:
        form = UserRegisterForm()
    return render(request, 'mail/register.html', {'form': form})

