from selenium.webdriver.support.ui import WebDriverWait


class Page:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def get_wait(self, sec):
        return WebDriverWait(self.driver, sec)
