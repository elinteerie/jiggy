from django.core.mail import send_mail

def send_welcome_email(email):
    subject = 'Welcome to Jiggy'
    message = f'Hello,\n\nThank you for registering on Jiggy! We are excited to have you with us.'

    send_mail(
        subject,
        message,
        'elinteerie@gmail.com',  # Sender's email address
        [email],  # Recipient's email address
        fail_silently=False,
    )


def send_otp_email(email, token):
    subject = 'Verify Token'
    message = f' Hello, Please Verify your Account with this Token {token.code}. This Token last for 10 Minutes'

    send_mail(subject, message,'elinteerie@gmail.com', [email], fail_silently=False)

