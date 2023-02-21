import time

from login import Login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.by import By

class Commenters:

    def __init__(self, browser, path) -> None:

        self.browser  = browser
        self.path     = path
        accounts      = open(f"{self.path}/files/accounts.txt", "r").readlines()
        self.login    = Login(self.browser, self.path)
        self.email    = accounts[0].split(",")[0]
        self.password = accounts[0].split(",")[1]

        self.login.login_using_email(self.email, self.password)
    

    def fetch_profile_posts(self, of_profile) -> list:
        profile_posts = []
        self.browser.get(of_profile)
        time.sleep(5)

        WebDriverWait(self.browser, 10).until(
            Ec.presence_of_element_located((
                By.CLASS_NAME, "m-rounded.m-flex.m-space-between.m-lg.g-btn"
            ))
        ).click()

        time.sleep(5)
        self.browser.execute_script("document.body.style.zoom='25%'")

        time.sleep(5)
        links  = WebDriverWait(self.browser, 10).until(
            Ec.presence_of_all_elements_located((
                By.CLASS_NAME, "b-tabs__nav__item.has-tooltip"
            ))
        )

        #commenters = open(f"{self.path}/files/commenters.txt", "r").readlines()
        for link in links:
            link = link.get_attribute("href")
            profile_posts.append(link)
    
        return profile_posts
    

    def get_commenters(self, post_link) -> None:
        commenters_list = open(f"{self.path}/files/commenters.txt" , "a")
        self.browser.get(post_link)
        time.sleep(5)

        self.browser.execute_script("document.body.style.zoom='25%'")
        try:
            more_replies = WebDriverWait(self.browser, 10).until(
                Ec.presence_of_element_located((
                    By.CLASS_NAME, "b-comments__load-more-btn"
                ))
            )

            while True:
                more_replies.find_element(
                    By.TAG_NAME, "button"
                ).click()
        
        except Exception as Error:
            pass

        time.sleep(5)
        commenters  = WebDriverWait(self.browser, 10).until(
            Ec.presence_of_all_elements_located((
                By.CLASS_NAME, "b-username-row.m-inline"
            ))
        )

        time.sleep(5)
        for commenter in commenters:
            commenter = commenter.find_element(
                By.TAG_NAME, "a"
            ).get_attribute("href")
            if f"{commenter}\n" in open(f"{self.path}/files/commenters.txt", "r").readlines():
                pass

            else:
                commenters_list.write(f"{commenter}\n")