import re

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as conditions

from data.product import Product
from pages.base_page import BasePage
from pages.components.filter_component import FilterComponent
from pages.components.header_component import HeaderComponent


class StorePage(BasePage):
    """Страница магазина с товарами"""

    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)
        self.filter_component = FilterComponent(self.driver, self.timeout)
        self.header_component = HeaderComponent(self.driver, self.timeout)

    # Карточка товара
    product_item = ()

    def get_products(self):
        """Получить список всех текущих товаров на странице"""
        self.logger.add_start_step("Получение списка товаров на странице")
        result = []
        try:
            elements = self.wait.until(conditions
                                       .presence_of_all_elements_located((By.CSS_SELECTOR, "[data-entity='item']")))
        except TimeoutException:
            return result  # Если товар отсутствует, то вернет пустой список
        for item in elements:
            vendor_code = item.find_element(By.CSS_SELECTOR, ".product-item-title-art").text
            vendor_code = re.subn("[\[|\]]", "", vendor_code)[0]  # Удаляем [ и ]
            title = item.find_element(By.CSS_SELECTOR, ".product-item-title a").text
            title = re.subn("Сборная модель ", "", title)[0]  # Удаляем "Сборная модель "
            price = item.find_element(By.CSS_SELECTOR, ".product-item-price-current").text
            price = int(re.subn(" руб", "", price)[0])  # Удаляем ' руб'
            result.append(Product(vendor_code, title, price))
        self.logger.add_end_step("Получение списка товаров на странице", self.get_current_url())
        return result

    def add_to_cart(self, vendor_code, quantity):
        """Добавить товар в корзину

        :param vendor_code - артикул добавляемого товара
        :param quantity - кол-во добавляемого товара"""
        self.logger.add_start_step(f"Добавление в корзину товара с артикулом {vendor_code} в количестве {quantity}")
        item = self.driver.find_element(By.XPATH, f"//*[@data-entity='item' and contains(., '[{vendor_code}]')]")
        self.action.move_to_element(item) \
            .send_keys_to_element(item.find_element(By.NAME, "quantity"), Keys.DELETE) \
            .send_keys_to_element(item.find_element(By.NAME, "quantity"), quantity) \
            .click(item.find_element(By.CSS_SELECTOR, "[onclick*='BUY_BTN']")) \
            .perform()
        self.logger.add_end_step(f"Добавление в корзину товара с артикулом {vendor_code} в количестве {quantity}",
                                 self.get_current_url())
