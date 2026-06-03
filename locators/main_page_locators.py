from selenium.webdriver.common.by import By

class MainPageLocators:
    # Кнопки заказа
    ORDER_BUTTON_TOP = (By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Button_ml__1HXwb' and text()='Заказать']")

    # Вопросы и ответы (FAQ)
    QUESTION_PATTERN = (By.ID, "accordion__heading-{}")      # место для индекса
    ANSWER_PATTERN = (By.XPATH, "//div[@id='accordion__panel-{}']/p")

    # Логотипы
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")