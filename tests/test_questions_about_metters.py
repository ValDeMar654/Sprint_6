import allure

from selenium import webdriver

from page_objects.questions_about_metters_page import QuestionsSection
from locators.questions_about_metters_locators import FaqLocators
from urls import scooter_main_page


class TestQuestionsAboutMetters:

    @allure.title('Проверка вопроса '
                  '"Сколько это стоит? И как оплатить?" '
                  'в разделе Вопросы о важном.'
                  )
    @allure.description('Скролим страницу пока не будет виден вопрос,'
                        'кликаем на вопрос, и проверяем, что ответ виден.'
                        )
    def test_check_question_1(self, driver):
        questions_section = QuestionsSection(driver)
        question_locator = FaqLocators.questions_about_metters_question_1
        answer_locator = FaqLocators.questions_about_metters_question_1_answer
        questions_section.check_question(question_locator, answer_locator)
        assert questions_section.check_answer_text(answer_locator), "Текст ответа не обнаружен"
        
    @allure.title('Проверка вопроса '
                  '"Хочу сразу несколько самокатов! Так можно?" '
                  'в разделе Вопросы о важном.'
                  )
    @allure.description('Скролим страницу пока не будет виден вопрос,'
                        'кликаем на вопрос, и проверяем, что ответ виден.'
                        )
    def test_check_question_2(self, driver):
        questions_section = QuestionsSection(driver)
        question_locator = FaqLocators.questions_about_metters_question_2
        answer_locator = FaqLocators.questions_about_metters_question_2_answer
        questions_section.check_question(question_locator, answer_locator)
        assert questions_section.check_answer_text(answer_locator), "Текст ответа не обнаружен"

    @allure.title('Проверка вопроса '
                  '"Как рассчитывается время аренды?" '
                  'в разделе Вопросы о важном.'
                  )
    @allure.description('Скролим страницу пока не будет виден вопрос,'
                        'кликаем на вопрос, и проверяем, что ответ виден.'
                        )
    def test_check_question_3(self, driver):
        questions_section = QuestionsSection(driver)
        question_locator = FaqLocators.questions_about_metters_question_3
        answer_locator = FaqLocators.questions_about_metters_question_3_answer
        questions_section.check_question(question_locator, answer_locator)
        assert questions_section.check_answer_text(answer_locator), "Текст ответа не обнаружен"

    @allure.title('Проверка вопроса '
                  '"Можно ли заказать самокат прямо на сегодня?" '
                  'в разделе Вопросы о важном.'
                  )
    @allure.description('Скролим страницу пока не будет виден вопрос,'
                        'кликаем на вопрос, и проверяем, что ответ виден.'
                        )
    def test_check_question_4(self, driver):
        questions_section = QuestionsSection(driver)
        question_locator = FaqLocators.questions_about_metters_question_4
        answer_locator = FaqLocators.questions_about_metters_question_4_answer
        questions_section.check_question(question_locator, answer_locator)
        assert questions_section.check_answer_text(answer_locator), "Текст ответа не обнаружен"

    @allure.title('Проверка вопроса '
                  '"Можно ли продлить заказ или вернуть самокат раньше?" '
                  'в разделе Вопросы о важном.'
                  )
    @allure.description('Скролим страницу пока не будет виден вопрос,'
                        'кликаем на вопрос, и проверяем, что ответ виден.'
                        )
    def test_check_question_5(self, driver):
        questions_section = QuestionsSection(driver)
        question_locator = FaqLocators.questions_about_metters_question_5
        answer_locator = FaqLocators.questions_about_metters_question_5_answer
        questions_section.check_question(question_locator, answer_locator)
        assert questions_section.check_answer_text(answer_locator), "Текст ответа не обнаружен"

    @allure.title('Проверка вопроса '
                  '"Вы привозите зарядку вместе с самокатом?" '
                  'в разделе Вопросы о важном.'
                  )
    @allure.description('Скролим страницу пока не будет виден вопрос,'
                        'кликаем на вопрос, и проверяем, что ответ виден.'
                        )
    def test_check_question_6(self, driver):
        questions_section = QuestionsSection(driver)
        question_locator = FaqLocators.questions_about_metters_question_6
        answer_locator = FaqLocators.questions_about_metters_question_6_answer
        questions_section.check_question(question_locator, answer_locator)
        assert questions_section.check_answer_text(answer_locator), "Текст ответа не обнаружен"

    @allure.title('Проверка вопроса '
                  '"Можно ли отменить заказ?" '
                  'в разделе Вопросы о важном.'
                  )
    @allure.description('Скролим страницу пока не будет виден вопрос,'
                        'кликаем на вопрос, и проверяем, что ответ виден.'
                        )
    def test_check_question_7(self, driver):
        questions_section = QuestionsSection(driver)
        question_locator = FaqLocators.questions_about_metters_question_7
        answer_locator = FaqLocators.questions_about_metters_question_7_answer
        questions_section.check_question(question_locator, answer_locator)
        assert questions_section.check_answer_text(answer_locator), "Текст ответа не обнаружен"

    @allure.title('Проверка вопроса '
                  '"Я жизу за МКАДом, привезёте?" '
                  'в разделе Вопросы о важном.'
                  )
    @allure.description('Скролим страницу пока не будет виден вопрос,'
                        'кликаем на вопрос, и проверяем, что ответ виден.'
                        )
    def test_check_question_8(self, driver):
        questions_section = QuestionsSection(driver)
        question_locator = FaqLocators.questions_about_metters_question_8
        answer_locator = FaqLocators.questions_about_metters_question_8_answer
        questions_section.check_question(question_locator, answer_locator)
        assert questions_section.check_answer_text(answer_locator), "Текст ответа не обнаружен"
