# -*- coding: utf8 -*-

from datetime import datetime


def now():
    return datetime.now()


def now_by_pattern(pattern):
    return now().strftime(pattern)


def duration(start, end):
    return end - start
