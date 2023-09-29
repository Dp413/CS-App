import os
import urllib.request
from selenium import webdriver
import time as t


def adminUpdate():
    
    
    # The URL of the remote .exe file on the server
    url = "<Server-Link-With-EXE>"
    driver = webdriver.Chrome("chromedriver")


    driver.get(url)
    t.sleep(600)
    driver.quit()
    
if __name__ == '__main__':
    adminUpdate()