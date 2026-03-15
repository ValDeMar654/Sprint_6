import allure

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from urls import scooter_main_page


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
    def click_empty_space(self, base_locators):
        return ActionChains(self.driver).move_to_element_with_offset(
            self.driver.find_element(
                *base_locators.empty_space
            ), 2, 300).click().perform()

    @allure.step('Ждем появления кнопки "Заказать" в хедере')
    def wait_for_load_header(self, base_locators):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(
                base_locators.order_button_in_header
            )
        ) 

    @allure.step('Кликаем на кнопку "Заказать" в хедере')
    def select_order_button_in_header(self, base_locators):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(
                base_locators.order_button_in_header
            )).click()   

    @allure.step('Кликаем на логотип Яндекс')
    def select_yandex_logo(self, base_locators):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(
                base_locators.yandex_logo)).click()

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

    @allure.step('# Кликаем на логотип Самокат')
    def select_scooter_logo(self, base_locators):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(
                base_locators.scooter_logo)).click()
        time.sleep(2)

    @allure.step('Проверяем что по клику на логотип Самокат осуществляется '
                 'переход на главную страницу «Самоката»')
    def check_scooter_logo_transition(self):
        assert (
            self.driver.current_url == scooter_main_page
        )
