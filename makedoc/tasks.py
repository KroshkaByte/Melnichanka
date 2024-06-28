import os
import shutil

from celery import shared_task
from django.conf import settings


@shared_task
def delete_files():
    directory = settings.BASE_DIR / "makedoc" / "tempdoc"

    if not os.path.exists(directory):
        return "Directory does not exist"
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        try:
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
        except Exception:
            return f"Failed to delete {item_path}. Reason {e}"

    return "Successfully deleted all user folders"
