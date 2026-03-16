import pytest
import allure

from selenium import webdriver

from page_objects.order_page import Order
from test_data import ORDER_DATA


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
        order.whole_order_flow(
            name, surname, adress, phone, when_date, courier_note
            )
        assert order.wait_successful_order_window(), \
            'Окно успешного заказа не появилось'        
        
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
        order.whole_order_flow(
            name, surname, adress, phone, when_date, courier_note
            )
        assert order.wait_successful_order_window(), \
            'Окно успешного заказа не появилось'        
