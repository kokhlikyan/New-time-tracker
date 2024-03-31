import os
import sys
import logging
from pathlib import Path
from PySide6.QtWidgets import QApplication, QDialog
from ui.app.tracker import ExpenseTracker
from PySide6.QtCore import QDir
from core.config import APP_LOCAL_FOLDER
from ui.dialog import AuthDialog
from ui.screenshot_dialog import ScreenshotDialog
from storage.database import init, session_factory
from storage.queries.selects import select_session


def main():
    # Init databases
    init()
    session = select_session()
    window = ExpenseTracker()
    if session is None:
        dialog = AuthDialog()
        sdialog = ScreenshotDialog()
        sdialog.exec()
        if dialog.exec() == QDialog.Accepted:
            window.show()
            return window
    else:
        window.show()
        return window


if __name__ == '__main__':
    app = QApplication(sys.argv)
    try:
        os.makedirs(APP_LOCAL_FOLDER, exist_ok=True)
        log_file_path = os.path.join(APP_LOCAL_FOLDER, 'app.log')
        logging.basicConfig(level=logging.DEBUG, filename=log_file_path, filemode='w',
                            format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info('loging file is created...')
        os.chdir(Path.home())
        os.chdir(QDir.homePath())
        app_path = os.path.dirname(os.path.realpath(sys.argv[0]))
        os.environ["PATH"] += os.pathsep + app_path  # for Windows
        os.environ["DYLD_FALLBACK_LIBRARY_PATH"] = app_path  # for macOS
        os.environ["LD_LIBRARY_PATH"] = app_path  # for Linux

        w = main()
    except Exception as e:
        logging.error(f'Error: {e}')
    finally:
        sys.exit(app.exec())
