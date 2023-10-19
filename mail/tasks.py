from celery import shared_task
from django.core.mail import send_mail
from register_mail import settings

@shared_task
def send_registration_email(user_email):
    subject = 'Registration Confirmation'
    message = 'Thank you for registering!'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)