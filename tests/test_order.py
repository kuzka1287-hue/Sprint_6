import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.urls import BASE_URL

# Данные для заказа (два набора)
ORDER_DATA_SET_1 = {
    "name": "Николай",
    "surname": "Кузнецов",
    "address": "ул. Пушкина, 10",
    "metro": "Сокольники",
    "phone": "+79998887766",
    "date": "10.06.2025",
    "rental_period": "сутки",
    "color": "black",
    "comment": "Позвонить за час"
}

ORDER_DATA_SET_2 = {
    "name": "Екатерина",
    "surname": "Иванова",
    "address": "пр. Мира, 5",
    "metro": "Комсомольская",
    "phone": "+79161234567",
    "date": "15.06.2025",
    "rental_period": "двое суток",
    "color": "grey",
    "comment": "Домофон 123"
}

@allure.feature("Заказ самоката")
class TestOrder:
    @allure.title("Позитивный сценарий заказа через верхнюю кнопку")
    @pytest.mark.parametrize("order_data", [ORDER_DATA_SET_1, ORDER_DATA_SET_2])
    def test_successful_order_top_button(self, driver, order_data):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_order_button_top()
        self._complete_order(driver, order_data)

    @allure.title("Позитивный сценарий заказа через нижнюю кнопку")
    @pytest.mark.parametrize("order_data", [ORDER_DATA_SET_1, ORDER_DATA_SET_2])
    def test_successful_order_bottom_button(self, driver, order_data):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_order_button_bottom()
        self._complete_order(driver, order_data)

    def _complete_order(self, driver, order_data):
        order_page = OrderPage(driver)
        order_page.fill_first_form(
            order_data["name"], order_data["surname"], order_data["address"],
            order_data["metro"], order_data["phone"]
        )
        order_page.fill_second_form(
            order_data["date"], order_data["rental_period"],
            order_data["color"], order_data["comment"]
        )
        order_page.confirm_order()
        success_msg = order_page.get_success_message() 
        assert "Заказ оформлен" in success_msg
