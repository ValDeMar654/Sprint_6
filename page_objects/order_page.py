import time

import allure

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from urls import scooter_main_page



class Order:

    rental_period_text = None

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем появления кнопки "Заказать" в хедере')
    def wait_for_load_header(self, order_locators):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(
                order_locators.order_button_in_header
            )
        )

    @allure.step('Кликаем на кнопку "Заказать" в хедере')
    def select_order_button_in_header(self, order_locators):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(
                order_locators.order_button_in_header
            )).click()

    @allure.step('Кликаем на кнопку "Заказать" в середине страницы')
    def select_order_button_in_middle(self, order_locators):
        order_button_in_middle = WebDriverWait(self.driver, 3).until(
            expected_conditions.presence_of_element_located(
                order_locators.order_button_in_middle))

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            order_button_in_middle
        )

        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(
                order_locators.order_button_in_middle)).click()

    @allure.step('Ищем поле "Имя" в форме Заказа и заполняем его')
    def set_name_field(self, order_locators, name):
        self.driver.find_element(
            *order_locators.order_form_name_field).send_keys(name)
        self.click_empty_space(order_locators)

    @allure.step('Проверяем отсутсвие ошибки заполнения поля Имя')
    def check_name_field(self, order_locators):
        assert WebDriverWait(self.driver, 3).until(
            expected_conditions.invisibility_of_element_located(
                order_locators.order_form_name_field_err)
        )

    @allure.step('Ищем поле "Фамилия" в форме Заказа и заполняем его')
    def set_surname_field(self, order_locators, surname):
        self.driver.find_element(
            *order_locators.order_form_surname_field).send_keys(surname)
        self.click_empty_space(order_locators)

    @allure.step('Проверяем отсутсвие ошибки заполнения поля Фамилия')
    def check_surname_field(self, order_locators):
        assert WebDriverWait(self.driver, 3).until(
            expected_conditions.invisibility_of_element_located(
                order_locators.order_form_surname_field_err)
        )

    @allure.step('Ищем поле "Адрес" в форме Заказа и заполняем его')
    def set_adress_field(self, order_locators, adress):
        self.driver.find_element(
            *order_locators.order_form_adress_field).send_keys(adress)
        self.click_empty_space(order_locators)

    @allure.step('Проверяем отсутсвие ошибки заполнения поля Адрес')
    def check_adress_field(self, order_locators):
        assert WebDriverWait(self.driver, 3).until(
            expected_conditions.invisibility_of_element_located(
                order_locators.order_form_adress_field_err)
        )

    @allure.step('Ищем поле "Станция метро" в форме Заказа и выбираем станцию')
    def set_metro_station_field(self, order_locators):
        self.driver.find_element(
            *order_locators.order_form_metro_station_field).click()

        metro_station = WebDriverWait(self.driver, 3).until(
            expected_conditions.presence_of_element_located(
                order_locators.fili_station))

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", metro_station)

        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(
                order_locators.fili_station)).click()

    @allure.step('Ищем поле "Телефон" в форме Заказа и заполняем его')
    def set_phone_field(self, order_locators, phone):
        self.driver.find_element(
            *order_locators.order_form_phone_field).send_keys(phone)
        self.click_empty_space(order_locators)

    @allure.step('Проверяем отсутсвие ошибки заполнения поля Телефон')
    def check_phone_field(self, order_locators):
        assert WebDriverWait(self.driver, 3).until(
            expected_conditions.invisibility_of_element_located(
                order_locators.order_form_phone_field_err)
        )

    @allure.step('Клик по пусому месту')
    def click_empty_space(self, order_locators):
        ActionChains(self.driver).move_to_element_with_offset(
            self.driver.find_element(
                *order_locators.empty_space
            ), 2, 300).click().perform()

    @allure.step('Ищем кнопку "Далее" и кликаем')
    def select_next_button(self, order_locators):
        self.driver.find_element(
            *order_locators.next_button_in_order_form).click()

    @allure.step('Ждём кода появится форма с заголовком "Про аренду"')
    def wait_about_rent_header(self, order_locators):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(
                order_locators.about_rent_header)
        )

    @allure.step(
        'Ищем поле "Когда привезти самокат" в форме Заказа и заполняем его')
    def set_when_field(self, order_locators, when_date):
        self.driver.find_element(
            *order_locators.order_form_when_field).send_keys(when_date)
        self.click_empty_space(order_locators)

    @allure.step(
        'Проверяем что в поле "Когда привезти самокат" указаны введеные данные'
    )
    def check_when_field(self, order_locators, when_date):
        assert self.driver.find_element(
            *order_locators.order_form_when_field
        ).get_attribute("value") == when_date

    @allure.step('Ищем поле "Срок аренды" в форме Заказа и кликаем')
    def set_rental_period_field(self, order_locators):
        self.driver.find_element(
            *order_locators.order_form_rental_period_field).click()

        rental_period = WebDriverWait(self.driver, 3).until(
            expected_conditions.presence_of_element_located(
                order_locators.seven_days))

        self.rental_period_text = rental_period.text

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", rental_period)

        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(
                order_locators.seven_days)).click()
        self.click_empty_space(order_locators)

    @allure.step('Проверяем что в поле "Срок аренды" указаны введеные данные')
    def check_rental_period_field(self, order_locators):
        assert self.driver.find_element(
            *order_locators.order_form_filled_rental_period_field
        ).text == self.rental_period_text

    @allure.step('Ищем чек-бокс "чёрный жемчуг" и кликаем')
    def set_black_check_box(self, order_locators):
        self.driver.find_element(*order_locators.black).click()

    @allure.step(
        'Ищем поле "Комментарий для курьера" в форме Заказа и заполняем его')
    def set_courier_note_field(self, order_locators, courier_note):
        self.driver.find_element(
            *order_locators.order_form_courier_note_field).send_keys(
                courier_note
        )
        self.click_empty_space(order_locators)

    @allure.step(
        'Проверяем что в поле "Комментарий для курьера" '
        'указаны введеные данные')
    def check_courier_note_field(self, order_locators, courier_note):
        assert self.driver.find_element(
            *order_locators.order_form_courier_note_field
        ).get_attribute("value") == courier_note

    @allure.step('Проверяем появление окна подтверждения заказа')
    def check_order_confirmation_window(self, order_locators):
        assert WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(
                order_locators.order_confirmation_window))

    @allure.step('Кликаем на кнопку "Да" в окне подтверждения заказа')
    def select_order_confirmation_window_yes_button(self, order_locators):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(
                order_locators.order_confirmation_window_yes_button
            )).click()

    @allure.step('Проверяем появление окна успешного заказа')
    def check_successful_order_window(self, order_locators):
        assert WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(
                order_locators.successful_order_window))

    @allure.step(
        'Кликаем на кнопку "Посмотреть статус" в окне успешного заказа')
    def select_view_status_button(self, order_locators):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(
                order_locators.successful_order_window_view_status_button
            )).click()

    @allure.step('# Кликаем на логотип Самокат')
    def select_scooter_logo(self, order_locators):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(
                order_locators.scooter_logo)).click()
        time.sleep(2)

    @allure.step('Проверяем что по клику на логотип Самокат осуществляется '
                 'переход на главную страницу «Самоката»')
    def check_scooter_logo_transition(self):
        assert (
            self.driver.current_url == scooter_main_page
        )

    @allure.step('Кликаем на логотип Яндекс')
    def select_yandex_logo(self, order_locators):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(
                order_locators.yandex_logo)).click()
        time.sleep(2)

    @allure.step('Проверяем что по клику на логотип Яндекс осуществляется '
                 'переход на главную страницу Дзен в новом окне')
    def check_yandex_logo_transition(self):

        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])
            assert "dzen" in self.driver.current_url
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
        else:
            raise Exception("Страница должна была открыться в новом окне.")

    @allure.step('Шаг по заполнению и проверке полей формы "Для кого самокат"')
    def filling_and_checks_for_whom_form(self, order_locators, name, surname,
                                         adress, phone):
        self.set_name_field(order_locators, name)
        self.check_name_field(order_locators)
        self.set_surname_field(order_locators, surname)
        self.check_surname_field(order_locators)
        self.set_adress_field(order_locators, adress)
        self.check_adress_field(order_locators)
        self.set_metro_station_field(order_locators)
        self.set_phone_field(order_locators, phone)
        self.check_phone_field(order_locators,)

    @allure.step('Шаг по заполнению и проверке полей формы "Про аренду"')
    def filling_and_checks_about_rent_form(self, order_locators, when_date,
                                           courier_note):
        self.set_when_field(order_locators, when_date)
        self.check_when_field(order_locators, when_date)
        self.set_rental_period_field(order_locators,)
        self.check_rental_period_field(order_locators,)
        self.set_black_check_box(order_locators,)
        self.set_courier_note_field(order_locators, courier_note)
        self.check_courier_note_field(order_locators, courier_note)

    @allure.step('Весь флоу позитивного сценария')
    def whole_order_flow(
            self, order_locators, name, surname, adress, phone, when_date,
            courier_note):
        self.filling_and_checks_for_whom_form(order_locators,
                                              name, surname, adress, phone)
        self.select_next_button(order_locators)
        self.wait_about_rent_header(order_locators)
        self.filling_and_checks_about_rent_form(
            order_locators, when_date, courier_note)
        self.select_order_button_in_middle(order_locators)
        self.check_order_confirmation_window(order_locators)
        self.select_order_confirmation_window_yes_button(order_locators)
        self.check_successful_order_window(order_locators)
        self.select_view_status_button(order_locators)
        self.select_scooter_logo(order_locators)
        self.check_scooter_logo_transition()
        self.select_yandex_logo(order_locators)
        self.check_yandex_logo_transition()
