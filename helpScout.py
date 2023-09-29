import imp
import time
import requests
from requests import get, request
from bs4 import BeautifulSoup, SoupStrainer
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import PySimpleGUI as sg
import urllib.parse
subject = '<Subject>'

# Searches customers in Helpscout by their email and order number

def searchByEmail (driver, email, orderNumber):
    driver.switch_to.window(driver.window_handles[1])
    driver.get('<Link>' + urllib.parse.quote(email) + '%20OR%20' + orderNumber)
    driver.switch_to.window(driver.window_handles[0])
    
# Creates an email filling in the recipient and the subject.
# Copies.py has the buttons to click to paste for body.

def sendEmail (driver, orderInfo, emailBody):
    driver.switch_to.window(driver.window_handles[1])
    driver.get('<LINK>')
    try:
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#tkReply > section > section > section > div > div")))
    except:
        driverLoaded = False
    driver.find_element(By.XPATH,'//*[@id="to-input"]').send_keys(orderInfo["email"])
    driver.find_element(By.XPATH,'//*[@id="ticket-subject"]').send_keys(orderInfo["subject"])

