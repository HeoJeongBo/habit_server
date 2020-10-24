import datetime
from django.core.exceptions import ValidationError


def parsing_time_from_str(str):
    try:
        return datetime.datetime.strptime(str, '%Y-%m-%d')
    except ValueError:
        print('esdad')
