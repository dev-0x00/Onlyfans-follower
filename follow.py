import time

from login import Login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class Follower:

    def __init__(self, browser, path) -> None:
        self.browser  = browser
        self.path     = path
        accounts      = open(f"{self.path}/files/accounts.txt", "r").readlines()
        self.login    = Login(self.browser, self.path)
        self.email    = accounts[0].split(",")[0]
        self.password = accounts[0].split(",")[1]
        self.action   = ActionChains(self.browser)

        self.login.login_using_email(self.email, self.password)
    

    def follow_and_add_to_list(self, commneter_link, file):
        self.browser.get(commneter_link)
        time.sleep(5)

        WebDriverWait(self.browser, 10).until(
            Ec.presence_of_element_located((
                By.CLASS_NAME, "m-rounded.m-flex.m-space-between.m-lg.g-btn"
            ))
        ).click()

        time.sleep(5)
        WebDriverWait(self.browser, 10).until(
            Ec.presence_of_all_elements_located((
                By.CLASS_NAME, "g-btn.m-rounded.m-border"
            ))
        )[2].click()

        if file == "commenters":
            
            radio = WebDriverWait(self.browser, 10).until(
            Ec.presence_of_element_located((
                By.ID, "users-list-976746733"
                ))
            )
            
            self.browser.execute_script("arguments[0].click();", radio)
            time.sleep(5)
        
        elif file == "creators":
            WebDriverWait(self.browser, 10).until(
            Ec.presence_of_element_located((
                By.CLASS_NAME, "users-list-976746733"
            ))
            ).click()