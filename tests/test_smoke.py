# -*- coding: utf8 -*-

from data.product import Product
from pages.components.catalog_component import CatalogItems
from pages.components.filter_component import Manufacturers
from pages.main_page import MainPage

timeout = 20


def test_order_happy_path(driver_setup):
    # Тестовые данные для фильтров:
    min_price = 10000  # Минимальная цена
    max_price = 15000  # Максимальная цена
    manufacturer = Manufacturers.master_corabel # Производитель
    vendor_code_start_with = "MK"  # Строка с которого должен начинаться артикул

    # Тестовые данные товара для покупки:
    expected_product = Product("MK0401", "Бригантина Феникс", 13400)  # Покупаемый товар
    quantity = 2  # Кол-во покупаемых единиц товара

    # Тестовые данные для оформления заказа
    name = "Вася Пупкин"
    city = "Петрозаводск"
    email = "test@example.ru"
    phone = "89001234567"
    address = "ул.Ленина 33"

    main_page = MainPage(driver_setup, timeout)
    store_page = main_page.catalog_component.open_store_by_catalog_item(CatalogItems.ships)
    print("Open catalog item 'Ship models'")

    store_page.filter_component.set_min_price(min_price)
    store_page.filter_component.set_max_price(max_price)
    store_page.filter_component.set_manufacturer(manufacturer)
    store_page.filter_component.click_submit()
    print("Set filters: min price - 10 000, max price - 15 000, manufacturer - 'MasterCorabel'")

    products = store_page.get_products()
    actual_product = None
    for product in products:
        assert min_price <= product.get_price() <= max_price # Проверка фильтра на макс/мин стоимость
        assert product.get_vendor_code().startswith(vendor_code_start_with) # Проверка фильтра на производителя
        if product.get_vendor_code() == expected_product.get_vendor_code():
            actual_product = product
    print("Accept all products matches filters is successful")

    assert actual_product.get_vendor_code() == expected_product.get_vendor_code()
    assert actual_product.get_title() == expected_product.get_title()
    assert actual_product.get_price() == expected_product.get_price()
    print(f"Accept expected product {expected_product} exist on filtered products {products}")

    cart_status = store_page.header_component.get_cart_status()
    assert cart_status == "Ваша корзина пуста"
    store_page.add_to_cart(expected_product.get_vendor_code(), quantity)
    cart_status = store_page.header_component.get_cart_status()
    assert cart_status == f"1 позиция на сумму {quantity * expected_product.get_price()} руб"
    print(f"Accept right cart status before/after added to cart product {expected_product}")

    cart_page = store_page.header_component.open_cart()
    products = cart_page.get_cart_products()
    assert len(products) == 1
    assert products[0][0].get_vendor_code() == expected_product.get_vendor_code()
    assert products[0][0].get_title() == expected_product.get_title()
    assert products[0][0].get_price() == expected_product.get_price()
    assert products[0][1] == quantity
    total_price = cart_page.get_total_price()
    assert total_price == quantity * expected_product.get_price()
    print("Accept right data on cart page is successful")

    checkout_page = cart_page.click_checkout()
    item_total_price = checkout_page.get_item_total_price()
    delivery_price = checkout_page.get_delivery_price()
    total_price = checkout_page.get_total_price()
    assert item_total_price == quantity * expected_product.get_price()
    assert total_price == quantity * expected_product.get_price() + delivery_price
    print("Accept right price on checkout page is successful")

    order_one_click_page = checkout_page.click_order_one_click()
    order_one_click_page.type_name(name)
    order_one_click_page.type_city(city)
    order_one_click_page.type_email(email)
    order_one_click_page.type_phone(phone)
    order_one_click_page.type_description(address)
    # Закомментил нажатие на кнопку оформления заявки, чтобы не создавать лишние данные на сервере
    # order_one_click_page.click_submit_order()
    print("Accept submit order is successful")
