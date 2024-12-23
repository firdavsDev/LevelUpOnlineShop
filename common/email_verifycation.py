from django.conf import settings
from django.core.mail import send_mail  # for sending email
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode


def verify_email_code(email_code: str) -> int:
    try:
        decoded_user_id = urlsafe_base64_decode(email_code).decode("utf-8")
        return int(decoded_user_id)
    except Exception as e:
        print(e)
        raise ValueError("Invalid email code")


def send_verification_email(user_id, user_email) -> bool:
    try:
        bytes_user_id = force_bytes(user_id)
        encoded_user_id = urlsafe_base64_encode(bytes_user_id)
        verificationUrl = (
            f"http://localhost:8000/accounts/verify-email/{encoded_user_id}/"
        )
        subject = settings.EMAIL_SUBJECT

        body = render_to_string(
            "accounts/verification.html",
            {
                "subject": subject,
                "verificationUrl": verificationUrl,
            },
        )

        html_body = strip_tags(body)

        # send email
        send_mail(
            subject,
            html_body,
            settings.EMAIL_HOST_USER,
            [user_email],
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(e)
        return False
