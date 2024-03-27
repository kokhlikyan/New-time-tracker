import sys
import random
from PySide6.QtCore import QTimer, QThread, Signal, QObject
from PySide6.QtWidgets import QApplication

class ScreenshotWorker(QObject):
    screenshot_signal = Signal()

    def __init__(self):
        super().__init__()

    def run_taker(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.capture_screenshots)
        self.timer.start(5000)

    def capture_screenshots(self):
        # Your screenshot capturing logic goes here
        print("Capturing screenshots...")

    def stop(self):
        self.timer.stop()

class ScreenshotThread(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        self.worker = ScreenshotWorker()
        self.worker.run_taker()
        self.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    thread = ScreenshotThread()
    thread.start()

    sys.exit(app.exec_())
