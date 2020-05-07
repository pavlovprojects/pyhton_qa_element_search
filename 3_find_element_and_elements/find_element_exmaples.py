from locators import MainPage
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="drivers/chromedriver")
driver.get("https://demo.opencart.com/")
elements = driver.find_elements_by_css_selector(MainPage.NAV_LINKS)
# element = driver.find_element_by_css_selector(MainPage.NAV_LINKS)
# elements = driver.find_elements(By.CSS_SELECTOR, MainPage.NAV_LINKS)
driver.quit()
