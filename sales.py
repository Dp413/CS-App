import gspread
import PySimpleGUI as sg
from datetime import datetime
import order


def sales(orderInfo):
    # Opens Google spreadsheet
    gc = gspread.service_account(filename=r'<Client-Secret-Json>')
    sh = gc.open('Copy of Derrick Sales Monthly Notes')
    wks = sh.worksheet('January 2023')

    # Worksheet selections
    me = ['Derrick.P']
    upsell = ['expedite', 'hardware', 'shocks', 'sway bars', 'compressor', 'no']
    trueFalse = ['Yes', 'No']
    reason = ['Backorder', 'Discontinued', 'Fitment Issue', 'Pricing Issue', 'No Longer Needs']
    checkDistro = ['Transamerica(TR)', 'KeyStone(KS)', 'Meyer(MY)', 'Checked ALL 3']
    discount = ['$0', '$5', '$10', 'Requested For Further $$ Approval']
    dt = datetime.now()

    # Layout Window
    sg.theme('Dark Grey 15')
    layout = [
    [sg.Text('Name:'), sg.InputText(key='name', default_text = orderInfo['name'])],
    [sg.Text('Phone Number:'), sg.InputText(key='phoneNumber', default_text = orderInfo['phoneNumber'])],
    [sg.Text('Y/M/M'), sg.InputText(key = 'YMM'), sg.Text('Email: '), sg.InputText(key = 'email', default_text = orderInfo['email'])],
    [sg.Text('Pre-Order?:'), sg.Radio('Yes', 'RADIO1', default = True, key = 'POE'), sg.Radio('No', 'RADIO1', default = True, key = 'POE'), sg.Text('You Scheduled Call?'), sg.OptionMenu(trueFalse,key = 'scheduledCalled')],
    [sg.Text('Called them back?/They Called Back? '), sg.Radio('Yes', 'RADIO2', default = True ,key='Called'), sg.Radio('No', 'RADIO2', default = True, key='Called')],
    [sg.Text('PO#:'), sg.InputText(key='PO', default_text = orderInfo['orderNumber']), sg.Text('Sale Amount:'), sg.InputText(key='SA', default_text = orderInfo['saleAmount'])], 
    [sg.Text('Upsell?: '), sg.OptionMenu(upsell, key = 'upsell')],
    [sg.Submit(), sg.Cancel()],
]
    window = sg.Window('Cancellation Prevention', layout, size=(800, 250), resizable=True, icon='ico16_1.ico')

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        if event == 'Submit':
            wks.append_row([values['name'],
             values['phoneNumber'], 
             values['YMM'],
             values['email'],
             values['POE'],
             values['scheduledCalled'],
             values['Called'],
             values['PO'],
             values['SA'],
             values['upsell']])            
                     

            print('Data has been submitted')
    window.close()
    
if __name__ == '__main__':
    sales()
