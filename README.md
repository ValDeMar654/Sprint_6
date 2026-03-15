# Sprint_6
```
По результатам 1 ревью:
- conftest теперь содержит только стартовую фикстуру
- добавлен файл base_locators в который перенесены различные локаторы, используемые в различных PO
- добавлен файл base_page который содержит локаторы base_locators и базовые методы используемые в различных PO.
- добавлен файл transitions_page который использует локаторы BaseLocators и действия с этими локаторами для тестов переходов по логотипам.
- добавлен файл test_transitions в котором проверяются переходы по кликам на логотип Яндекс и логотип Самокат
- из всех тестов удалена функция time.sleep()
- Ассерты перенесены из РО в тесты
- обновлены внешние зависимости
- Сгенерирован новый Allure-отчёт
```

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
- [base_locators](#base_locators)
- [order_locators](#order_locators)
- [questions_about_metters_locators](#questions_about_metters_locators)
- [base_page](#base_page)
- [order_page](#order_page)
- [questions_about_metters_page](#questions_about_metters_page)
- [transitions_page](#transitions_page)
- [test_order](#test_order)
- [test_questions_about_metters](#test_lquestions_about_metters)
- [test_transitions](#test_transitions)
- [test_data](#test_data)
- [urls](#urls)
- [requirements](#requirements)
- [allure_results](#allure_results)

## conftest
Файл содержит стартовую фикстуру 

## base_locators
В файле собраны различные локаторы, используемые в различных PO

## order_locators
В файле собраны различные локаторы для проверки всего флоу заказа самоката

## questions_about_metters_locators
В файле собраны различные локаторы для проверки раздела «Вопросы о важном»

## base_page
Файл содержит класс Base, который содержит локаторы base_locators и 
базовые методы используемые в различных PO.

## order_page
Файл содержит класс Order, который содержит локаторы order_locators и действия с этими локаторами.
Действия с локаторами собраны в шаги:
Шаг по заполнению полей формы "Для кого самокат"
```
def filling_for_whom_form
```

Шаг по заполнению полей формы "Про аренду"
```
def filling_about_rent_form
```

## questions_about_metters_page
Файл содержит класс TestQuestionsAboutMetters, в который вынесены локаторы 
questions_about_metters_locators и действия с этими локаторами.
Действия с локаторами собраны в шаг:
Шаг проверки выпадающего списка в разделе "Вопросы о важном"
```
def check_question
```

## transitions_page
Файл содержит класс Transitions, который использует локаторы BaseLocators
и действия с этими локаторами для тестов переходов по логотипам.

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

## test_transitions
Файл содержит тесты:
```
def test_transition_yandex_logo
def test_transition_scooter_logo
```
Которые проверяют что по клику на логотип Яндекс осуществляется
переход на главную страницу Дзен в новом окне, а клик на логотип
Самокат ведет на главную страницу Самоката.

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
