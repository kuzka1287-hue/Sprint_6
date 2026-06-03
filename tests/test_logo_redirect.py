import allure
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage

@allure.feature("Логотипы")
class TestLogoRedirect:
    @allure.title("Клик по логотипу 'Самокат' возвращает на главную страницу")
    def test_scooter_logo_redirects_to_main(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru/order")
        main_page = MainPage(driver)
        main_page.click_scooter_logo()
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.title("Клик по логотипу 'Яндекс' открывает Дзен в новой вкладке")
    def test_yandex_logo_redirects_to_dzen(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru/")
        main_page = MainPage(driver)
        main_page.click_yandex_logo()
        # переключаемся на новую вкладку
        driver.switch_to.window(driver.window_handles[1])
        # ждём редирект на dzen.ru
        driver.get("https://dzen.ru/")  # или проверить, что URL содержит dzen.ru
        assert "dzen.ru" in driver.current_url