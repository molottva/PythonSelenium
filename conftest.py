# -*- coding: utf8 -*-

import pytest
from selenium import webdriver

from helpers.logger import Logger


@pytest.fixture
def driver_setup():
    """Запуск и настройка экземпляра веб-драйвера перед тестом
    и переход на главную страницу магазина.
    Закрытие драйвера по окончанию теста.
    """
    driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
    driver.maximize_window()
    Logger.add_start_test()
    driver.get("https://www.shipmodeling.ru/")
    yield driver
    Logger.add_end_test(driver.current_url)
    driver.quit()
