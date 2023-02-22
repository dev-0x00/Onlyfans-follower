import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class Scraplinks:

    def __init__(self, path, browser) -> None:
        self.path = path
        self.browser = browser
        self.action = ActionChains(self.browser)

    
    def scrapper(self):
        self.browser.get("https://fansmetrics.com/onlyfans-trial-links")

        time.sleep(5)
        scrolls = 0
        #scroll and fetch all tweets from out timeline
        free_fans = []
        while scrolls < 100:
            print(f"[+] scrapping page {scrolls} of 10")
            #self.browser.execute_script("document.body.style.zoom='55%'")
            fans_profile = WebDriverWait(self.browser, 10).until(
        
            Ec.presence_of_all_elements_located((
                By.CLASS_NAME, "col-md-4"
                ))
            )

            for fan_profile in fans_profile:
                try:
                    
                        fan_link = fan_profile.find_element(
                            By.CLASS_NAME, "creator-card-v3"
                            ).find_elements(
                        By.TAG_NAME, "a")[0].get_attribute("href")
                    
                        if fan_link in free_fans or "fansmetrics.com" in fan_link.split("/"):
                            pass

                        else:
                            with open(f"{self.path}/files/creators.txt", "a") as this_file:
            
                                if f"{fan_link}\n" in open(f"{self.path}/files/creators.txt", "r").readlines():
                                    pass

                                else:
                                    this_file.write(f"{fan_link}\n")
                    
                                this_file.close()
                
                except Exception as Error:
                    pass
            
            self.action.send_keys(Keys.PAGE_DOWN)
            self.action.send_keys(Keys.PAGE_DOWN)
            self.action.send_keys(Keys.PAGE_DOWN)
            self.action.send_keys(Keys.PAGE_DOWN)
            self.action.send_keys(Keys.PAGE_DOWN)
            self.action.perform()
            time.sleep(10)
            scrolls += 1
        

        
