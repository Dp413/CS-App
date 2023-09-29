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
import PySimpleGUI as sg
import helpScout

# SDLoginLogin
SdLogin = "<Username>"
SdPassword = "<Password>"

orderInfo = {
    'name': '',
    'orderNumber': '',
    'phoneNumber': '',
    'email': '',
    'subject': '<Subject>',
    'saleAmount': '',

}


def getByOrderNumber(driver, orderNumber):
    
    if (orderNumber == None):
        orderNumber = 1000
        return "Order Number is empty"
    SdSite = "<Web-Admin-Link>" + orderNumber + "&action=edit"

    # initialize the Chrome driver
    driver.switch_to.window(driver.window_handles[0])
    driver.get(SdSite)
    
    #orderInfo['Name'] = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td[1]/table/tbody/tr[1]/td[2]/text()[1]').text
    orderInfo['phoneNumber'] = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td[1]/table/tbody/tr[3]/td[2]').text
    orderInfo['orderNumber'] = orderNumber
    orderInfo['email'] = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td[1]/table/tbody/tr[4]/td[2]/a[1]').text
    #orderInfo['saleAmount'] = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[14]/td/table/tbody/tr[3]/td/table[1]/tbody/tr[4]/td[2]').text
    email = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td[1]/table/tbody/tr[4]/td[2]/a[1]').text
    helpScout.searchByEmail(driver, email, orderNumber)
    


def getByPhoneNumber(driver, phoneNumber):
    SdPhoneSearch = "<Web-Admin-Link>" + phoneNumber 
    driver.switch_to.window(driver.window_handles[0])
    driver.get(SdPhoneSearch)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    orderList = soup.find_all('tr', attrs={'onmouseover': "rowOverEffect(this)"})
    if len(orderList) > 1:
        orderNumberList = []
        layout = [[]]
        for record in orderList:
            soup = BeautifulSoup(str(record), 'html.parser')
            print(record)
            print("--------------------------------------------------------------------------------")
            orderNumber = soup.find('td').text
            orderNumberList.append(orderNumber)
            layout[0].append(sg.Button(orderNumber))
        layout[0].append(sg.Button('Home'))
        print(orderNumberList)
    
        #STEP 2 - create the window
        window = sg.Window('My New Orders', layout, alpha_channel=0.87, grab_anywhere=True,icon='ico16_1.ico')
        
        while True:
            event, values = window.read()
            if event is not "Home":
                getByOrderNumber(driver, event)
            elif event is 'Home':
                window.close()
                break
            if event is sg.WIN_CLOSED:
                break
            
                              
            
    elif len(orderList) == 1:
        soup = BeautifulSoup(str(orderList[0]), 'html.parser')
        orderNumber = soup.find('td').text
        getByOrderNumber(driver, orderNumber)
        # Going directly to order page
    else:
        # No orders found
        print("done")

def getOrderInfo():
    return orderInfo
