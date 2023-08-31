from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


def get_playlist_info(url):
    response = requests.get(url)
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    playlist_content = []
    final_dictionary = {}

    try:
        consent_button = driver.find_element(by=By.CSS_SELECTOR,
                                             value="#yDmH0d > c-wiz > div > div > div > div.NIoIEf > div.G4njw > div.qqtRac > div.VtwTSb > form:nth-child(2) > div > div > button")
        consent_button.click()
    except:
        pass

    playlist_title = driver.find_element(by=By.XPATH,
                                         value='/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-playlist-header-renderer/div/div[2]/div[1]/div/yt-dynamic-sizing-formatted-string/div/yt-formatted-string').text
    channel_name = driver.find_element(by=By.XPATH,
                                       value="/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-playlist-header-renderer/div/div[2]/div[1]/div/div[1]/div[1]/div/yt-formatted-string[1]/a").text
    views_number = driver.find_element(by=By.XPATH,
                                       value="/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-playlist-header-renderer/div/div[2]/div[1]/div/div[1]/div[1]/ytd-playlist-byline-renderer/div/yt-formatted-string[2]").text
    videos_number = driver.find_element(by=By.XPATH,
                                         value="/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-playlist-header-renderer/div/div[2]/div[1]/div/div[1]/div[1]/ytd-playlist-byline-renderer/div/yt-formatted-string[1]").text

    final_dictionary["Playlist Title"] = playlist_title
    final_dictionary["Channel Name"] = channel_name
    final_dictionary["Views"] = views_number
    final_dictionary["Videos"] = videos_number

    names = driver.find_elements(by=By.ID, value="video-title")
    playlist_content = [name.text for name in names]
    final_dictionary["Playlist Content"] = {index: video for index, video in enumerate(playlist_content)}

    driver.quit()
    return final_dictionary


url = "https://www.youtube.com/playlist?list=PLnMypF4SBSUhooeCS2Js-T5y20lQaO6HV"
playlist_info = get_playlist_info(url)

def show_details():
    for key,value in playlist_info.items():
        print(key,":",value)
show_details()
