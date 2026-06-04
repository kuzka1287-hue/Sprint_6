import allure
from pages.main_page import MainPage
from data.urls import BASE_URL, ORDER_PAGE_URL, DZEN_URL_PATTERN

@allure.feature("Логотипы")
class TestLogoRedirect:
    @allure.title("Клик по логотипу 'Самокат' возвращает на главную страницу")
    def test_scooter_logo_redirects_to_main(self, driver):
        main_page = MainPage(driver)
        driver.get(ORDER_PAGE_URL)           # переход на страницу заказа
        main_page.click_scooter_logo()
        assert main_page.get_current_url() == BASE_URL

    @allure.title("Клик по логотипу 'Яндекс' открывает Дзен в новой вкладке")
    def test_yandex_logo_redirects_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_yandex_logo()
        new_window_url = main_page.get_new_window_url()
        assert DZEN_URL_PATTERN in new_window_url
 
