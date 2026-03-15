import time

import allure

from selenium.webdriver.support.wait import WebDriverWait
from page_objects.base_page import Base
from locators.base_locators import BaseLocators

from urls import scooter_main_page


class Transitions:


    def __init__(self, driver):
        self.driver = driver
        self.base = Base(self.driver)

    @allure.step('Кликаем на логотип Самокат')
    def select_scooter_logo(self):
        self.base.click_for_element(BaseLocators.scooter_logo)
        
    @allure.step('Кликаем на логотип Яндекс')
    def select_yandex_logo(self):
        self.base.click_for_element(BaseLocators.yandex_logo)
        
    @allure.step('Получаем уникальный идентификатор текущего активного окна')
    def get_current_window_handle(self):
        return self.driver.current_window_handle
    
    @allure.step('Переключемся на следующее окно')
    def change_window(self):
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])
        else:
            raise Exception("Страница должна была открыться в новом окне.")
        
    @allure.step('Ожидаем изменения url с about:blank')
    def wait_for_url_not_blank(self):
        WebDriverWait(self.driver, 10).until(
            lambda d: d.current_url != "about:blank")
    
    @allure.step('Шаг Клик по логотипу Яндекс и переход на второе окно')
    def yandex_logo_transition(self):
        self.select_yandex_logo()
        self.change_window()
        self.wait_for_url_not_blank()
        