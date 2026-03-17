import pytest
import allure

from page_objects.questions_about_metters_page import QuestionsSection
from locators.questions_about_metters_locators import FaqLocators
from test_data import QUESTION_ANSWER

class TestQuestionsAboutMetters:

    @allure.title('Проверка вопроса '
                  '"Сколько это стоит? И как оплатить?" '
                  'в разделе Вопросы о важном.'
                  )
    @allure.description('Скролим страницу пока не будет виден вопрос,'
                        'кликаем на вопрос, и проверяем, что ответ виден.'
                        )
    @pytest.mark.parametrize(
        'question_locator, answer_locator',
        QUESTION_ANSWER
    )
    def test_check_question(self, driver, question_locator, answer_locator):
        questions_section = QuestionsSection(driver)
        questions_section.check_question(question_locator, answer_locator)
        assert questions_section.check_answer_text(answer_locator), "Текст ответа не обнаружен"
     