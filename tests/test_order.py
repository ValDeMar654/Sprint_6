import pytest
import allure

from selenium import webdriver

from page_objects.order_page import Order
from test_data import ORDER_DATA
from urls import scooter_main_page
from locators.order_locators import OrderLocators
from page_objects.base_page import Base


class TestOrder:


    @allure.title('Проверка всего флоу позитивного сценария с двумя '
                  'наборами данных по клику по кнопке "Заказать" в хедере'
                  )
    @allure.description(
        'На главной странице в хедере ищем кнопку "Заказать" и кликаем, '
        'заполняем форму "Для кого самокат", проверяем ошибки заполнения '
        'полей. Переходим в форму "Про аренду", заполняем ее, проверяем '
        'ошибки заполнения полей. '
        'Проверяем появление окна подтверждения заказа.'
        'Проверяем появление окна успешного заказа.'
    )
    @pytest.mark.parametrize(
        'name, surname, adress, phone, when_date, courier_note',
        ORDER_DATA
    )
    def test_order_via_button_in_header(
            self, driver, name, surname, adress, phone, when_date,
            courier_note):
        order = Order(driver)

        order.select_order_button_in_header()
        order.filling_for_whom_form(name, surname,
                                         adress, phone)
        assert len(order.check_name_field()) == 0, \
            "Допущена ошибка при заполнении поля Имя"
        assert len(order.check_surname_field()) == 0, \
            "Допущена ошибка при заполнении поля Фамилия"
        assert len(order.check_adress_field()) == 0, \
            "Допущена ошибка при заполнении поля Адрес"
        assert len(order.check_phone_field()) == 0, \
            "Допущена ошибка при заполнении поля Телефон"
        
        order.select_next_button()
        order.wait_about_rent_header()
        order.filling_about_rent_form(when_date, courier_note)
        assert order.check_when_field() == when_date
        assert order.check_rental_period_field()
        assert len(order.check_courier_note_field()) == 0, \
            "Допущена ошибка при заполнении поля Комментарий для курьера"
        order.select_order_button_in_middle()
        assert order.check_order_confirmation_window(), \
            'Окно подтверждения заказа не появилось'
        order.select_order_confirmation_window_yes_button()
        assert order.check_successful_order_window(), \
            'Окно успешного заказа не появилось'
        order.select_view_status_button()
        
        
    @allure.title('Проверка всего флоу позитивного сценария с двумя '
                  'наборами данных по клику по кнопке "Заказать" в середине '
                  'страницы.'
                  )
    @allure.description(
        'Прокручиваем главную страницу до кнопки "Заказать" и кликаем, '
        'заполняем форму "Для кого самокат", проверяем ошибки заполнения '
        'полей. Переходим в форму "Про аренду", заполняем ее, проверяем '
        'ошибки заполнения полей. '
        'Проверяем появление окна подтверждения заказа.'
        'Проверяем появление окна успешного заказа.'
    )
    @pytest.mark.parametrize(
        'name, surname, adress, phone, when_date, courier_note',
        ORDER_DATA
    )
    def test_order_via_button_in_middle(
            self, driver, name, surname, adress, phone, when_date,
            courier_note):
        order = Order(driver)
        
        order.scrol_until_order_button_in_middle_located()
        order.select_order_button_in_middle()
        order.filling_for_whom_form(name, surname,
                                         adress, phone)
        assert len(order.check_name_field()) == 0, \
            "Допущена ошибка при заполнении поля Имя"
        assert len(order.check_surname_field()) == 0, \
            "Допущена ошибка при заполнении поля Фамилия"
        assert len(order.check_adress_field()) == 0, \
            "Допущена ошибка при заполнении поля Адрес"
        assert len(order.check_phone_field()) == 0, \
            "Допущена ошибка при заполнении поля Телефон"
        
        order.select_next_button()
        order.wait_about_rent_header()
        order.filling_about_rent_form(when_date, courier_note)
        assert order.check_when_field() == when_date
        assert order.check_rental_period_field()
        assert len(order.check_courier_note_field()) == 0, \
            "Допущена ошибка при заполнении поля Комментарий для курьера"
        order.select_order_button_in_middle()
        assert order.check_order_confirmation_window(), \
            'Окно подтверждения заказа не появилось'
        order.select_order_confirmation_window_yes_button()
        assert order.check_successful_order_window(), \
            'Окно успешного заказа не появилось'
        order.select_view_status_button()


