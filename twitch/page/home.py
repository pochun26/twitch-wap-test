from selenium.webdriver.common.by import By
from .page import Page
from .search import SearchPage


class TwitchHomePage(Page):
    def go_home(self):
        self.driver.get("https://m.twitch.tv/")

    def do_search(self, key_word):
        ele = self.wait.until(lambda x: x.find_element(By.XPATH, f"//a[@aria-label='Search']"))
        ele.click()
        ele = self.wait.until(lambda x: x.find_element(By.XPATH, f"//input[@type='search']"))
        ele.send_keys(key_word)
        ele = self.wait.until(lambda x: x.find_element(By.XPATH, f"//p[@title='{key_word}' and contains(@class, 'hWrlxE')]"))
        ele.click()
        return SearchPage(self.driver)
