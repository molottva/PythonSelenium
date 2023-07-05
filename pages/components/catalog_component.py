# -*- coding: utf8 -*-

import enum

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as conditions

from pages.base_page import BasePage
from pages.store_page import StorePage


class Catalog(BasePage):
    """Класс-компонент 'Каталог товаров'"""

    def open_store_by_catalog_item(self, catalog_item):
        """Открыть магазин с товарами определенной категории

        :param catalog_item - категория товара в каталоге (CatalogItems)"""
        self.logger.add_start_step(f"Открыть товары категории: {catalog_item.name}")
        self.click_btn(catalog_item.value)
        self.wait.until(conditions.presence_of_element_located((By.CSS_SELECTOR, ".product-item-container")))
        self.logger.add_end_step(f"Открыть товары категории: {catalog_item.name}", self.get_current_url())
        return StorePage(self.driver, self.timeout)


class CatalogItems(enum.Enum):
    """Перечисление позиций каталога"""

    # Модели кораблей
    ships = (By.CSS_SELECTOR, ".itb_content_catalog_wrap [href*='modeli_korabley']")
    # Элементы
    elements = (By.CSS_SELECTOR, ".itb_content_catalog_wrap [href*='model_elements']")
    # Материалы
    materials = (By.CSS_SELECTOR, ".itb_content_catalog_wrap [href*='materials']")
    # Ручные инструменты
    hand_tools = (By.CSS_SELECTOR, ".itb_content_catalog_wrap [href*='ruchnye_instrumenty']")
