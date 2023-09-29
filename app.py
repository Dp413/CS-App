import PySimpleGUI as sg
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_auto_update import check_driver
import copies
import cancel
import DistroLogin
#import manufacture
import sales
import helpScout
import order
import datetime
import time as t
import threading
import updater
import copies
import socket
import error


# Checks to see if the server is online. 
'''def is_server_running(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(60)
        s.connect((ip, port))
        s.close()
        return True
    except socket.error as ex:
        print(ex)
        exit()

ip = "<Enter Server IP"
port = <Enter Port Number>
'''


threadingCondition = threading.Condition()
lastActionTime = None
defaultTimeout = 800
phoneNumber = ''

sg.theme('Dark Grey 13') 

#Checks for expiration date.
'''def program_expired():
    app_date = datetime.datetime(year=2023,month=1,day=15) 
    now = datetime.datetime.now()
    if (now-app_date).days >=0: 
        sg.popup("Error","Your tool has expired")
        exit()
    else:
        pass

is_server_running(ip, port) 
'''

def runGUILoop():
    global lastActionTime
    # STEP3 - the event loop
    while True:
        threadingCondition.acquire()
        lastActionTime = datetime.datetime.now()
        threadingCondition.notifyAll()
        threadingCondition.release()
        event, values = window.read()  # Read the event that happened and the values dictionary
        if event == sg.WIN_CLOSED or event == ' Close ': 
            driver.quit()
            # If user closed window with X or if user clicked "Exit" button then exit
            break
        if event == 'Order Number':
            print('You pressed the button and entered value:' + ' ' + values[0])
            threadingCondition.acquire()
            lastActionTime = datetime.datetime.now()
            threadingCondition.notifyAll()
            threadingCondition.release()
            if values[0] != '':
                order.getByOrderNumber(driver, values[0])            
            
            
        if event == 'All Search':
            threadingCondition.acquire()
            lastActionTime = datetime.datetime.now()
            threadingCondition.notifyAll()
            threadingCondition.release()
            
            order.getByPhoneNumber(driver, values[0])
        if event == 'Distro Search': 
            DistroLogin.distroLogin()
        if event == 'Send Email':
            helpScout.sendEmail(driver, order.getOrderInfo(), copies.getEmailBody(event))
        if event == 'Review Email':
            copies.getEmailBody(event)           
        if event == 'Fitment Check':
            copies.getEmailBody(event)
        if event == 'Universal Pass':
            copies.getEmailBody(event)
        if event == 'Sale Email':
            copies.getEmailBody(event)           
        if event == 'Air Lift Email':
            copies.getEmailBody(event)
        if event == 'Refund Email':
            copies.getEmailBody(event)
        #if event == 'Mfg List':
            #manufacture.manufactures() 
        if event == 'Update':
            updater.adminUpdate()  
            quit() 
        if event == 'Sales':
            orderInfo = order.getOrderInfo()
            sales.sales(orderInfo)
        if event == 'Cancellation':
            orderInfo = order.getOrderInfo() 
            cancel.cancellation(orderInfo)
        if event == 'Error/Bug Report':
            error.errorBugFix()
       


            
   # Search by phone number - https://www.sdtrucksprings.com/adzmin24sd/orders.php?search=520-257-6491

    # https://www.sdtrucksprings.com/adzmin24sd/orders.php?search=4172471670&page=1&oID=759772&action=edit

    # onmouseover="rowOverEffect(this)"
def checkForIdle():
    global lastActionTime
    
    while True:
        currTime = datetime.datetime.now()
        threadingCondition.acquire()
        if lastActionTime != None:
            
            if (currTime - lastActionTime).total_seconds() > defaultTimeout:
                driver.switch_to.window(driver.window_handles[0])
                driver.refresh()
                print("Hitting Timeout Refreshing Page")
                lastActionTime = datetime.datetime.now()
        threadingCondition.notifyAll()
        threadingCondition.release()
        t.sleep(2)



# HelpScout Login 
helpScoutLogin = "<Helpscout-Login>"
helpScoutPassword = "<HelpScout Passowrd>"
hsSite = "<HelpScout-Login-Link>"

# SD Login
SdLoginSite = "<Web-Admin-Login-Link>"
SdLogin = "<Username>"
SdPassword = "<Password>"

universalPass = "<Website-Universal-Master-Pass>"



# sg.theme_previewer() - Views a preview of selectable themes



#Selenium Chrome Driver
driver = webdriver.Chrome("chromedriver")

driver.get(SdLoginSite)



# find username/email field and send the username itself to the input field
try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "admin_name")))
except:
    driverLoaded = False

driver.find_element(By.ID, "admin_name").send_keys(SdLogin)

# find password input field and insert password as well
driver.find_element(By.ID, "admin_pass").send_keys(SdPassword)

# click login button
driver.find_element(By.ID, "btn_submit").click()

# Open a new window
driver.execute_script("window.open('');")

# Switch to the new window and open new URL
driver.switch_to.window(driver.window_handles[1])
driver.get(hsSite)
driver.find_element(By.ID, "email").send_keys(helpScoutLogin)

# find password input field and insert password as well
driver.find_element(By.ID, "password").send_keys(helpScoutPassword)

# click login button
driver.find_element(By.ID, "logInButton").click()
driver.switch_to.window(driver.window_handles[0])

# Layout of GUI
layout = [
    [sg.Text('Enter Information:')],
    [sg.InputText()],
    [sg.Button('Order Number'), sg.Button('All Search'), sg.Button('Distro Search'), sg.Button('Cancellation')],
    [sg.Text('        --------------------------- Copy Buttons ---------------------------')],
    [sg.Button('Universal Pass'), sg.Button('Fitment Check')],
    [sg.Button('Review Email'),sg.Button('Sale Email'), sg.Button('Air Lift Email'), sg.Button('Refund Email')],
    [sg.Text('Send Email:'), sg.Button('Send Email'), sg.Button('Sales')],
    [sg.Text(' ')],
    [sg.Text('                                           '), sg.Button('Error/Bug Report'),sg.Button('Update')], 
]

# Create the window
window = sg.Window('SD Admin', layout)

# set the window icon
window.SetIcon("<Icon>")

# Created the Threads
t1 = threading.Thread(target=runGUILoop, args=())
t2 = threading.Thread(target=checkForIdle, args=())
 
# Started the threads
t1.start()
t2.start()


