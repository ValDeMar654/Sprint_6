from selenium import webdriver

import allure

from page_objects.questions_about_metters_page import QuestionsSection
from urls import scooter_main_page


class TestQuestionsAboutMetters:

    @allure.title('Cоздаем драйвер для браузера Firefox')
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    @allure.title('Проверка вопроса '
                  '"Сколько это стоит? И как оплатить?" '
                  'в разделе Вопросы о важном.'
                  )
    @allure.description('Скролим страницу пока не будет виден вопрос,'
                        'кликаем на вопрос, и проверяем, что ответ виден.'
                        )
    def test_check_question_1(self, faq_locators):

        self.driver.get(scooter_main_page)
        self.questions_section = QuestionsSection(self.driver)
        question_locator = faq_locators.questions_about_metters_question_1
        answer_locator = faq_locators.questions_about_metters_question_1_answer
        self.questions_section.check_question(
            faq_locators, question_locator, answer_locator)

    @allure.title('Проверка вопроса '
                  '"Хочу сразу несколько самокатов! Так можно?" '
                  'в разделе Вопросы о важном.'
                  )
    @allure.description('Скролим страницу пока не будет виден вопрос,'
                        'кликаем на вопрос, и проверяем, что ответ виден.'
                        )
    def test_check_question_2(self, faq_locators):

        self.driver.get(scooter_main_page)
        self.questions_section = QuestionsSection(self.driver)
        question_locator = faq_locators.questions_about_metters_question_2
        answer_locator = faq_locators.questions_about_metters_question_2_answer
        self.questions_section.check_question(
            faq_locators, question_locator, answer_locator)

    @allure.title('Проверка вопроса '
                  '"Как рассчитывается время аренды?" '
                  'в разделе Вопросы о важном.'
                  )
    @allure.description('Скролим страницу пока не будет виден вопрос,'
                        'кликаем на вопрос, и проверяем, что ответ виден.'
                        )
    def test_check_question_3(self, faq_locators):

        self.driver.get(scooter_main_page)
        self.questions_section = QuestionsSection(self.driver)
        question_locator = faq_locators.questions_about_metters_question_3
        answer_locator = faq_locators.questions_about_metters_question_3_answer
        self.questions_section.check_question(
            faq_locators, question_locator, answer_locator)

    @allure.title('Проверка вопроса '
                  '"Можно ли заказать самокат прямо на сегодня?" '
                  'в разделе Вопросы о важном.'
                  )
    @allure.description('Скролим страницу пока не будет виден вопрос,'
                        'кликаем на вопрос, и проверяем, что ответ виден.'
                        )
    def test_check_question_4(self, faq_locators):

        self.driver.get(scooter_main_page)
        self.questions_section = QuestionsSection(self.driver)
        question_locator = faq_locators.questions_about_metters_question_4
        answer_locator = faq_locators.questions_about_metters_question_4_answer
        self.questions_section.check_question(
            faq_locators, question_locator, answer_locator)

    @allure.title('Проверка вопроса '
                  '"Можно ли продлить заказ или вернуть самокат раньше?" '
                  'в разделе Вопросы о важном.'
                  )
    @allure.description('Скролим страницу пока не будет виден вопрос,'
                        'кликаем на вопрос, и проверяем, что ответ виден.'
                        )
    def test_check_question_5(self, faq_locators):

        self.driver.get(scooter_main_page)
        self.questions_section = QuestionsSection(self.driver)
        question_locator = faq_locators.questions_about_metters_question_5
        answer_locator = faq_locators.questions_about_metters_question_5_answer
        self.questions_section.check_question(
            faq_locators, question_locator, answer_locator)

    @allure.title('Проверка вопроса '
                  '"Вы привозите зарядку вместе с самокатом?" '
                  'в разделе Вопросы о важном.'
                  )
    @allure.description('Скролим страницу пока не будет виден вопрос,'
                        'кликаем на вопрос, и проверяем, что ответ виден.'
                        )
    def test_check_question_6(self, faq_locators):

        self.driver.get(scooter_main_page)
        self.questions_section = QuestionsSection(self.driver)
        question_locator = faq_locators.questions_about_metters_question_6
        answer_locator = faq_locators.questions_about_metters_question_6_answer
        self.questions_section.check_question(
            faq_locators, question_locator, answer_locator)

    @allure.title('Проверка вопроса '
                  '"Можно ли отменить заказ?" '
                  'в разделе Вопросы о важном.'
                  )
    @allure.description('Скролим страницу пока не будет виден вопрос,'
                        'кликаем на вопрос, и проверяем, что ответ виден.'
                        )
    def test_check_question_7(self, faq_locators):

        self.driver.get(scooter_main_page)
        self.questions_section = QuestionsSection(self.driver)
        question_locator = faq_locators.questions_about_metters_question_7
        answer_locator = faq_locators.questions_about_metters_question_7_answer
        self.questions_section.check_question(
            faq_locators, question_locator, answer_locator)

    @allure.title('Проверка вопроса '
                  '"Я жизу за МКАДом, привезёте?" '
                  'в разделе Вопросы о важном.'
                  )
    @allure.description('Скролим страницу пока не будет виден вопрос,'
                        'кликаем на вопрос, и проверяем, что ответ виден.'
                        )
    def test_check_question_8(self, faq_locators):

        self.driver.get(scooter_main_page)
        self.questions_section = QuestionsSection(self.driver)
        question_locator = faq_locators.questions_about_metters_question_8
        answer_locator = faq_locators.questions_about_metters_question_8_answer
        self.questions_section.check_question(
            faq_locators, question_locator, answer_locator)

    @allure.title('Закрываем браузер')
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
