# Sprint_6

# Задача

### [x] Выпадающий список в разделе «Вопросы о важном»
    - [x] Нужно проверить: когда нажимаешь на стрелочку, открывается соответствующий текст.
    - [x] Нужно написать отдельный тест на каждый вопрос.

### [x] Заказ самоката
    - [x] Нужно проверить весь флоу позитивного сценария с двумя наборами данных.
    - [x] Нужно проверить две точки входа в сценарий - «Заказать» вверху страницы и внизую


# Реализация
## Оглавление
- [conftest](#conftest)
- [order_locators](#order_locators)
- [questions_about_metters_locators](#questions_about_metters_locators)
- [order_page](#order_page)
- [questions_about_metters_page](#questions_about_metters_page)
- [test_order](#test_order)
- [test_questions_about_metters](#test_lquestions_about_metters)
- [test_data](#test_data)
- [urls](#urls)
- [requirements](#requirements)
- [allure_results](#allure_results)

## conftest
Файл содержит 2 класса локаторов

## order_locators
В файле собраны различные локаторы для проверки всего флоу заказа самоката

## questions_about_metters_locators
В файле собраны различные локаторы для проверки раздела «Вопросы о важном»

## order_page
Файл содержит класс Order, в который вынесены локаторы order_locators и действия с этими локаторами.
Действия с локаторами собраны в шаги:
Шаг по заполнению и проверке полей формы "Для кого самокат"
```
def filling_and_checks_for_whom_form
```

Шаг по заполнению и проверке полей формы "Про аренду"
```
def filling_and_checks_about_rent_form
```

Весь флоу позитивного сценария
```
def whole_order_flow
```

## questions_about_metters_page
Файл содержит класс TestQuestionsAboutMetters, в который вынесены локаторы 
questions_about_metters_locators и действия с этими локаторами.
Действия с локаторами собраны в шаг:
Шаг проверки выпадающего списка в разделе "Вопросы о важном"
```
def check_question
```

## test_order
Файл содержит параметризированные тесты:
```
def test_order_via_button_in_header
```
который проверяет весь флоу позитивного сценария с двумя 
наборами данных по клику по кнопке "Заказать" в хедере
и
```
def test_order_via_button_in_header
```
который проверяет весь флоу позитивного сценария с двумя 
наборами данных по клику по кнопке "Заказать" в середине страницы

## test_questions_about_metters
Файл содержит тесты:
```
def test_check_question_1
def test_check_question_2
def test_check_question_3
def test_check_question_4
def test_check_question_5
def test_check_question_6
def test_check_question_7
def test_check_question_8
```
которые проверяют клик по вопросу и появление ответа.
По заданию, на каждый вопрос должен быть написан отдельный тест. 

## test_data
Файл содержит 2 два набора тестовых данных, которые используются в параметризированных тестах.


## urls
Файл для хранения url страниц.
В данный моммент файл содержит url только главной страницы Самоката

## requirements
Файл содержит внешние зависимости.
Команда для установки зависимостей:
```
pip install -r requirements.txt
```
или
```
pip3 install -r requirements.txt
```

## allure_results
Директория allure_results содержит сгенерированный Allure-отчёт.
Для формирования отчёта в формате веб-страницы выполните команду:
```
allure serve allure_results
```
