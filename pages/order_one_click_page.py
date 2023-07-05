from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OrderOneClickPage(BasePage):
    """Страница оформления заказа при покупки в один клик"""

    # Поле 'Фамилия, Имя'
    name_input = (By.NAME, "NAME")
    # Поле 'Населенный пункт'
    city_input = (By.NAME, "CITY")
    # Поле 'E-mail'
    email_input = (By.NAME, "EMAIL")
    # Поле 'Мобильный телефон'
    phone_input = (By.NAME, "PHONE")
    # Поле 'Адрес доставки, пожелания по способам доставки и оплаты'
    description_input = (By.NAME, "ORDER_DESCRIPTION")
    # Кнопка 'Отправить заявку'
    submit_btn = (By.CSS_SELECTOR, "input[value='Отправить заявку']")

    def type_name(self, name):
        """Заполнить поле 'Фамилия, Имя'"""
        self.logger.add_start_step(f"Заполнение поля 'Фамилия, Имя' значением: {name}")
        self.type_input(self.name_input, name)
        self.logger.add_end_step(f"Заполнение поля 'Фамилия, Имя' значением: {name}", self.get_current_url())

    def type_city(self, city):
        """Заполнить поле 'Населенный пункт'"""
        self.logger.add_start_step(f"Заполнение поля 'Населенный пункт' значением: {city}")
        self.type_input(self.city_input, city)
        self.logger.add_end_step(f"Заполнение поля 'Населенный пункт' значением: {city}", self.get_current_url())

    def type_email(self, email):
        """Заполнить поле 'E-mail'"""
        self.logger.add_start_step(f"Заполнение поля 'E-mail' значением: {email}")
        self.type_input(self.email_input, email)
        self.logger.add_end_step(f"Заполнение поля 'E-mail' значением: {email}", self.get_current_url())

    def type_phone(self, phone):
        """Заполнить поле 'Мобильный телефон'"""
        self.logger.add_start_step(f"Заполнение поля 'Мобильный телефон' значением: {phone}")
        self.type_input(self.phone_input, phone)
        self.logger.add_end_step(f"Заполнение поля 'Мобильный телефон' значением: {phone}", self.get_current_url())

    def type_description(self, description):
        """Заполнить поле 'Адрес доставки, пожелания по способам доставки и оплаты'"""
        self.logger.add_start_step(f"Заполнение поля 'Адрес доставки...' значением: {description}")
        self.type_input(self.description_input, description)
        self.logger.add_end_step(f"Заполнение поля 'Адрес доставки...' значением: {description}", self.get_current_url())

    def click_submit_order(self):
        """Нажать 'Отправить заявку'"""
        self.logger.add_start_step("Нажатие на кнопку 'Отправить заявку'")
        self.click_btn(self.submit_btn)
        self.logger.add_end_step("Нажатие на кнопку 'Отправить заявку'", self.get_current_url())
