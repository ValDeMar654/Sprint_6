import allure

from selenium.webdriver.support.wait import WebDriverWait
from page_objects.base_page import Base
from locators.base_locators import BaseLocators


class Transitions(Base):


    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step('Кликаем на логотип Самокат')
    def select_scooter_logo(self):
        self.click_for_element(BaseLocators.scooter_logo)
        
    @allure.step('Кликаем на логотип Яндекс')
    def select_yandex_logo(self):
        self.click_for_element(BaseLocators.yandex_logo)
        
    @allure.step('Получаем уникальный идентификатор текущего активного окна')
    def get_current_window_handle(self):
        return self.current_window_handle
    
    @allure.step('Шаг Клик по логотипу Яндекс и переход на второе окно')
    def yandex_logo_transition(self):
        self.select_yandex_logo()
        self.change_window()
        self.wait_for_url_not_blank()
    
   
        