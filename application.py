import random
import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options


from selenium.webdriver.common.by import By


from app_constants import UI_TEST_URL, PASSWORD, TEST_URL


class Application:

    def __init__(self):
        options = Options()
        options.add_argument("--start-maximized")
        self.wd = WebDriver(options=options)
        self.wd.implicitly_wait(10)

    def open_home_page(self):
        wd = self.wd
        wd.get(UI_TEST_URL)

    def check_register_page(self):
        wd = self.wd
        wd.find_element(By.ID, value='pv_id_2_header')

    def fill_register_form(self):
        wd = self.wd
        wd.find_element(By.ID, value='login').click()
        wd.find_element(By.ID, value='login').send_keys(f'holy_test_ui_login{random.randint(1000, 10000)}@ddd.ru')
        wd.find_element(By.ID, value='password').click()
        wd.find_element(By.CLASS_NAME, value='p-password').click()
        wd.find_element(By.CSS_SELECTOR, value='#password > input').send_keys(PASSWORD)
        wd.find_element(By.ID, value='login').click()
        wd.find_element(By.CSS_SELECTOR, value='#confirm_password > input').click()
        wd.find_element(By.CSS_SELECTOR, value='#confirm_password > input').send_keys(PASSWORD)

    def submit(self):
        wd = self.wd
        wd.find_element(By.ID, value='login').click()
        wd.find_element(By.CSS_SELECTOR,
                        value='#pv_id_2_content > div > form > div:nth-child(4) > button > span.p-button-label').click()

    def check_current_url(self):
        wd = self.wd
        time.sleep(1)
        return wd.current_url

    def destroy(self):
        self.wd.quit()
