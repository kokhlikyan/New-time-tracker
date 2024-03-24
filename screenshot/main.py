import os
import logging
import time
from datetime import datetime
from core.config import APP_LOCAL_FOLDER
from PIL import ImageGrab
from storage.events import set_last_screenshot_path


def capture_screenshot(all_screens=False):
    try:
        folder_name = 'screenshot'
        os.makedirs(os.path.join(APP_LOCAL_FOLDER, folder_name), exist_ok=True)
        screenshot = ImageGrab.grab(all_screens=all_screens)

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"screenshot_{timestamp}.png"
        filepath = os.path.join(APP_LOCAL_FOLDER, folder_name, filename)
        screenshot.save(filepath)
        logging.info('Take screenshot...')


    except Exception as e:
        logging.error(f'Error: {e}')


all_screens = True
while True:
    time.sleep(5)
    capture_screenshot(all_screens)
