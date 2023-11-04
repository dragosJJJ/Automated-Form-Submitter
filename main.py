from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

FIRST_NAME = "Dragos"
LAST_NAME = "Juganariu"
MAIL = "random_email@yahoo.com"

chrome_settings = webdriver.ChromeOptions()
chrome_settings.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_settings)
driver.get("https://secure-retreat-92358.herokuapp.com/")

wait = WebDriverWait(driver, 10)
first_name_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".form-control.top")))
last_name_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".form-control.middle")))
email_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".form-control.bottom")))

first_name_input.send_keys(FIRST_NAME)
last_name_input.send_keys(LAST_NAME)
email_input.send_keys(MAIL, Keys.ENTER)

