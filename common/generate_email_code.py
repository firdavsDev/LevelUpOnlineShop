from django.conf import settings
from django.core.mail import send_mail  # for sending email
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode


def send_verification_email(user_id, user_email) -> bool:
    try:
        bytes_user_id = force_bytes(user_id)
        encoded_user_id = urlsafe_base64_encode(bytes_user_id)
        domain = f"http://localhost:8000/activate/{encoded_user_id}/"
        subject = settings.EMAIL_SUBJECT
        message = f"Click the link below to verify your email\n{domain}"

        # body = render_to_string(
        #     "accounts/verification.html",
        #     {
        #         "subject": subject,
        #         "body": message,
        #         "domain": domain,
        #     },
        # )

        # html_body = strip_tags(body)

        # send email
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user_email],
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(e)
        return False
