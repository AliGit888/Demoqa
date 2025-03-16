import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    webdriver.Chrome()
    yield driver
    driver.quit()