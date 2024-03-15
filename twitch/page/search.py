from selenium.webdriver.common.by import By
import random
from .page import Page
from .room import RoomPage
import time


class SearchPage(Page):
    def enter_random_room(self):
        ele = self.wait.until(lambda x: x.find_elements(By.CLASS_NAME, "tw-aspect"))
        picked_room = random.choice(ele)
        picked_room.click()
        return RoomPage(self.driver)

    def scroll_down(self, times):
        for _ in range(times):
            # wait loading
            self.wait.until(lambda x: x.find_elements(By.CLASS_NAME, "tw-aspect"))
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
            time.sleep(2)
