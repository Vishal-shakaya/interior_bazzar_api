from ib_app.settings import EMAIL_HOST_USER

from django.test import TestCase

# Create your tests here.
def TestMailView():
    try:
        send_mail(
            subject='Test Subject',
            message='Hello! This is a test email from Django using Gmail.',
            from_email=EMAIL_HOST_USER,
            recipient_list=['vishalshakaya.feelsafe@gmail.com'],
        )
        print('Email sent successfully!')
    except Exception as e:
        print(f'Email sending failed: {e}')
