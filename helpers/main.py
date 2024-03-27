import logging
import os
import secrets
import string

from PIL import Image


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
