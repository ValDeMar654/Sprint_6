import allure

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_locators import BaseLocators


class Base:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем когда элемент станет видимым')
    def wait_for_visibility_element(self, element):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(
                element))

    @allure.step('Ждем когда элемент станет невидим')
    def wait_for_invisibility_element(self, element):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.invisibility_of_element_located(
                element))

    @allure.step('Ждем когда элемент появится в DOM')
    def wait_for_element_load_in_dom(self, element):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.presence_of_element_located(
                element))

    @allure.step('Ждем когда элемент станет кликабелен')
    def wait_for_element_clickable(self, element):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(
                element))

    @allure.step('Ждем когда элемент станет кликабелен и кликаем')
    def click_for_element(self, element):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(
                element)).click()

    @allure.step('Скролл страницы до нужного элемента')
    def scrol_until_element_located(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", 
            self.wait_for_element_load_in_dom(element)) 

    @allure.step('Ищем и заполняем поле')  
    def fill_field(self, element, value):
        self.driver.find_element(*element).send_keys(value)    

    @allure.step('Клик по пусому месту') 
    def click_empty_space(self):
        return ActionChains(self.driver).move_to_element_with_offset(
            self.driver.find_element(
                *BaseLocators.empty_space
            ), 2, 300).click().perform()
        
    @allure.step('Переключаемся на следующее окно')
    def change_window(self):
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])
        else:
            raise Exception("Страница должна была открыться в новом окне.")

    @allure.step('Ожидаем изменения url с about:blank')
    def wait_for_url_not_blank(self):
        WebDriverWait(self.driver, 10).until(
            lambda d: d.current_url != "about:blank")
    
    @allure.step('Получаем уникальный идентификатор текущего активного окна')
    def get_current_window_handle(self):
        return self.current_window_handle
    
    @allure.step('Получаем url')
    def get_current_url(self):
        return self.driver.current_url