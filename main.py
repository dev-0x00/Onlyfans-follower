import tkinter as tk
from tkinter import *
from follow import Follower
from commenters import Commenters
from scrapper import Scraplinks

import browser
import os

class Display:

    def __init__(self) -> None:
        #self.browser = browser.GetBrowser()
        self.path = os.getcwd()
    

    def display(self):
        window = tk.Tk()
        window.title("Controller")
        window.geometry("480x520")
        window.rowconfigure(0, weight=1)
        operation   = IntVar(value=1)

        frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2, padx=130, borderwidth=1, pady=0)
        frm_buttons.grid(row=0, column=0, sticky="nsew", padx=20, pady=30)
        actions = tk.Label(frm_buttons, text="    ACTIONS: ")
        actions.grid(row=0, column=0, padx=0, pady=10)
        
        check1 = Radiobutton(frm_buttons, variable=operation, text="GET COMMENTERS", value=1)
        check2 = Radiobutton(frm_buttons, variable=operation, text="  SUBSCRIBE  ", value=2)
        check3 = Radiobutton(frm_buttons, variable=operation, text=" GET OF LINKS", value=3)
        
        check1.grid(row=1, )
        check2.grid(row=2, )
        check3.grid(row=3, )

        start  = Button(frm_buttons, text="   START ACTION!  ", 
            bd=1, padx=20,command=lambda: self.start_action(
        operation.get()))
        start.grid(row=5, column=0, padx=0, pady=10)
        
        window.mainloop()
    

    def start_action(self, action):
        #get people who commented on a posts
        if int(action) == 1:
            posts = []
            scraped_fans = []

            driver = browser.GetBrowser()
            commenters = Commenters(driver, self.path)


            if len(open(f"{self.path}/files/fans_accounts.txt", "r").readlines() )\
                == 0:
                pass

            else:
               with open(f"{self.path}/files/fans_accounts.txt", "r") as fans:
                fans = fans.readlines()
                for fan in fans:
                    try:
                        profile_posts = commenters.fetch_profile_posts(fan)
                        [posts.append(profile) for profile in profile_posts]
                        
                    except Exception as Error:
                        print(Error)
                        pass
                    
                    scraped_fans.append(fan)
            
            for post in posts:
                try:
                    commenters.get_commenters(post)
                
                except Exception as Error:
                    pass
            
            self.writer("fans_accounts.txt", scraped_fans)
            driver.close()

        if int(action) == 2:
            subscribed_commenters = []
            driver = browser.GetBrowser()
            follow = Follower(driver, self.path)

            commenters = open(f"{self.path}/files/commenters.txt", "r").readlines()
            for commenter in commenters:
                try:
                    follow.follow_and_add_to_list(commenter, "commenters")
                
                except Exception as Error:
                    pass
                
                subscribed_commenters.append(commenter)
            
            self.writer("commenters.txt", subscribed_commenters)
            driver.close()
        
        
        if int(action) == 3:
            driver = browser.get_headless_browser()
            scrapper = Scraplinks(self.path, driver)
            try:
                scrapper.scrapper()
            
            except Exception as Error:
                pass

            driver.close()

                
    def writer(self, file, contents: list):
        new_contents  = []
        try:
            with open(f"{self.path}/files/{file}", "r+") as this_file:
                for data in this_file.readlines():
                    if data in contents:
                        pass

                    else:
                        new_contents.append(f"{data}\n")
            
                this_file.close()
            
            with open(f"{self.path}/files/{file}", "w") as _this_file:
                if len(new_contents) == 0:
                    _this_file.write("None\n")
                
                else:
                    _this_file.writelines(new_contents)
                _this_file.close()
    
        except Exception as Error:
            print(Error)
            pass


if __name__ == "__main__":
    display = Display()
    display.display()