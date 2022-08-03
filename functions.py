from django.utils.timezone import localtime
import pytz

MAX_VISIT_DURATION = 25


def get_duration(visit):
    entered_time = localtime(visit.entered_at)
    left_time = localtime(visit.leaved_at)
    time_in_storage = left_time - entered_time
    seconds = time_in_storage.total_seconds()
    hours = round(seconds // 3600)
    minutes = round((seconds % 3600) // 60)
    seconds = round((seconds % 3600) // 3600)
    return hours, minutes, seconds


def format_duration(hours, minutes, seconds):
    formated_duration = f'{hours:02}:{minutes:02}:{seconds:02}'
    return formated_duration


def is_visit_long(visit, threshhold):
    hours, minutes, seconds = get_duration(visit)
    return hours * 60 + minutes > threshhold

