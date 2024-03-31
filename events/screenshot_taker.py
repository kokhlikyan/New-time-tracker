import logging
import os
import screeninfo
from datetime import datetime
from PIL import ImageGrab
from PySide6.QtCore import QTimer, QObject, Signal, QThread, Slot, Qt
from PySide6.QtWidgets import QApplication

from core.config import APP_LOCAL_FOLDER
from observer.main import Observer, Subject
from helpers.time import get_random_seconds
from helpers.main import check_png_file, show_notification
from ui.styles.app import get_header_stylesheet, get_cross_platform_url
from ui.screenshot_dialog import ScreenshotDialog


class ScreenshotWorker(QObject):
    startTimerSignal = Signal()
    stopTimerSignal = Signal()
    screenshotTaken = Signal(str)

    def __init__(self, subject):
        super().__init__()
        self.ms = 100
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.capture_screenshots)
        self.active_screen = None
        self.subject = subject
        self.screenshot_time = get_random_seconds() * self.ms
        self.sdialog = ScreenshotDialog()

    @Slot()
    def start_timer_slot(self):
        logging.info(f'Screenshot taker is started...')
        logging.info(f'Screenshot will be taken in  {self.screenshot_time / self.ms}s...')
        self.timer.start(self.screenshot_time)

    @Slot()
    def stop_timer_slot(self):
        logging.info(f'Screenshot taker is stopped...')
        self.timer.stop()

    @Slot()
    def capture_screenshots(self):
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
        self.screenshot_time = get_random_seconds() * self.ms
        logging.info(f'Screenshot will be taken in  {self.screenshot_time / self.ms}s...')

    def save_screenshot(self, screenshot, monitor):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"screenshot_{monitor}_{timestamp}.png"
        filepath = os.path.join(APP_LOCAL_FOLDER, 'screenshot', filename)
        screenshot.save(filepath)
        logging.info(f'Took screenshot for {monitor} monitor...')
        if check_png_file(filepath):
            self.set_border_image(filepath)
            self.screenshotTaken.emit(filepath)

    def set_border_image(self, border_image_path):
        app = self.subject.get_app()
        app.header.setStyleSheet(get_header_stylesheet(border_image_path))


class ScreenshotTaker(QThread):

    def __init__(self, mainWindow):
        super(ScreenshotTaker, self).__init__()
        self.subject = None
        self.worker = None
        self.mainWindow = mainWindow

    def run(self):
        self.worker = ScreenshotWorker(self.subject)
        self.worker.moveToThread(self)

        self.worker.screenshotTaken.connect(self.openScreenshotDialog, Qt.QueuedConnection)
        self.worker.startTimerSignal.connect(self.worker.start_timer_slot, Qt.QueuedConnection)
        self.worker.stopTimerSignal.connect(self.worker.stop_timer_slot, Qt.QueuedConnection)
        self.worker.startTimerSignal.emit()
        self.exec_()

    @Slot(str)
    def openScreenshotDialog(self, filepath):
        if self.subject and self.subject.get_app():
            self.worker.sdialog.setStyleSheet(f'border-image: url({get_cross_platform_url(filepath)})')
            self.worker.sdialog.show()
            QTimer.singleShot(5000, self.worker.sdialog.close)
            show_notification(filepath)

    def stop(self):
        if self.worker is not None:
            self.worker.stopTimerSignal.emit()
            self.quit()

    def update(self, subject: Subject) -> None:
        self.subject = subject

        if subject.get_status():
            self.start()
        else:
            self.stop()
