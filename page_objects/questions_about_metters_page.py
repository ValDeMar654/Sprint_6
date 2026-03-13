import time

import allure

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class QuestionsSection:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем появления заголовка "Самокат"')
    def wait_for_load_header(self, faq_locators):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(
                faq_locators.scooter_header
            )
        )

    @allure.step('Скролл страницы до нужного элемента')
    def scrol_until_element_located(self, question_locator):
        question = WebDriverWait(self.driver, 3).until(
            expected_conditions.presence_of_element_located(
                question_locator))

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", question)

    @allure.step('Клик по вопросу')
    def select_question(self, question_locator):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(
                question_locator)).click()

    @allure.step('Проверяем виден соответствующий текст ответа')
    def check_answer_text(self, answer_locator):
        assert WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(answer_locator))

    @allure.step(
        'Шаг проверки выпадающего списка в разделе "Вопросы о важном"')
    def check_question(self, faq_locators, question_locator, answer_locator):
        self.wait_for_load_header(faq_locators)
        time.sleep(2)
        self.scrol_until_element_located(question_locator)
        self.select_question(question_locator)
        self.check_answer_text(answer_locator)
        self.driver.delete_all_cookies()
