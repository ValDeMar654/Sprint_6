from selenium.webdriver.common.by import By


class OrderLocators:

    # Поле "Имя" в форме Заказа
    order_form_name_field = (
        By.XPATH,
        '//input[@placeholder="* Имя"]'
    )
    
    # Ошибка заполнения поля "Имя" в форме Заказа
    order_form_name_field_err = (
        By.XPATH,
        '//div[@class="Input_ErrorMessage__3HvIb Input_Visible___syz6" '
        'and contains(text(), "Введите корректное имя")]'
    )

    # Поле "Фамилия" в форме Заказа
    order_form_surname_field = (
        By.XPATH,
        '//input[@placeholder="* Фамилия"]'
    )
    
    # Ошибка заполнения поля "Фамилия" в форме Заказа
    order_form_surname_field_err = (
        By.XPATH,
        '//div[@class="Input_ErrorMessage__3HvIb Input_Visible___syz6" '
        'and contains(text(), "Введите корректную фамилию")]'
    )

    # Поле "Адрес" в форме Заказа
    order_form_adress_field = (
        By.XPATH,
        '//input[@placeholder="* Адрес: куда привезти заказ"]'
    )

    # Ошибка заполнения поля "Адрес" в форме Заказа
    order_form_adress_field_err = (
        By.XPATH,
        '//div[@class="Input_ErrorMessage__3HvIb Input_Visible___syz6" '
        'and contains(text(), "Введите корректный адрес")]'
    )

    # Поле "Станция метро" в форме Заказа
    order_form_metro_station_field = (
        By.XPATH,
        '//input[@placeholder="* Станция метро"]'
    )

    # Поле "Телефон" в форме Заказа
    order_form_phone_field = (
        By.XPATH,
        '//input[@placeholder="* Телефон: на него позвонит курьер"]'
    )
    
    # Ошибка заполнения поля "Телефон" в форме Заказа
    order_form_phone_field_err = (
        By.XPATH,
        '//div[@class="Input_ErrorMessage__3HvIb Input_Visible___syz6" '
        'and contains(text(), "Введите корректный номер")]'
    )


    # Кнопка "Далее" в форме Заказа
    next_button_in_order_form = (
        By.XPATH,
        '//button[@class = "Button_Button__ra12g Button_Middle__1CSJM" '
        'and text() = "Далее"]'
    )

    # Поле "Когда привезти самокат" на странице Про аренду
    order_form_when_field = (
        By.XPATH,
        '//input[@placeholder="* Когда привезти самокат"]'
    )

    # Поле "Срок аренды" на странице Про аренду
    order_form_rental_period_field = (
        By.XPATH,
        '//div[@class="Dropdown-placeholder"]'
    )
    
    # Поле "Срок аренды" на странице Про аренду
    order_form_filled_rental_period_field = (
        By.XPATH,
        '//div[@class ="Dropdown-placeholder is-selected"]'
    )

    # Заголовок "Про аренду"
    about_rent_header = (
        By.XPATH,
        '//div[@class = "Order_Header__BZXOb" and text() = "Про аренду"]'
    )

    # Станция "Фили" выпадающего списка Метро
    fili_station = (
        By.XPATH,
        "//div[@class='Order_Text__2broi' and text()='Фили']"
    )

    # Пустое место на странице
    empty_space = (By.XPATH, "//div[@id='root']")

    # "семеро суток" выпадающего списка Срок аредны на странице Про аренду
    seven_days = (
        By.XPATH,
        "//div[@class='Dropdown-option' and text()='семеро суток']"
    )

    # Чек-бокс "черный жемчуг" в поле "Цвет самоката" на странице Про аренду
    black = (
        By.XPATH,
        "//input[@id='black']"
    )
    
    # Поле "Комментарий для курьера" на странице Про аренду
    order_form_courier_note_field = (
        By.XPATH,
        '//input[@placeholder = "Комментарий для курьера"]'
    )
    
    # Ошибка заполнения поля "Комментарий для курьера" на странице Про аренду
    order_form_phone_field_err = (
        By.XPATH,
        '//div[@class="Input_ErrorMessage__3HvIb Input_Visible___syz6" '
        'and contains(text(), "Тут что-то не так")]'
    )

    # Окно подтверждения заказа
    order_confirmation_window = (
        By.XPATH, '//div[@class = "Order_ModalHeader__3FDaJ" '
        'and text() = "Хотите оформить заказ?"]'
    )
        
    # Кнопка "Да" в окне подтверждения заказа
    order_confirmation_window_yes_button = (
        By.XPATH, '//div[@class = "Order_Buttons__1xGrp"]/button[text()="Да"]'
    )

    # Окно успешного заказа
    successful_order_window = (
        By.XPATH, '//div[@class = "Order_ModalHeader__3FDaJ" '
        'and text() = "Заказ оформлен"]')
