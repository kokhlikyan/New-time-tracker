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


def other_notification():
    notification.notify(
        title='Screenshot',
        message='Screenshot taken.',
        app_name='Loxala',
        timeout=10  # Time in seconds the notification is displayed
    )


def macos_notification():
    from Foundation import NSDate, NSUserNotification, NSUserNotificationCenter
    notification = NSUserNotification.alloc().init()
    notification.setTitle_("Screenshot")
    notification.setInformativeText_("Screenshot taken")

    delivery_date = NSDate.dateWithTimeIntervalSinceNow_(3)
    notification.setDeliveryDate_(delivery_date)

    center = NSUserNotificationCenter.defaultUserNotificationCenter()
    center.deliverNotification_(notification)


def show_notification():
    if os.name == 'posix':

        macos_notification()
    else:
        other_notification()
