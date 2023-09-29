import gspread
import PySimpleGUI as sg
from datetime import datetime

# Keeps errors/bug list on a Google spreadsheet.

def errorBugFix():
    gc = gspread.service_account(filename=r'<Client-Secret.json>')
    sh = gc.open('Bug List')
    wks = sh.worksheet('Sheet1')
    datetime.now()
    
    sg.theme('Dark Grey 15')
    
    layout = [
    [sg.Text('Please enter the name of the person who reported the error.')],
    [sg.InputText('',key='name')],
    [sg.Text('Please enter bug description.')],
    [sg.InputText('',key='bugs')],
    [sg.Text('Can you reproduce the error? If so, please describe the steps.')],
    [sg.InputText('',key='reproduce')],
    [sg.Text('How many times has this error occurred?')],
    [sg.InputText('',key='times')],
    [sg.InputText(datetime.now(),key='date')],
    [sg.Button('Submit'), sg.Button('Cancel')]

]
    window = sg.Window('Error/Bug Fix Report', layout, size=(450, 285), resizable=True, icon='ico16_1.ico')
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            window.close()
            return
        if event == 'Submit':
            wks.append_row([values['name'],
                            values['bugs'],
                            values['reproduce'],
                            values['times'],
                            values['date']])
            print('Data has been submitted')
        window.close()

if __name__ == '__main__':
    errorBugFix()