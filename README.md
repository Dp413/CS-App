
# Customer Service Automation Application.

This app was used to streamline the process of finding
customer information in the web admin or HelpScout 
email system. 

Searches by various fields including:
last name, email, phone number, zip code.
#

Uses Selenium for finding fields and scraping data.
Uses PySimpleGUI for the GUI for inputs/buttons.
Uses OAuth2 for updating Google spreadsheets 
through Google Cloud Platform.

#

On opening the application you will be prompted
with a GUI with an input box and various buttons.
The web browswer will also open to the web admin
page and HelpScout.

#

Once you input the information, click the desired 
button. The information will be passed to the browser
opening the web admin with order information. In
another tab HelpScout will search by order 
number and the customers email.

#

There are other buttons for sending emails,
copying templated emails, submitting sales, 
submitting cancellations, and searching 
distribution centers.
