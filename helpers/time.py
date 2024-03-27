import datetime
import math
import random

from PySide6.QtCore import QTime

from storage.queries.selects import get_project


def get_random_seconds():
    current_time = datetime.datetime.now()

    current_seconds = (current_time.minute % 10) * 60
    return random.randint(current_seconds, 600)


def format_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def format_qtime(seconds):
    hours, remainder = divmod(seconds or 0, 3600)
    minutes, seconds = divmod(remainder, 60)
    qtime = QTime()
    qtime.setHMS(hours, minutes, seconds)
    return qtime


def qtime_to_seconds(qtime):
    milliseconds = qtime.msecsSinceStartOfDay()
    seconds = milliseconds / 1000
    return int(seconds)
