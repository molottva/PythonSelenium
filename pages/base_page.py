# -*- coding: utf8 -*-
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as conditions

from helpers.logger import Logger


class BasePage:
    """Класс-базовая страница, которая содержит основные функции взаимойдествия
    с веб-элементами и от которой наследуются все остальные классы-страницы.
    """

    def __init__(self, driver, timeout):
        """Инициализирующий конструктор, общий для всех классов-страниц

        :param driver - экземпляр веб-драйвера (webdriver)
        :param timeout - время ожидания в сек (int)"""
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)
        self.action = ActionChains(self.driver)
        self.logger = Logger()

    def type_input(self, locator, value):
        """Набрать текст

        :param locator - локатор веб-элемента (By, str)
        :param value - вводимое значение (str)"""
        element = self.wait.until(conditions.presence_of_element_located(locator))
        self.action.move_to_element(element).perform()
        element.clear()
        element.send_keys(value)
        print(f"Type value {value} on element with locator {locator}")

    def click_btn(self, locator):
        """Кликнуть по элементу

        :param locator - локатор веб-элемента (By, str)"""
        element = self.wait.until(conditions.presence_of_element_located(locator))
        self.action.move_to_element(element).perform()
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)
        print(f"Click on button element with locator {locator}")

    def read_text(self, locator):
        """Прочитать текст внутри элемента

        :param locator - локатор веб-элемента (By, str)
        :return - текст внутри элемента (str) """
        element = self.wait.until(conditions.presence_of_element_located(locator))
        result = element.text
        print(f"Read text {result} from element with locator {locator}")
        return result

    def get_current_url(self):
        """Прочитать текущий URL"""
        result = self.driver.current_url
        print(f"Current url: {result}")
        return result
