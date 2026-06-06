from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as Loc

class MainPage(BasePage):
    def click_order_button_top(self):
        self.click(Loc.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        self.scroll_to_element(Loc.ORDER_BUTTON_BOTTOM)
        self.click(Loc.ORDER_BUTTON_BOTTOM)

    def click_scooter_logo(self):
        self.click(Loc.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(Loc.YANDEX_LOGO)

    def get_faq_answer_text(self, index):
        question_loc = (Loc.QUESTION_PATTERN[0], Loc.QUESTION_PATTERN[1].format(index))
        self.scroll_to_element(question_loc)
        self.click(question_loc)
        answer_loc = (Loc.ANSWER_PATTERN[0], Loc.ANSWER_PATTERN[1].format(index))
        return self.get_text(answer_loc)