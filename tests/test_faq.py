import allure
import pytest
from pages.main_page import MainPage
from data.urls import BASE_URL
from data.faq_data import FAQ_EXPECTED_ANSWERS

@allure.feature("Главная страница")
@allure.story("Выпадающий список 'Вопросы о важном'")
class TestFAQ:
    @pytest.mark.parametrize("q_index, expected_text", FAQ_EXPECTED_ANSWERS)
    @allure.title("Текст ответа на вопрос №{q_index} соответствует ожиданию")
    def test_faq_answer_text(self, driver, q_index, expected_text):
        main_page = MainPage(driver)
        main_page.open()
        actual = main_page.get_faq_answer_text(q_index)
        assert actual == expected_text
 
