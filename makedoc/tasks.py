import os
import shutil

from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMessage


@shared_task
def delete_files():
    """
    Deletes all user folders from the specified directory.

    Checks if the directory exists, and if it does, deletes all subdirectories
    within it. If the directory does not exist, it returns an appropriate message.
    If an error occurs while deleting a subdirectory, it returns the error message.
    """
    directory = settings.BASE_DIR / "makedoc" / "tempdoc"

    if not os.path.exists(directory):
        return "Directory does not exist"
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        try:
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
        except Exception as e:
            return f"Failed to delete {item_path}. Reason {e}"

    return "Successfully deleted all user folders"


@shared_task(bind=True, max_retries=3)
def send_email_with_attachment(self, email, file_path, full_name):
    """
    Task to send an email with an attachment.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist")

    email_message = EmailMessage(
        subject=f"{full_name}",
        body="Documents archive",
        from_email=settings.EMAIL_HOST_USER,
        to=[email],
    )

    try:
        with open(file_path, 'rb') as f:
            email_message.attach(os.path.basename(file_path), f.read(), 'application/zip')

        email_message.send()

    except Exception as e:
        self.retry(exc=e, countdown=60)
