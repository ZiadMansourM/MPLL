from django.conf import settings
from django.core.mail import send_mail


class BaseMailer:
    def __init__(self, subject, message, recipient_list, html_message=None):
        self.subject = subject
        self.message = message
        self.recipient_list = recipient_list
        self.html_message = html_message

    def send_email(self):
        send_mail(
            subject=self.subject,
            message=self.message,
            from_email=settings.EMAIL_HOST_USER,
            # '"ODHR" <odhr.egypt@gmail.com>',
            recipient_list=self.recipient_list,
            html_message=self.html_message,
            fail_silently=False,
        )


class SearchedMailer(BaseMailer):
    def __init__(self, recipient_list):
        super().__init__(
            subject = 'ODHR: Your EMR Has Been Viewed!',
            recipient_list = [recipient_list],  
            message = """Hey there!\nWe are sending you this email to inform you that your EMR account has been viewed""", 
            html_message = """<p><strong>Hey there!</strong><br>We are sending you this email to inform you that <mark>your EMR account has been viewed</mark></p>"""
        )


class ActivationMailer(BaseMailer):
    def __init__(self, recipient_list):
        super().__init__(
            subject='ODHR: Activate Your Account',
            recipient_list=[recipient_list],  
            message='Hey there!\nWe are sending you this email to let you activate your email', 
            html_message='<p><strong>Hey there!</strong><br>We are sending you this email to let you <mark>activate your email</mark></p>'
        )