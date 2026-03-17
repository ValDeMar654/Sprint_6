from selenium.webdriver.common.by import By


class BaseLocators:
    # Кнопка "Заказать" в хедере
    order_button_in_header = (
        By.XPATH,
        '//button[@class = "Button_Button__ra12g" and text() = "Заказать"]'
    )

    # Кнопка "Закакзать" в середине страницы
    order_button_in_middle = (
        By.XPATH,
        '//button[@class = "Button_Button__ra12g Button_Middle__1CSJM" '
        'and text() = "Заказать"]'
    )
    
    # Заголовок "Самокат"
    scooter_header = (
        By.XPATH, '//div[@class="Home_Header__iJKdX" '
                      'and text()="Самокат "]'
                      )
    
    # Заголовок "Вопросы о важном"
    questions_about_metters_header = (
        By.XPATH, '//div[text()="Вопросы о важном"]'
        )
    
    # Логотип Яндекс
    yandex_logo = (By.XPATH, '//a[contains(@class, "Header_LogoYandex")]')

    # Логотип Самокат
    scooter_logo = (By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]')
    
    # Пустое место на странице
    empty_space = (By.XPATH, "//div[@id='root']")
    
    # Логотип Дзен
    dzen_logo = (By.XPATH, '//div[@data-testid="floor-title-text" and text()="Новости"]')
