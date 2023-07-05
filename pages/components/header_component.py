from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.cart_page import CartPage


class HeaderComponent(BasePage):
    """Класс компонента header"""

    # Статус корзины
    cart_status = (By.CSS_SELECTOR, ".bx-basket-block div:nth-child(1)")
    # Кнопка "Оформление"
    cart_btn = (By.CSS_SELECTOR, ".bx-basket-block div:nth-child(2)")

    def get_cart_status(self):
        """Получение статуса корзины"""
        self.logger.add_start_step("Получение статуса корзины")
        self.driver.refresh()
        result = self.read_text(self.cart_status)
        self.logger.add_end_step(f"Получение статуса корзины: {result}", self.get_current_url())
        return result

    def open_cart(self):
        """Перейти на страницу корзины"""
        self.logger.add_start_step("Переход на стриницу корзины")
        self.click_btn(self.cart_btn)
        self.logger.add_end_step("Переход на стриницу корзины", self.get_current_url())
        return CartPage(self.driver, self.timeout)
