class Product:
    """Дата-класс сущности 'Товар'"""

    def __init__(self, vendor_code, title, price):
        """Инициализирующий конструктор для сущности 'Товар'

        :param vendor_code - артикул товара (str)
        :param title - название товара (str)
        :param price - цена за единицу товара (int)"""
        self.vendor_code = vendor_code
        self.title = title
        self.price = price

    def get_vendor_code(self):
        return self.vendor_code

    def get_title(self):
        return self.title

    def get_price(self):
        return self.price
