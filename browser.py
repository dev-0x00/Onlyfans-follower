import undetected_chromedriver.v2 as uc

def GetBrowser():
    options = uc.ChromeOptions()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--profile-directory=Default")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--disable-plugins-discovery")
    #options.add_argument("--disable-notifications")
    #options.add_argument("--incognito")
    options.add_argument("user_agent=DN")
    #options.add_argument("--start-maximized")
    #prefs = {"profile.default_content_setting_values.geolocation": 1}
    #options.add_experimental_option("prefs", prefs)
    driver = uc.Chrome(options=options)
    return driver

def get_headless_browser():
    options = uc.ChromeOptions()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--profile-directory=Default")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--disable-plugins-discovery")
    #options.add_argument("--disable-notifications")
    options.add_argument("--headless")
    options.add_argument("user_agent=DN")
    #prefs = {"profile.default_content_setting_values.geolocation": 1}
    #options.add_experimental_option("prefs", prefs)
    driver = uc.Chrome(options=options)
    driver.maximize_window()
    return driver

def main():
    driver = GetBrowser()
    driver.get("https://accounts.google.com/")
    import time
    time.sleep(60000)
    
if __name__ == "__main__":
    main()