import PySimpleGUI as sg
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


mfg = ''
partNumber = ''
keystone = '<Link>'
keystoneLogin = '<Login>'
keystonePassword = '<Password>'
keystoneSearch = "<Link>" + mfg + partNumber + "&ssid=ed7c3136-a835-4384-8bc0-8087c957ca6f&allin=true"

meyermfg = ''
meyer = '<Link>'
meyerLogin = '<Login>'
meyerPassword ='<Password>'
meyerSearch = ''

turn14 = '<Link>'
turn14Login = '<Login>'
turn14Password = '<Password>'
turn14Search = '<Link>' + partNumber

def distroLogin():
    # Opens Chrome webdriver.
    driver = webdriver.Chrome("chromedriver")
    # Goes to Link and opens in first tab
    driver.get("<Link>")
    driver.execute_script("window.open('');")

    # Switches to second tab
    driver.switch_to.window(driver.window_handles[1])

    # Opens this link in new tab
    driver.get(keystone)
    # Finds Username and inputs username
    driver.find_element(By.ID, "Username").send_keys(keystoneLogin)
    # find password input field and insert password as well
    driver.find_element(By.ID, "Password").send_keys(keystonePassword)
    # click login button
    driver.find_element(By.ID, "SignInButton").click()

    driver.execute_script("window.open('');")
    
    # Switches to third tab.
    driver.switch_to.window(driver.window_handles[2])
    driver.get(meyer)
    # Inputs Username
    driver.find_element(By.XPATH,'//*[@id="username"]/input').send_keys(meyerLogin)
    # find password input field and insert password as well
    driver.find_element(By.XPATH, '//*[@id="password"]/input').send_keys(meyerPassword)
    # click login button
    driver.find_element(By.XPATH, '/html/body/app-root/ion-app/ion-router-outlet/public/ion-content/public-layout-desktop/div/div/div[2]/div[1]/div[2]/login/login-container-desktop/login-form/form/div/button-spinner/ion-button/span').click()
    
    # Meyer Search 
    driver.execute_script("window.open('');")
    # Fourth Tab.
    driver.switch_to.window(driver.window_handles[3])
    driver.get(turn14)
    # Inputs Username
    driver.find_element(By.NAME, "username").send_keys(turn14Login)
    # find password input field and insert password as well
    driver.find_element(By.NAME, "password").send_keys(turn14Password)
    # click login button
    driver.find_element(By.XPATH,'//*[@id="login"]/form/div[3]/button').click()

    # Layout Window 
    sg.theme('Dark Grey 15')  # Let's set our own color theme
    layout = [
    [sg.Input()],
    [sg.Button('Air Lift'), sg.Button('Firestone'), sg.Button('Hellwig'), sg.Button('Addco'), sg.Button('Exit')],
    ]
    window = sg.Window("Enter Part Number and Select Manufacture", layout, icon='ico16_1.ico')
    
    while True:
        event, partNumber = window.read()
            # End program if user closes window or
        # presses the OK button
        if event == 'Air Lift':
            mfg = 'AIR'
            meyermfg = 'ALC'
        if event == 'Firestone':
            mfg = 'FRS'
            meyermfg = 'FIR'
        if event == 'Hellwig':
            mfg = 'HWG'
            meyermfg = 'HWG'      
        if event == 'Addco':
            mfg = 'ADD'
            meyermfg = 'ado'
        if event == sg.WIN_CLOSED or event == 'Exit':
            window.close()            
            break

        layout.append(partNumber[0])
        driver.switch_to.window(driver.window_handles[0])
        driver.get("<Link>" + partNumber[0])
        driver.switch_to.window(driver.window_handles[1])
        driver.get("<Link>" + mfg + partNumber[0] + "&ssid=ed7c3136-a835-4384-8bc0-8087c957ca6f&allin=true")
        driver.switch_to.window(driver.window_handles[2])
        driver.get("<Link>" + meyermfg + partNumber[0])
        driver.switch_to.window(driver.window_handles[3])
        driver.get('<Link>' + partNumber[0])
        
