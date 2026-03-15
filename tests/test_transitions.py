import allure
import pytest

from urls import scooter_main_page
from page_objects.transitions_page import Transitions


class TestTransitions:

    @allure.title('Проверяем что по клику на логотип Яндекс осуществляется '
                 'переход на главную страницу Дзен в новом окне'
                  )
    @allure.description('Кликаем на логотип Яндекс, переходим на новую '
                        'страницу и проверяем url.'
                        )  
    def test_transition_yandex_logo(
            self, driver):
        transition = Transitions(driver)
        transition.yandex_logo_transition()
        assert "dzen" in driver.current_url
     
    @allure.title('Проверка перехода на главную страницу Самоката '
                  'по клику на логотип Самокат.'
                  )
    @allure.description('Кликаем на логотип Самоката, проверяем url.'
                        )    
    def test_transition_scooter_logo(
            self, driver):
        transition = Transitions(driver)
        transition.select_scooter_logo()
        assert driver.current_url == scooter_main_page
