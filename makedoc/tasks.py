import os
import shutil

from celery import shared_task
from django.conf import settings


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
