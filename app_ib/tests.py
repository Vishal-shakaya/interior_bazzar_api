from django.test import TestCase

# Create your tests here.
def send_test_email():
    try:
        send_mail(
            subject='Test Subject',
            message='Hello! This is a test email from Django using Gmail.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['recipient@example.com'],
        )
        print('Email sent successfully!')
    except Exception as e:
        print(f'Email sending failed: {e}')
