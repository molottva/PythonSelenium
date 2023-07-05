# -*- coding: utf8 -*-

from pages.base_page import BasePage
from pages.components.catalog_component import Catalog


class MainPage(BasePage):
    """Класс главной страницы магазина"""

    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)
        self.catalog_component = Catalog(driver, timeout)
