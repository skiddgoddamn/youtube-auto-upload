import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import chromedriver_py

def login_to_youtube(bot):
    bot.get("https://studio.youtube.com")
    time.sleep(3)

def upload_video(bot, video_path):
    upload_button = bot.find_element(By.XPATH, '//*[@id="create-icon"]')
    upload_button.click()
    time.sleep(1)
    
    upload_button = bot.find_element(By.XPATH, '//*[@id="text-item-0"]')
    upload_button.click()
    time.sleep(1)

    file_input = bot.find_element(By.XPATH, '//*[@id="content"]/input')
    abs_path = os.path.abspath(video_path)
    file_input.send_keys(abs_path)
    time.sleep(7)

def select_video_settings(bot):
    upload_button = bot.find_element(By.XPATH, '//*[@name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]')
    upload_button.click()
    time.sleep(1)

    next_button = bot.find_element(By.XPATH, '//*[@id="next-button"]')
    for _ in range(3):
        next_button.click()
        time.sleep(1)

def finalize_upload(bot):
    done_button = bot.find_element(By.XPATH, '//*[@id="done-button"]')
    done_button.click()
    time.sleep(5)

options = webdriver.ChromeOptions()
options.add_argument("--log-level=3")
options.add_argument("user-data-dir=C:\\Users\\qwe qwe\\AppData\\Local\\Google\\Chrome\\User Data")  
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-debugging-port=9222")
 #options.add_argument("--headless")  # Запуск в headless-режиме
options.add_argument("--disable-gpu")  
options.add_argument("--disable-extensions")  

dir_path = './videos'
videos = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f)) and f.endswith('.mp4')]
videos.sort()
count = len(videos)
print("   ", count, " Видео найдено в папке videos, готово к загрузке...")

chromedriver_path = chromedriver_py.binary_path

for video in videos:
    service = Service(executable_path=chromedriver_path)
    bot = webdriver.Chrome(service=service, options=options)

    try:
        login_to_youtube(bot)
        upload_video(bot, os.path.join(dir_path, video))
        select_video_settings(bot)
        finalize_upload(bot)
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}. Повторная попытка...")
        bot.quit()  # Закрываем браузер
        continue  # Продолжаем с следующим видео
    finally:
        bot.quit()
