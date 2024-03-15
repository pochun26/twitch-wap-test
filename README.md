# Selenium Test Case for Twitch(WAP)

## Test Steps
1. Go to Twitch
2. Click in the search icon
3. Input StarCraft II
4. Scroll down 2 times
5. Select one streamer
6. On the streamer page wait until all is load and take a screenshot

## Setup
1. [ChromeDriver](https://chromedriver.chromium.org/downloads)
2. Install python packages
```shell
$ pip install -r requirements.txt
```

## Run test
```shell
$ pytest
```

## File structue
- test_twitch.py: pytest
- twitch/page/page.py: The page parent object
- twitch/page/home.py: twitch home page function
- twitch/page/search.py: twitch search page function
- twitch/page/room.py: twitch room page function
- util.py: save/delete screenshot

## TODO
- gif
