import logging
import threading
from pynput import mouse
from observer.main import Observer, Subject
from storage.queries.selects import get_project, get_mouse_events
from storage.queries.inserts import get_project, create_or_update_mouse_event


class MouseListener(threading.Thread, Observer):
    def __init__(self):
        super(MouseListener, self).__init__()
        self.project = None
        self.daemon = True
        self.listener = None
        self.running = False
        self.left, self.right = 0, 0

    def on_click(self, x, y, button, pressed):
        if pressed:
            if button._name_ == 'left':
                self.left = self.left + 1
            elif button._name_ == 'right':
                self.right = self.right + 1

    def run(self):
        if not self.running:
            self.listener = mouse.Listener(on_click=self.on_click)
            self.listener.name = 'Mouse event runner'
            self.listener.start()
            self.running = True
            logging.info('mouse event listener is started')

    def stop_listener(self):
        if self.running:
            self.listener.stop()
            self.listener.join()
            self.running = False
            logging.info('mouse event listener is stoped')

    def update(self, subject: Subject) -> None:
        if subject.get_status():

            self.project = get_project(subject.get_project_name())
            if self.project is not None:
                mouse_event = get_mouse_events(self.project.id)
                if mouse_event is not None:
                    self.left = mouse_event.left
                    self.right = mouse_event.right
                else:
                    create_or_update_mouse_event(self.project.id, self.left, self.right)
                self.run()
        else:
            if self.project is not None:
                create_or_update_mouse_event(self.project.id, self.left, self.right)
            self.stop_listener()
