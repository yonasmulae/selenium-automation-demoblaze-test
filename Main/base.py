from selenium import webdriver


class Base:
    driver = webdriver.Chrome()

    def init(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\webdriver\chromedriver.exe')
        self.driver.get("https://www.demoblaze.com")
        self.driver.maximize_window()
        return self.driver

    def tear_down(self):
        self.driver.quit()

