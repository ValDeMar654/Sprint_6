import pytest
from locators.order_locators import OrderLocators
from locators.questions_about_metters_locators import FaqLocators


@pytest.fixture(scope="function")
def order_locators():
    order_locators = OrderLocators()
    return order_locators


@pytest.fixture(scope="function")
def faq_locators():
    faq_locators = FaqLocators()
    return faq_locators
