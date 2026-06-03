import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage

@allure.feature("Заказ самоката")
class TestOrder:
    @pytest.mark.parametrize("order_data, button_position", [
        # первый набор данных, кнопка вверху
        (
            {
                "name": "Николай",
                "surname": "Кузнецов",
                "address": "ул. Пушкина, 10",
                "metro": "Сокольники",
                "phone": "+79998887766",
                "date": "10.06.2025",
                "rental_period": "сутки",
                "color": "black",
                "comment": "Позвонить за час"
            },
            "top"
        ),
        # второй набор данных, кнопка внизу
        (
            {
                "name": "Екатерина",
                "surname": "Иванова",
                "address": "пр. Мира, 5",
                "metro": "Комсомольская",
                "phone": "+79161234567",
                "date": "15.06.2025",
                "rental_period": "двое суток",
                "color": "grey",
                "comment": "Домофон 123"
            },
            "bottom"
        )
    ])
    @allure.title("Позитивный сценарий заказа с кнопкой '{button_position}'")
    def test_successful_order(self, driver, order_data, button_position):
        driver.get("https://qa-scooter.praktikum-services.ru/")
        main_page = MainPage(driver)
        if button_position == "top":
            main_page.click_order_button_top()
        else:
            main_page.click_order_button_bottom()

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