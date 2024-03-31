import logging
import threading
from PySide6.QtCore import QObject, Signal

from observer.main import Observer, Subject

locker = threading.Lock()
class KeyPressEvent(QObject):
    """Custom signal to communicate keypress events within the PySide6 event loop."""
    key_pressed = Signal(object)  # Emit the pressed key object


class KeyboardMonitor(QObject, threading.Thread):

    def __init__(self, subject):
        super().__init__()
        self.running = False
        self.count = 0
        self.subject = subject
        self.key_press_event = KeyPressEvent()
        self.key_press_event.key_pressed.connect(self.handle_key_press)

    def handle_key_press(self, key):
        locker.acquire()
        self.count = self.count + 1
        logging.info(f"Key pressed: {key}, Count: {self.count}")
        locker.release()

    def run(self):
        from pynput import keyboard

        def on_press(key):
            self.key_press_event.key_pressed.emit(key)  # Emit the key object using the signal

        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
            self.running = False

    def start_monitoring(self):
        if not self.running:
            self.running = True
            self.start()  # Start the thread

    def stop_monitoring(self):
        if self.running:
            self.running = False
            self.wait()

    def update(self, subject: Subject) -> None:
        if subject.get_status():
            pass
            # self.start()
