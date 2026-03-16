import allure

from selenium.webdriver.common.keys import Keys

from locators.base_locators import BaseLocators
from locators.order_locators import OrderLocators
from page_objects.base_page import Base


class Order(Base):

    rental_period_text = None

    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step('Кликаем на кнопку "Заказать" в хедере')
    def select_order_button_in_header(self):
        self.click_for_element(BaseLocators.order_button_in_header)

    @allure.step('Скролл страницы до кнопки "Заказать" в середине страницы')
    def scrol_until_order_button_in_middle_located(self):
        self.scrol_until_element_located(BaseLocators.order_button_in_middle)

    @allure.step('Клик по кнопке "Заказать" в середине страницы')
    def select_order_button_in_middle(self):
        self.click_for_element(BaseLocators.order_button_in_middle)

    @allure.step('Ищем поле "Имя" в форме Заказа и заполняем его')
    def set_name_field(self, name):
        self.fill_field(element=OrderLocators.order_form_name_field, value=name)
            
    @allure.step('Ищем поле "Фамилия" в форме Заказа и заполняем его')
    def set_surname_field(self, surname):
        self.fill_field(element=OrderLocators.order_form_surname_field, value=surname)
        
    @allure.step('Ищем поле "Адрес" в форме Заказа и заполняем его')
    def set_adress_field(self, adress):
        self.fill_field(element=OrderLocators.order_form_adress_field, value=adress)

    @allure.step('Ищем поле "Станция метро" в форме Заказа и выбираем станцию')
    def set_metro_station_field(self):
        self.click_for_element(OrderLocators.order_form_metro_station_field)
        self.scrol_until_element_located(OrderLocators.fili_station)
        self.click_for_element(OrderLocators.fili_station)
        
    @allure.step('Ищем поле "Телефон" в форме Заказа и заполняем его')
    def set_phone_field(self, phone):
        self.fill_field(element=OrderLocators.order_form_phone_field, value=phone)

    @allure.step('Ищем кнопку "Далее" и кликаем')
    def select_next_button(self):
        self.click_for_element(OrderLocators.next_button_in_order_form)

    @allure.step('Ждём кода появится форма с заголовком "Про аренду"')
    def wait_about_rent_header(self):
        self.wait_for_visibility_element(OrderLocators.about_rent_header)

    @allure.step(
        'Ищем поле "Когда привезти самокат" в форме Заказа и заполняем его')
    def set_when_field(self, when_date):
        self.fill_field(
            element = OrderLocators.order_form_when_field, value = when_date)
        self.fill_field(
            element = OrderLocators.order_form_when_field, value = Keys.ENTER)

    @allure.step('Ищем поле "Срок аренды" в форме Заказа и кликаем')
    def set_rental_period_field(self):
        self.click_for_element(
            OrderLocators.order_form_rental_period_field)
        self.rental_period_text = self.wait_for_element_load_in_dom(
            OrderLocators.seven_days).text
        self.scrol_until_element_located(OrderLocators.seven_days)
        self.click_for_element(OrderLocators.seven_days)

    @allure.step('Ищем чек-бокс "чёрный жемчуг" и кликаем')
    def set_black_check_box(self):
        self.click_for_element(OrderLocators.black)

    @allure.step(
        'Ищем поле "Комментарий для курьера" в форме Заказа и заполняем его')
    def set_courier_note_field(self, courier_note):
        self.fill_field(
            element=OrderLocators.order_form_courier_note_field, 
            value=courier_note)

    @allure.step('Ждем появление окна подтверждения заказа')
    def wait_order_confirmation_window(self):
        self.wait_for_visibility_element(
              OrderLocators.order_confirmation_window)

    @allure.step('Кликаем на кнопку "Да" в окне подтверждения заказа')
    def select_order_confirmation_window_yes_button(self):
        self.click_for_element(
            OrderLocators.order_confirmation_window_yes_button)

    @allure.step('Ждум появление окна успешного заказа')
    def wait_successful_order_window(self):
        return self.wait_for_visibility_element(
                OrderLocators.successful_order_window)

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
        
    @allure.step('Весь флоу позитивного сценария')
    def whole_order_flow(
            self, name, surname, adress, phone, when_date, courier_note):
        self.filling_for_whom_form(name, surname, adress, phone)
        self.select_next_button()
        self.wait_about_rent_header()
        self.filling_about_rent_form(when_date, courier_note)
        self.select_order_button_in_middle()
        self.wait_order_confirmation_window()
        self.select_order_confirmation_window_yes_button()
        self.wait_successful_order_window()
