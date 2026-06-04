import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as Loc
from data.urls import BASE_URL

class MainPage(BasePage):
    @allure.step("Нажать кнопку 'Заказать' (верхняя)")
    def click_order_button_top(self):
        self.click(Loc.ORDER_BUTTON_TOP)

    @allure.step("Нажать кнопку 'Заказать' (нижняя)")
    def click_order_button_bottom(self):
        self.scroll_to_element(Loc.ORDER_BUTTON_BOTTOM)
        self.click(Loc.ORDER_BUTTON_BOTTOM)

    @allure.step("Нажать логотип 'Самокат'")
    def click_scooter_logo(self):
        self.click(Loc.SCOOTER_LOGO)

    @allure.step("Нажать логотип 'Яндекс'")
    def click_yandex_logo(self):
        self.click(Loc.YANDEX_LOGO)

    @allure.step("Получить текст ответа на вопрос №{index}")
    def get_faq_answer_text(self, index):
        question_loc = (Loc.QUESTION_PATTERN[0], Loc.QUESTION_PATTERN[1].format(index))
        self.scroll_to_element(question_loc)
        self.click(question_loc)
        answer_loc = (Loc.ANSWER_PATTERN[0], Loc.ANSWER_PATTERN[1].format(index))
        return self.get_text(answer_loc)

    def open(self):
        self.driver.get(BASE_URL)
