import re

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.order_one_click_page import OrderOneClickPage


class CheckoutPage(BasePage):
    """Страница оформления заказа"""

    # Стоимость товаров
    items_total_price = (By.CSS_SELECTOR, "#bx-soa-total .bx-soa-cart-total-line:nth-child(1) .bx-soa-cart-d")
    # Стоимость доставки
    delivery_price = (By.CSS_SELECTOR, "#bx-soa-total .bx-soa-cart-total-line:nth-child(3) .bx-soa-cart-d")
    # Итоговая стоимость
    total_price = (By.CSS_SELECTOR, "#bx-soa-total .bx-soa-cart-total-line:nth-child(4) .bx-soa-cart-d")
    # Кнопка "Купить в один клик"
    order_one_click_btn = (By.CSS_SELECTOR, "[href='/personal/preorder.php']")

    def get_item_total_price(self):
        """Получить стоимость товаров"""
        self.logger.add_start_step("Получение стоимости товаров")
        result = self.read_text(self.items_total_price)
        result = int(re.subn(" руб", "", result)[0])  # Удаляем ' руб'
        self.logger.add_end_step(f"Получение стоимости товаров: {result}", self.get_current_url())
        return result

    def get_delivery_price(self):
        """Получить стоимость доставки"""
        self.logger.add_start_step("Получение стоимости доставки")
        result = self.read_text(self.delivery_price)
        result = int(re.subn(" руб", "", result)[0])  # Удаляем ' руб'
        self.logger.add_end_step(f"Получение стоимости доставки: {result}", self.get_current_url())
        return result

    def get_total_price(self):
        """Получить итоговую стоимость"""
        self.logger.add_start_step("Получение итоговой стоимости")
        result = self.read_text(self.total_price)
        result = int(re.subn(" руб", "", result)[0])  # Удаляем ' руб'
        self.logger.add_end_step(f"Получение итоговой стоимости: {result}", self.get_current_url())
        return result

    def click_order_one_click(self):
        """Нажать Покупка в один клик"""
        self.logger.add_start_step("Нажатие на кнопку 'Купить в один клик'")
        self.click_btn(self.order_one_click_btn)
        self.logger.add_end_step("Нажатие на кнопку 'Купить в один клик'", self.get_current_url())
        return OrderOneClickPage(self.driver, self.timeout)
