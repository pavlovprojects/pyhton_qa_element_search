import pytest
import os

from selenium import webdriver


def driver_factory(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="drivers/chromedriver")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path="drivers/geckodriver")
    elif browser == "yandex":
        driver = webdriver.Chrome(executable_path="drivers/yandexdriver")
    elif browser == "opera":
        driver = webdriver.Opera(executable_path="drivers/operadriver")
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise Exception("Driver not supported")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="https://demo.opencart.com/", help="choose your browser")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    driver = driver_factory(browser)
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.addfinalizer(driver.close)
    driver.get(url)
    return driver


@pytest.fixture(params=["chrome", "firefox", "opera"])
def parametrize_browser(request):
    driver = driver_factory(request.param)
    driver.implicitly_wait(5)
    request.addfinalizer(driver.quit)
    driver.get(request.config.getoption("--url"))
    return driver
