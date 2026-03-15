import allure

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_locators import BaseLocators
from locators.order_locators import OrderLocators
from page_objects.base_page import Base
from urls import scooter_main_page


class Order:

    rental_period_text = None

    def __init__(self, driver):
        self.driver = driver
        self.base = Base(self.driver)

    @allure.step('Кликаем на кнопку "Заказать" в хедере')
    def select_order_button_in_header(self):
        self.base.click_for_element(BaseLocators.order_button_in_header)

    @allure.step('Скролл страницы до кнопки "Заказать" в середине страницы')
    def scrol_until_order_button_in_middle_located(self):
        self.base.scrol_until_element_located(BaseLocators.order_button_in_middle)

    @allure.step('Клик по кнопке "Заказать" в середине страницы')
    def select_order_button_in_middle(self):
        self.base.click_for_element(BaseLocators.order_button_in_middle)

    @allure.step('Ищем поле "Имя" в форме Заказа и заполняем его')
    def set_name_field(self, name):
        self.base.fill_field(element=OrderLocators.order_form_name_field, value=name)
        self.base.click_empty_space(BaseLocators)

    @allure.step('Проверяем отсутсвие ошибки заполнения поля Имя')
    def check_name_field(self):
        return self.driver.find_elements(*OrderLocators.order_form_name_field_err)
            
    @allure.step('Ищем поле "Фамилия" в форме Заказа и заполняем его')
    def set_surname_field(self, surname):
        self.base.fill_field(element=OrderLocators.order_form_surname_field, value=surname)
        self.base.click_empty_space(BaseLocators)

    @allure.step('Проверяем отсутсвие ошибки заполнения поля Фамилия')
    def check_surname_field(self):
        return self.driver.find_elements(*OrderLocators.order_form_surname_field_err)
        
    @allure.step('Ищем поле "Адрес" в форме Заказа и заполняем его')
    def set_adress_field(self, adress):
        self.base.fill_field(element=OrderLocators.order_form_adress_field, value=adress)
        self.base.click_empty_space(BaseLocators)

    @allure.step('Проверяем отсутсвие ошибки заполнения поля Адрес')
    def check_adress_field(self):
        return self.driver.find_elements(*OrderLocators.order_form_adress_field_err)

    @allure.step('Ищем поле "Станция метро" в форме Заказа и выбираем станцию')
    def set_metro_station_field(self):
        self.driver.find_element(
            *OrderLocators.order_form_metro_station_field).click()

        metro_station = WebDriverWait(self.driver, 3).until(
            expected_conditions.presence_of_element_located(
                OrderLocators.fili_station))

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", metro_station)

        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(
                OrderLocators.fili_station)).click()

    @allure.step('Ищем поле "Телефон" в форме Заказа и заполняем его')
    def set_phone_field(self, phone):
        self.base.fill_field(element=OrderLocators.order_form_phone_field, value=phone)
        self.base.click_empty_space(BaseLocators)

    @allure.step('Проверяем отсутсвие ошибки заполнения поля Телефон')
    def check_phone_field(self):
        return self.driver.find_elements(*OrderLocators.order_form_phone_field_err)

    @allure.step('Ищем кнопку "Далее" и кликаем')
    def select_next_button(self):
        self.base.click_for_element(OrderLocators.next_button_in_order_form)

    @allure.step('Ждём кода появится форма с заголовком "Про аренду"')
    def wait_about_rent_header(self):
        self.base.wait_for_visibility_element(OrderLocators.about_rent_header)

    @allure.step(
        'Ищем поле "Когда привезти самокат" в форме Заказа и заполняем его')
    def set_when_field(self, when_date):
        self.base.fill_field(element=OrderLocators.order_form_when_field, value = when_date)
        self.base.click_empty_space(BaseLocators)

    @allure.step(
        'Проверяем что в поле "Когда привезти самокат" указаны введеные данные'
    )
    def check_when_field(self):
        return self.driver.find_element(
            *OrderLocators.order_form_when_field
        ).get_attribute("value")

    @allure.step('Ищем поле "Срок аренды" в форме Заказа и кликаем')
    def set_rental_period_field(self):
        self.base.click_for_element(
            OrderLocators.order_form_rental_period_field)
        self.rental_period_text = self.base.wait_for_element_load_in_dom(
            OrderLocators.seven_days).text
        self.base.scrol_until_element_located(OrderLocators.seven_days)
        self.base.click_for_element(OrderLocators.seven_days)

        self.base.click_empty_space(BaseLocators)

    @allure.step(
        'Проверяем что в поле "Срок аренды" указаны введеные данные')
    def check_rental_period_field(self):
        return self.driver.find_element(
            *OrderLocators.order_form_filled_rental_period_field
        ).text == self.rental_period_text

    @allure.step('Ищем чек-бокс "чёрный жемчуг" и кликаем')
    def set_black_check_box(self):
        self.driver.find_element(*OrderLocators.black).click()

    @allure.step(
        'Ищем поле "Комментарий для курьера" в форме Заказа и заполняем его')
    def set_courier_note_field(self, courier_note):
        self.base.fill_field(
            element=OrderLocators.order_form_courier_note_field, 
            value=courier_note)
        self.base.click_empty_space(BaseLocators)

    @allure.step(
        'Проверяем отсутсвие ошибки заполнения поля "Комментарий для курьера"')
    def check_courier_note_field(self):
        return self.driver.find_elements(
            *OrderLocators.order_form_phone_field_err)

    @allure.step('Проверяем появление окна подтверждения заказа')
    def check_order_confirmation_window(self):
        return self.base.wait_for_visibility_element(
                OrderLocators.order_confirmation_window)

    @allure.step('Кликаем на кнопку "Да" в окне подтверждения заказа')
    def select_order_confirmation_window_yes_button(self):
        self.base.click_for_element(
            OrderLocators.order_confirmation_window_yes_button)

    @allure.step('Проверяем появление окна успешного заказа')
    def check_successful_order_window(self):
        return self.base.wait_for_visibility_element(
                OrderLocators.successful_order_window)

    @allure.step(
        'Кликаем на кнопку "Посмотреть статус" в окне успешного заказа')
    def select_view_status_button(self):
        self.base.click_for_element(
            OrderLocators.successful_order_window_view_status_button)

    @allure.step('Шаг по заполнению и проверке полей формы "Для кого самокат"')
    def filling_for_whom_form(self, name, surname,
                                         adress, phone):
        self.set_name_field(name)
        self.set_surname_field(surname)
        self.set_adress_field(adress)
        self.set_metro_station_field()
        self.set_phone_field(phone)

    @allure.step('Шаг по заполнению и проверке полей формы "Про аренду"')
    def filling_about_rent_form(self, when_date,
                                           courier_note):
        self.set_when_field(when_date)
        self.set_rental_period_field()
        self.set_black_check_box()
        self.set_courier_note_field(courier_note)
