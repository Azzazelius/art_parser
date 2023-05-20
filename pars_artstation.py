from bs4 import BeautifulSoup
import requests
import csv
from selenium import webdriver  # библиотека для работы с веб браузером из программы
from selenium.webdriver.chrome.service import Service  # импорт сервиса для обращения к драйверу Хрома
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  #  Модуль expected_conditions, EC для сокращения записи это набор условий ожидания, которые могут использоваться совместно с WebDriverWait
import time
import getpass
#
# browser_driver = Service("/usr/bin/chromedriver")  # Создание объекта сервиса ChromeDriver с указанием пути к драйверу браузера Chrome. Узнать путь в терминале: which chromedriver
# page_to_scrape = webdriver.Chrome(service=browser_driver)
# page_to_scrape.get('https://www.artstation.com/')

page_to_scrape = requests.get("https://www.artstation.com/'")  # какой сайт парсить
soup = BeautifulSoup(page_to_scrape.text, "html.parser")  # page_to_scrape.text представляет собой текстовое содержимое веб-страницы, которое необходимо разобрать. "html.parser" - это параметр, указывающий на использование парсера HTML для анализа HTML-код

url = "https://artstation.p.rapidapi.com/artists/jkind"

headers = {
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "artstation.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())