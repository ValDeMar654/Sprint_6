from selenium.webdriver.common.by import By


class FaqLocators:

    # Вопрос "Сколько это стоит? И как оплатить?"
    questions_about_metters_question_1 = (
        By.XPATH, '//div[@id="accordion__heading-0"]')

    # Ответ на вопрос "Сколько это стоит? И как оплатить?"
    questions_about_metters_question_1_answer = (
        By.XPATH, '//div[@id="accordion__panel-0"]/p')

    # Вопрос "Хочу сразу несколько самокатов! Так можно?"
    questions_about_metters_question_2 = (
        By.XPATH, '//div[@id="accordion__heading-1"]')

    # Ответ на вопрос "Хочу сразу несколько самокатов! Так можно?"
    questions_about_metters_question_2_answer = (
        By.XPATH, '//div[@id="accordion__panel-1"]/p')

    # Вопрос "Как рассчитывается время аренды?"
    questions_about_metters_question_3 = (
        By.XPATH, '//div[@id="accordion__heading-2"]')

    # Ответ на вопрос "Как рассчитывается время аренды?"
    questions_about_metters_question_3_answer = (
        By.XPATH, '//div[@id="accordion__panel-2"]/p')

    # Вопрос "Можно ли заказать самокат прямо на сегодня?"
    questions_about_metters_question_4 = (
        By.XPATH, '//div[@id="accordion__heading-3"]')

    # Ответ на вопрос "Можно ли заказать самокат прямо на сегодня?"
    questions_about_metters_question_4_answer = (
        By.XPATH, '//div[@id="accordion__panel-3"]/p')

    # Вопрос "Можно ли продлить заказ или вернуть самокат раньше?"
    questions_about_metters_question_5 = (
        By.XPATH, '//div[@id="accordion__heading-4"]')

    # Ответ на вопрос "Можно ли продлить заказ или вернуть самокат раньше?"
    questions_about_metters_question_5_answer = (
        By.XPATH, '//div[@id="accordion__panel-4"]/p')

    # Вопрос "Вы привозите зарядку вместе с самокатом?"
    questions_about_metters_question_6 = (
        By.XPATH, '//div[@id="accordion__heading-5"]')

    # Ответ на вопрос "Вы привозите зарядку вместе с самокатом?"
    questions_about_metters_question_6_answer = (
        By.XPATH, '//div[@id="accordion__panel-5"]/p')

    # Вопрос "Можно ли отменить заказ?"
    questions_about_metters_question_7 = (
        By.XPATH, '//div[@id="accordion__heading-6"]')

    # Ответ на вопрос "Можно ли отменить заказ?"
    questions_about_metters_question_7_answer = (
        By.XPATH, '//div[@id="accordion__panel-6"]/p')

    # Вопрос "Я жизу за МКАДом, привезёте?"
    questions_about_metters_question_8 = (
        By.XPATH, '//div[@id="accordion__heading-7"]')

    # Ответ на вопрос "Я жизу за МКАДом, привезёте?"
    questions_about_metters_question_8_answer = (
        By.XPATH, '//div[@id="accordion__panel-7"]/p')
