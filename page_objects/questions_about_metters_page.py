import allure

from page_objects.base_page import Base
from locators.base_locators import BaseLocators

class QuestionsSection(Base):

    def __init__(self, driver):
        super().__init__(driver)
        
    @allure.step('Ждем появления заголовка "Самокат"')
    def wait_for_load_header(self):
        self.wait_for_visibility_element(BaseLocators.scooter_header)

    @allure.step('Скролл страницы до нужного вопроса')
    def scrol_until_question_located(self, question_locator):
        self.scrol_until_element_located(question_locator)

    @allure.step('Клик по вопросу')
    def select_question(self, question_locator):
        self.click_for_element(question_locator)
        
    @allure.step('Проверяем виден соответствующий текст ответа')
    def check_answer_text(self, answer_locator):
        return self.wait_for_visibility_element(answer_locator)
        
    @allure.step(
        'Шаг проверки выпадающего списка в разделе "Вопросы о важном"')
    def check_question(self, question_locator, answer_locator):
        self.wait_for_load_header()
        self.scrol_until_question_located(question_locator)
        self.select_question(question_locator)

