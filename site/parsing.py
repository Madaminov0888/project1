from logging import exception
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import speech_recognition as sr
import ffmpy, urllib, pydub
import os,time, requests, sys


MAIN_url = "https://visa.vfsglobal.com/tur/en/pol/login"
email = "madaminovmuhammadjon31@gmail."+"com"
password = "Fe*12fe@"

sitekey = "6LfDUY8bAAAAAPU5MWGT_w0x5M-8RdzC29SClOfI"
api_key = "529619540e8720bdaa0e671809350217"

options = Options()
ua = UserAgent(verify_ssl=False)
ua.update()
userAgent = ua.random
options.add_argument(f'user-agent={userAgent}')
BROWSER = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
BROWSER.get(MAIN_url)
time.sleep(5)


def login(email, password):
    element = BROWSER.find_element(By.ID, "mat-input-0")
    element2 = BROWSER.find_element(By.ID, "mat-input-1")
    element.send_keys(email)
    element2.send_keys(password)
    print("bitdi1")
    time.sleep(25)
    return after_login()


def after_login():
    element = BROWSER.find_element(By.CLASS_NAME, "mat-checkbox-frame")
    element.click()


login(email, password)

