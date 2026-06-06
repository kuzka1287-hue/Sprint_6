from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators as Loc

class OrderPage(BasePage):
    def fill_first_form(self, name, surname, address, metro_station, phone):
        self.send_keys(Loc.NAME_INPUT, name)
        self.send_keys(Loc.SURNAME_INPUT, surname)
        self.send_keys(Loc.ADDRESS_INPUT, address)
        self.send_keys(Loc.METRO_INPUT, metro_station)
        self.click(Loc.METRO_INPUT)  # клик по выпадающему списку (если нужен выбор)
        self.send_keys(Loc.PHONE_INPUT, phone)
        self.click(Loc.NEXT_BUTTON)

    def fill_second_form(self, date, rental_period, color, comment):
        self.send_keys(Loc.DATE_INPUT, date)
        self.click(Loc.RENTAL_PERIOD)
        period_option = (Loc.RENTAL_OPTION[0], Loc.RENTAL_OPTION[1].format(rental_period))
        self.click(period_option)
        if color.lower() == "black":
            self.click(Loc.COLOR_BLACK)
        elif color.lower() == "grey":
            self.click(Loc.COLOR_GREY)
        self.send_keys(Loc.COMMENT_INPUT, comment)
        self.click(Loc.ORDER_BUTTON)

    def confirm_order(self):
        self.click(Loc.CONFIRM_BUTTON)

    def get_success_message(self):
        return self.get_text(Loc.SUCCESS_MESSAGE)