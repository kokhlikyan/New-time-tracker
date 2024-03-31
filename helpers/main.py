import logging
import os
import secrets
import string

from PIL import Image
from PySide6 import QtCore
from PySide6.QtCore import QByteArray
from PySide6.QtGui import QPixmap, QImage
from plyer import notification


def generate_token(length=16):
    alphabet = string.ascii_letters + string.digits
    token = ''.join(secrets.choice(alphabet) for _ in range(length))
    return token


def check_png_file(filename):
    if not os.path.exists(filename):
        logging.error(f"Error: File '{filename}' does not exist.")
        return False

    try:
        with Image.open(filename) as img:
            img.verify()
            return True
    except Exception as e:
        logging.error(f"Error: File '{filename}' is either not a PNG or is corrupted.")
        logging.error(f"Exception: {e}")
        return False


def other_notification(image_path):
    notification.notify(
        title='Notification Title',
        message='This is a notification message.',
        app_name='My App',
        app_icon=image_path,  # You can specify an icon if needed
        timeout=10  # Time in seconds the notification is displayed
    )


def macos_notification(image_path):
    from Foundation import NSDate, NSUserNotification, NSUserNotificationCenter
    notification = NSUserNotification.alloc().init()
    notification.setTitle_("Screenshot")
    notification.setInformativeText_("screenshot taken")

    delivery_date = NSDate.dateWithTimeIntervalSinceNow_(3)
    notification.setDeliveryDate_(delivery_date)

    center = NSUserNotificationCenter.defaultUserNotificationCenter()
    center.deliverNotification_(notification)


def show_notification(image_path):
    if os.name == 'posix':

        macos_notification(image_path)
    else:
        other_notification()
