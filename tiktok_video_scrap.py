from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen


def downloadVideo(link, id):
    cookies = {
        # Please get this data from the console network activity tool
        # This is explained in the video :)
    }

    headers = {
        # Please get this data from the console network activity tool
        # This is explained in the video :)
    }

    params = {
        'url': 'dl',
    }

    data = {
        'id': link,
        'locale': 'en',
        'tt': 'NDZuMTU2',
    }

    response = requests.post('https://ssstik.io/abc', params=params,
                             cookies=cookies, headers=headers, data=data)
    downloadSoup = BeautifulSoup(response.text, "html.parser")

    downloadLink = downloadSoup.a["href"]

    mp4File = urlopen(downloadLink)
    # Feel free to change the download directory
    with open(f"videos/{id}.mp4", "wb") as output:
        while True:
            data = mp4File.read(4096)
            if data:
                output.write(data)
            else:
                break


driver = webdriver.Chrome()
# Change the tiktok link
driver.get("https://www.tiktok.com/@papayaho.cat")

time.sleep(1)

scroll_pause_time = 1
screen_height = driver.execute_script("return window.screen.height;")
i = 1

while True:
    driver.execute_script(
        "window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
    i += 1
    time.sleep(scroll_pause_time)
    scroll_height = driver.execute_script("return document.body.scrollHeight;")
    if (screen_height) * i > scroll_height:
        break

soup = BeautifulSoup(driver.page_source, "html.parser")
# make sure to inspect the page and find the correct class
videos = soup.find_all("div", {"class": "tiktok-yz6ijl-DivWrapper"})

print(len(videos))
for index, video in enumerate(videos):
    downloadVideo(video.a["href"], index)
    time.sleep(10)
