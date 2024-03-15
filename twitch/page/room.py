from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from .page import Page


class RoomPage(Page):
    def close_popout(self):
        # found one pop-out element
        # <div data-a-target="tw-core-button-label-text" class="Layout-sc-1xcs6mc-0 jmTjSc">Start Watching</div>
        try:
            ele = self.wait.until(lambda x: x.find_element(By.XPATH, "//*[text()='Start Watching']"))
            if ele:
                ele.click()
        except (NoSuchElementException, TimeoutException):
            pass
    
    def if_video_playing(self):
        ele = self.wait.until(lambda x: x.find_element(By.XPATH, f"//video"))
        result = self.wait.until(lambda x: x.execute_script("return !arguments[0].paused;", ele))
        return result
