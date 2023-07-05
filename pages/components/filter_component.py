# -*- coding: utf8 -*-
import enum

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as conditions

from pages.base_page import BasePage


class FilterComponent(BasePage):
    """Класс компонента магазина 'Подбор по параметрам'"""

    # 'Header' выпадающего меню 'Подбор по параметрам'
    filter_header = (By.CSS_SELECTOR, ".b-sbBlock-head")
    # Тело выпадающего меню 'Подбор по параметрам'
    filter_body = (By.CSS_SELECTOR, ".bx-filter .bx-filter-section")
    # Минимальная цена
    min_price_input = (By.ID, "arrFilter_P2_MIN")
    # Максимальная цена
    max_price_input = (By.ID, "arrFilter_P2_MAX")
    # Кнопка "Показать"
    submit_filter_btn = (By.ID, "set_filter")

    def set_min_price(self, price):
        """Установить минимальную цену"""
        self.logger.add_start_step(f"Установка минимальной цены: {price}")
        self.expand_filters()
        self.type_input(self.min_price_input, price)
        self.logger.add_end_step(f"Установка минимальной цены: {price}", self.get_current_url())

    def set_max_price(self, price):
        """Установить максимальную цену"""
        self.logger.add_start_step(f"Установка максимальной цены: {price}")
        self.expand_filters()
        self.type_input(self.max_price_input, price)
        self.logger.add_end_step(f"Установка максимальной цены: {price}", self.get_current_url())

    def set_manufacturer(self, manufacturer):
        """Выбор производителя"""
        self.logger.add_start_step(f"Выбор производителя: {manufacturer.name}")
        self.expand_filters()
        self.click_btn(manufacturer.value)
        self.logger.add_end_step(f"Выбор производителя: {manufacturer.name}", self.get_current_url())

    def click_submit(self):
        """Кликнуть 'Показать'"""
        self.logger.add_start_step("Клик на кнопку 'Показать' в 'Подбор по параметрам'")
        self.expand_filters()
        self.click_btn(self.submit_filter_btn)
        self.logger.add_end_step("Клик на кнопку 'Показать' в 'Подбор по параметрам'", self.get_current_url())

    def expand_filters(self):
        """Раскрыть компонент 'Подбор по параметрам'"""
        if not self.is_filters_open():
            self.click_btn(self.filter_header)
            self.wait.until(conditions.visibility_of_element_located(self.filter_body))

    def is_filters_open(self):
        attr = self.driver.find_element(*self.filter_body).get_attribute("style")
        return "display: none;" not in attr


class Manufacturers(enum.Enum):
    """Перечисление производителей"""

    # МастерКорабел
    master_corabel = (By.XPATH, "//span[@title='МастерКорабел']//parent::span/input")
