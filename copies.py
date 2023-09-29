import PySimpleGUI as sg
import helpScout

# This sets values to buttons for click to copy

partNumber = ''
timeFrame = ''
originalCost = ''
customerCost = ''
subject = '<Subject>'

reviewEmail = '''Hello,

Thanks again for letting me assist you today with some updated information about your order!

Here is my direct extension <Phone-Number>, for if you ever need to reach out feel free! My name is <Name> and I will be happy to assist you at any time! It's been my pleasure to help you. If you were happy with my service, if you would be so kind to leave me a Google or Trust Pilot review on the links provided below as it is greatly appreciated!.

Good reviews with my name do help me with the company.
 
Also if I get a couple of them it can put some extra cash in my pocket! 
 
Thanks again and have a great rest of your day! 
 
Please use this link below to be directed to Google to leave a review: 
<Link>
Please use this link below to leave a Trust Pilot Review : 
<Link>
Please use this link for the BBB:  
<Link>

Warm Regards,'''

saleEmail = '''Hello,

Thanks again for letting me assist you today with placing your order!

Here is my direct extension <Phone-Number>, for if you ever need to reach out feel free! My name is Derrik and I will be happy to assist you at any time! It's been my pleasure to help you. If you were happy with my service, if you would be so kind to leave me a Google or Trust Pilot review on the links provided below as it is greatly appreciated!.

Good reviews with my name do help me with the company.
 
Also if I get a couple of them it can put some extra cash in my pocket! 
 
Thanks again and have a great rest of your day! 
 
Please use this link below to be directed to Google to leave a review: 
<Link>
Please use this link below to leave a Trust Pilot Review : 
<Link>
Please use this link for the BBB:  
<Link> 

Warm Regards,'''

refundEmail = '''Hello,

Thanks again for letting me assist you today with some updated information about your order! I have submitted your order for cancellation, please allow 24/48 hours for the funds to process back to the original payment method.

Here is my direct extension <Phone-Number>, for if you ever need to reach out feel free! My name is Derrik and I will be happy to assist you at any time! It's been my pleasure to help you. If you were happy with my service, if you would be so kind to leave me a Google or Trust Pilot review on the links provided below as it is greatly appreciated!.

Good reviews with my name do help me with the company.
 
Also if I get a couple of them it can put some extra cash in my pocket! 
 
Thanks again and have a great rest of your day! 
 
Please use this link below to be directed to Google to leave a review: 
<Link>
Please use this link below to leave a Trust Pilot Review : 
<Link>
Please use this link for the BBB:  
<Link> 

Warm Regards,'''

fitmentCheck = '''Thank you for choosing SDtrucksprings.com, Please review the following information for accuracy.
If anything is wrong please contact us immediately at <Phone-Number> or <Email-Address>
Make:
Model:
4wd or 2wd:
Cab and Chassis or pick up:
Lifted or Stock Suspension:
Lead time:
Custom Product/Special Order/Non-Returnable:
Representative: 
Email: <Email-Address>
Ext: 524
Our Shipping/Return Policy:
<Link>
<Name> - Ext 524'''

universalPass = '<Website-Admin-Pass>'

airLiftEmail = ''' Hello!
We are currently still awaiting stock on''' + partNumber +'''. We expect this to arrive within the next''' + timeFrame + '''. I do have them in stock at a 3rd party dropship partner but their price is slightly higher than our price. Normally it would cost''' + originalCost + ''' but I can split that with you and collect only''' + customerCost + ''' and would have it shipped out to you within 24 hours. 

If you would like to go this route we would be able to charge the existing card on file or use another form of payment.

However, if you provide me with your year, make, model and drive type I can look into alternative products that are on par or superior and ready to ship today.
Please let us know how you would like to proceed.
If you have any questions feel free to reach out at <Phone-Number>, I look forward to hearing from you soon!'''

def getEmailBody(event):
    emailBody = None
    airLiftEmail = ''
    if event == sg.WIN_CLOSED or event == 'Cancel':
        return None
    if event == 'Review Email':
        sg.clipboard_set(reviewEmail)
        emailBody = reviewEmail
    if event == 'Fitment Check':      
        sg.clipboard_set(fitmentCheck)      
        
    if event == 'Universal Pass':
        sg.clipboard_set(universalPass)
    if event == 'Refund Email':
        sg.clipboard_set(refundEmail)
        emailBody = refundEmail
    if event == 'Sale Email':
        sg.clipboard_set(saleEmail)
        emailBody = saleEmail
    if event == 'Air Lift Email':
    #open new window to type in part number and time frame
        layout = [[sg.Text('Part Number'), sg.InputText(key = 'partNumber')],
                    [sg.Text('Time Frame'), sg.InputText(key = 'timeFrame')],
                    [sg.Text('Original Cost: $'), sg.InputText(key = 'originalCost')],
                    [sg.Text('Customer Cost: $'), sg.InputText(key='customerCost')],
                    [sg.Button('Submit'), sg.Button('Cancel')]]
        window = sg.Window('Air Lift Email', layout, icon = 'ico16_1.ico')
        event, values = window.read()
        if event == 'Submit':
            #set variables to values from window
            partNumber = str(values['partNumber'])
            timeFrame = str(values['timeFrame'])
            originalCost = str(values['originalCost'])
            customerCost = str(values['customerCost'])
            #set airLiftEmail to new values
            airLiftEmail = '''Hello!

We are currently still awaiting stock on Model#: ''' + partNumber +'''. We expect this to arrive within the next ''' + timeFrame + '''. I do have them in stock at a 3rd party dropship partner but their price is slightly higher than our price. 

Normally it would cost $''' + originalCost + ''' but I can split that with you and collect only $''' + customerCost + ''' and would have it shipped out to you within 24 hours.

If you would like to go this route we would be able to charge the existing card on file or use another form of payment.

However, if you provide me with your year, make, model and drive type I can look into alternative products that are on par or superior and ready to ship today.

Please let us know how you would like to proceed.

If you have any questions feel free to reach out at <Phone-Number>, I look forward to hearing from you soon!

Thank you,'''
        
        sg.clipboard_set(airLiftEmail)
        emailBody = airLiftEmail
        window.close()
        #created on 12/15/2022 and took 2 hours to make
        #order to reference failure 762845 still can't make it right within 24 hours
        return emailBody
    '''if event == sg.WIN_CLOSED or event == 'Cancel':
        return None'''
            
    return
        
    
    

    
