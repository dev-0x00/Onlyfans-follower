import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class Login:

    def __init__(self, browser, path) -> None:
        self.browser = browser
        self.path = path
        self.action = ActionChains(self.browser)
    
    def login_using_twitter(self):
        self.browser.get("https://onlyfans.com/")
        time.sleep(5)
    

    def login_using_google(self):
        self.browser.get("https://onlyfans.com/")
        time.sleep(5)

    
    def login_using_email(self, email, password):
        try:
            self.browser.get("https://onlyfans.com/")
            time.sleep(5)
            email_input = WebDriverWait(self.browser, 10).until(
                Ec.presence_of_element_located((
                    By.NAME, "email"
                ))
            )
            
            self.action.click(on_element=email_input)
            self.action.send_keys(email)
            self.action.perform()
            
            time.sleep(5)
            password_input = WebDriverWait(self.browser, 10).until(
                Ec.presence_of_element_located((
                    By.NAME, "password"
                ))
            )

            self.action.click(on_element=password_input)
            self.action.send_keys(password)
            self.action.perform()

            time.sleep(5)
            login_btn = WebDriverWait(self.browser, 10).until(
                Ec.presence_of_element_located((
                    By.CLASS_NAME, "g-btn.m-rounded.m-block.m-md.mb-0" 
                ))
            )
            
            self.action.move_to_element(to_element=login_btn)
            self.action.click()
            self.action.perform()

            time.sleep(30)
        
        except Exception as Error:
            print(Error)