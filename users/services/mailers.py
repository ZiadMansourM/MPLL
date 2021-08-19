from django.conf import settings
from django.core.mail import send_mail
# ---------------> ActivationMailer
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode



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
    def __init__(self, domain: str, user):
        super().__init__(
            subject='MPLL: Activate your blog account.',
            recipient_list=[user.email],  
            message = render_to_string('users/acc_active_email.html', {
                'user': user,
                'domain': domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            }),
        )