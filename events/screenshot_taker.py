import logging
import os
import random
import threading
import time
import screeninfo
from datetime import datetime
from PIL import ImageGrab
from PySide6.QtCore import QTimer, QObject, Signal, QThread

from core.config import APP_LOCAL_FOLDER
from observer.main import Observer, Subject
from helpers.time import get_random_seconds
from helpers.main import check_png_file


class ScreenshotWorker(QObject):
    screenshot_signal = Signal()

    def __init__(self, subject):
        super().__init__()
        self.active_screen = None
        self.timer = None
        self.subject = subject
        self.screenshot_time = get_random_seconds() * 1000

    def run_taker(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.capture_screenshots)
        self.timer.start(self.screenshot_time)
        logging.info(f'Screenshot will be taken in  {self.screenshot_time / 1000}ms...')

    def stop(self):
        self.timer.stop()

    def capture_screenshots(self):
        logging.info(f'Screenshot will be taken in  {self.screenshot_time / 1000}s...')
        folder_name = 'screenshot'
        os.makedirs(os.path.join(APP_LOCAL_FOLDER, folder_name), exist_ok=True)
        screens = screeninfo.get_monitors()
        monitor = self.subject.monitor()
        if monitor == 'active':
            self.active_screen = True
        else:
            self.active_screen = False
        for i, screen in enumerate(screens):
            if screen.is_primary == self.active_screen:
                screenshot = ImageGrab.grab(bbox=(screen.x, screen.y, screen.width, screen.height))
                self.save_screenshot(screenshot, monitor)
        self.screenshot_time = get_random_seconds() * 1000

    def save_screenshot(self, screenshot, monitor):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"screenshot_{monitor}_{timestamp}.png"
        filepath = os.path.join(APP_LOCAL_FOLDER, 'screenshot', filename)
        screenshot.save(filepath)
        logging.info(f'Took screenshot for {monitor} monitor...')
        if check_png_file(filepath):
            self.set_border_image(filepath)

    def set_border_image(self, border_image_path):
        app = self.subject.get_app()
        app.header.setStyleSheet(self.get_stylesheet(border_image_path))

    @staticmethod
    def get_stylesheet(border_image_path):
        # Construct and return the stylesheet with the provided border image path
        stylesheet = f"#header{{\n" \
                     f"    border-radius: 5px;\n" \
                     f"    border-image: url({border_image_path});\n" \
                     f"}}\n" \
                     f"\n" \
                     f"#frame{{\n" \
                     f"    border-radius: 5px;\n" \
                     f"    background-color: rgba(0, 0, 0, 102);\n" \
                     f"    border-image: none;\n" \
                     f"}}\n" \
                     f"\n" \
                     f"QPushButton{{\n" \
                     f"    border: none;\n" \
                     f"    background-color: none;\n" \
                     f"    border-image: none;\n" \
                     f"}}\n" \
                     f"QLabel{{\n" \
                     f"    border-image: none;\n" \
                     f"}}"
        return stylesheet


class ScreenshotTaker(QThread):

    def __init__(self):
        super(ScreenshotTaker, self).__init__()
        self.subject = None
        self.worker = None
        self.screenshot_time = 10

    def run(self):
        self.worker = ScreenshotWorker(self.subject)
        self.worker.run_taker()
        self.exec_()

    def stop(self):
        if self.worker is not None:
            self.worker.stop()

    def update(self, subject: Subject) -> None:
        self.subject = subject

        if subject.get_status():
            self.start()
        else:
            self.stop()
