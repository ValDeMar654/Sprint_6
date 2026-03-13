import pytest
import allure

from selenium import webdriver

from page_objects.order_page import Order
from test_data import ORDER_DATA
from urls import scooter_main_page


class TestOrder:

    @allure.title('Cоздаем драйвер для браузера Firefox')
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    @allure.title('Проверка всего флоу позитивного сценария с двумя '
                  'наборами данных по клику по кнопке "Заказать" в хедере'
                  )
    @allure.description(
        'На главной странице в хедере ищем кнопку "Заказать" и кликаем, '
        'заполняем форму "Для кого самокат", переходим в форму "Про аренду" '
        'и заполняем ее. '
        'Проверяем появление всплывающего окна с сообщением '
        'об успешном создании заказа. '
        'Проверяем переход по клику на логотип Самокат. '
        'Проверяем переход по клику на логитип Яндекс.'
    )
    @pytest.mark.parametrize(
        'name, surname, adress, phone, when_date, courier_note',
        ORDER_DATA
    )
    def test_order_via_button_in_header(
            self, order_locators, name, surname, adress, phone, when_date,
            courier_note):
        self.driver.get(scooter_main_page)
        self.order = Order(self.driver)

        self.order.select_order_button_in_header(order_locators)
        self.order.whole_order_flow(order_locators,
                                    name, surname, adress, phone, when_date,
                                    courier_note)

    @allure.title('Проверка всего флоу позитивного сценария с двумя '
                  'наборами данных по клику по кнопке "Заказать" в середине '
                  'страницы.'
                  )
    @allure.description(
        'Прокручиваем главную страницу до кнопки "Заказать" и кликаем, '
        'заполняем форму "Для кого самокат", переходим в форму "Про аренду" '
        'и заполняем ее. '
        'Проверяем появление всплывающего окна с сообщением '
        'об успешном создании заказа. '
        'Проверяем переход по клику на логотип Самокат. '
        'Проверяем переход по клику на логитип Яндекс.'
    )
    @pytest.mark.parametrize(
        'name, surname, adress, phone, when_date, courier_note',
        ORDER_DATA
    )
    def test_order_via_button_in_middle(
            self, order_locators, name, surname, adress, phone, when_date,
            courier_note):
        self.driver.get(scooter_main_page)
        self.order = Order(self.driver)

        self.order.select_order_button_in_middle(order_locators)
        self.order.whole_order_flow(order_locators,
                                    name, surname, adress, phone, when_date,
                                    courier_note)

    @allure.title('Закрываем браузер')
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
