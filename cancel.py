import gspread
import PySimpleGUI as sg
from datetime import datetime



def cancellation(orderInfo):
    # Connect to Google spreadsheet
    gc = gspread.service_account(filename=r'<Client-Secret>')
    sh = gc.open('Copy of Cancellation-Prevention 11/22')
    wks = sh.worksheet('Cancellation Prevent 11/1 to Present')

    # Dropdowns or Selections in spreadsheet
    me = ['Derrik.P']
    rep = ['Devin.G', 'Oscar.M', 'Nick.D', 'Alex.M', 'Alyrra.G', 'BrianB', 'BrockD','Christopher.P','David.B', 'Derrick.P', 'Heather.P', 'Jacque.R', 'Matt.V', 'Mary.P', 'Thomas.M', 'Tristan. P', 'online']
    trueFalse = ['Yes', 'No']
    reason = ['Backorder', 'Discontinued', 'Fitment Issue', 'Pricing Issue', 'No Longer Needs', 'wait time', 'ordered wrong']
    checkDistro = ['Transamerica(TR)', 'KeyStone(KS)', 'Meyer(MY)', 'Checked ALL 3']
    discount = ['$0', '$5', '$10', 'Requested For Further $$ Approval']
    dt = datetime.now()

    #Layout of GUI
    sg.theme('Dark Grey 15')
    layout = [
    [sg.Text('Date:'), sg.InputText(dt.strftime('%m-%d-%Y'), key='date')],
    [sg.Text('Order Number:'),sg.InputText(key='orderNumber', default_text = orderInfo['orderNumber']), sg.Text('Rep Saving:'), sg.OptionMenu(me, key='repSaver')],
    [sg.Text('Rep Who Took Order'), sg.OptionMenu(rep, key='repTaker'), sg.Text('You Saved It?'), sg.OptionMenu(trueFalse,key = 'saved')],
    [sg.Text('Amount Saved OR Lost: '), sg.InputText(key='amount')],
    [sg.Text('Sorry Package Sent:'), sg.OptionMenu(trueFalse, key = 'sorry'), sg.Text('Reason For Cancellation:'), sg.OptionMenu(reason, key='reason')],
    [sg.Text('Customer' + "'" + 's Phone Number:'),sg.InputText(key='phone', default_text = orderInfo['phoneNumber'])],
    [sg.Text('Part Number:'),sg.InputText(key='part')],
    [sg.Text('Checked Distro?'),sg.OptionMenu(checkDistro, key='distro')],
    [sg.Text('Discount Offered?'),sg.OptionMenu(discount, key='discount')],
    [sg.Text('Alternative Product Offered?'), sg.Radio('Yes', 'RADIO1', default = True, key = 'alternative'), sg.Radio('No', 'RADIO1', default = True, key = 'alternative'), sg.Text('Product Offered:'), sg.InputText(key='productNumber')],
    [sg.Text('Customer' + "'" + 's Comments'), sg.InputText(key='comments')],
    [sg.Text('Unable To Save Over $500 Slack'),sg.Radio('Yes', 'RADIO2', default = True, key='slackSaved'), sg.Radio('No', 'RADIO2', default = True, key='slackSaved')],
    [sg.Text('Saved Order and Slacked?'),sg.Radio('Yes', 'RADIO3', default = True, key='slackUnableToSave'), sg.Radio('No', 'RADIO3', default = True, key='slackUnableToSave')],
    [sg.Text("Slack Message/Additional Notes"), sg.Button('Send Slack'), sg.InputText(key = 'slack')],
    [sg.Submit(), sg.Cancel()],
]
    window = sg.Window('Cancellation Prevention', layout, size=(750, 450), resizable=True, icon='ico16_1.ico')
    
    # If submit is hit appends data to sheet.
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            window.close()
            return
        if event == 'Submit':
            wks.append_row([values['date'],
             values['orderNumber'],
             values['repTaker'],
             values['saved'],
             values['amount'],
             values['repSaver'],
             values['phone'], 
             values['part'], 
             values['reason'],
             values['distro'], 
             values['discount'],
             values['sorry'], 
             values['alternative'],
             values['productNumber'], 
             values['comments'], 
             values['slackUnableToSave'],
             values['slackSaved'],
             values['slack']])
        

            print('Data has been submitted')
        window.close()
    
if __name__ == '__main__':
    cancellation()
