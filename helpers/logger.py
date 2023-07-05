# -*- coding: utf8 -*-

import os

from helpers import datetime_helper


class Logger:
    now = datetime_helper.now_by_pattern("__%Y-%m-%d__%H-%M-%S")
    file_name = f"D:\\Git\\Shipmodeling\\artefacts\\logs\\log{now}.log"
    timer_step = None
    timer_test = None

    @classmethod
    def add_start_step(cls, step):
        cls.timer_step = datetime_helper.now()
        data_to_add = f"-----|-----|-----|-----|-----|-----|-----|-----|-----\n" \
                      f"Start step: {step}\n"
        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_end_step(cls, step, url):
        data_to_add = f"Finish step: {step}\n" \
                      f"Current URL: {url}\n" \
                      f"Duration step: {datetime_helper.duration(cls.timer_step, datetime_helper.now())}\n" \
                      f"-----|-----|-----|-----|-----|-----|-----|-----|-----\n"
        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_start_test(cls):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')
        cls.timer_test = datetime_helper.now()
        data_to_add = f"*****|*****|*****|*****|*****|*****|*****|*****|*****\n" \
                      f"Start test: {test_name}\n" \
                      f"Start time: {datetime_helper.now_by_pattern('%Y-%m-%d %H:%M:%S')}\n"
        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_end_test(cls, url):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')
        data_to_add = f"Finish test: {test_name}\n" \
                      f"Current URL: {url}\n" \
                      f"Finish time: {datetime_helper.now_by_pattern('%Y-%m-%d %H:%M:%S')}\n" \
                      f"Duration test: {datetime_helper.duration(cls.timer_test, datetime_helper.now())}\n" \
                      f"*****|*****|*****|*****|*****|*****|*****|*****|*****\n"
        cls.write_log_to_file(data_to_add)

    @classmethod
    def write_log_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf=8') as logger_file:
            logger_file.write(data)
