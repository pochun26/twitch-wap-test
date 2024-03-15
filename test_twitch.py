
import pytest
from selenium import webdriver
from twitch.page.home import TwitchHomePage
from util import save_screenshot
import subprocess

@pytest.fixture
def driver():
    recording_process = subprocess.Popen(['ffmpeg', '-y', '-f', 'x11grab', '-s', '2240x1400', '-i', ':0.0', '-r', '30', 'output.mp4'])
    # Change device here
    mobile_emulation = {"deviceName": "iPhone 12 Pro"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()
    recording_process.terminate()


def test_bot_functionality(driver):
    cur_page = TwitchHomePage(driver)
    cur_page.go_home()
    cur_page = cur_page.do_search("StarCraft II")

    cur_page.scroll_down(2)
    cur_page = cur_page.enter_random_room()

    cur_page.close_popout()

    if cur_page.if_video_playing():
        save_screenshot(driver)
        ret = True
    else:
        ret = False

    assert ret is True
