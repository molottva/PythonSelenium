# -*- coding: utf8 -*-
import re

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from data.product import Product
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as conditions

from pages.checkout_page import CheckoutPage


class CartPage(BasePage):
    """Страница корзины"""

    # Итоговая цена
    total_price = (By.CSS_SELECTOR, "[data-entity='basket-total-price']")
    # Кнопка "Оформить заказ"
    checkout_btn = (By.CSS_SELECTOR, "[data-entity='basket-checkout-button']")

    def get_cart_products(self):
        """Получение списка продуктов в корзине

        :return список списков из [товар Product, кол-во единиц в корзине]"""
        self.logger.add_start_step("Получение списка продуктов в корзине")
        result = []
        try:
            elements = self.wait.until(conditions
                                       .presence_of_all_elements_located(
                (By.CSS_SELECTOR, "[data-entity='basket-item']")))
        except TimeoutException:
            return result  # Если корзина пустая, то вернет пустой список
        for item in elements:
            vendor_code = item.find_element(By.CSS_SELECTOR, "[data-entity='basket-item-name']").text \
                .split("] ")[0]
            vendor_code = re.subn("\[", "", vendor_code)[0]  # Удаляем [
            title = item.find_element(By.CSS_SELECTOR, "[data-entity='basket-item-name']").text \
                .split("] ")[1].title()
            price = item.find_element(By.CSS_SELECTOR, "[id^='basket-item-price']").text
            price = int(re.subn(" руб", "", price)[0])  # Удаляем ' руб'
            quantity = item.find_element(By.CSS_SELECTOR, "[id^='basket-item-quantity']").get_attribute("value")
            quantity = int(quantity)
            result.append([Product(vendor_code, title, price), quantity])
        self.logger.add_end_step("Получение списка продуктов в корзине", self.get_current_url())
        return result

    def get_total_price(self):
        """Получить итоговую стоимость"""
        self.logger.add_start_step("Получение итоговой стоимости")
        result = self.read_text(self.total_price)
        result = int(re.subn(" руб", "", result)[0])  # Удаляем ' руб'
        self.logger.add_end_step(f"Получение итоговой стоимости: {result}", self.get_current_url())
        return result

    def click_checkout(self):
        """Нажать Оформить заказ"""
        self.logger.add_start_step("Нажатие на кнопку 'Оформить заказ'")
        self.click_btn(self.checkout_btn)
        self.logger.add_end_step("Нажатие на кнопку 'Оформить заказ'", self.get_current_url())
        return CheckoutPage(self.driver, self.timeout)
