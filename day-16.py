#day-16
'''
SMPT(simle mail transafe protocol
----------------------------------
-->this is use to send emails from server to another...
note:
-----
1.SMTP SSL Port
---------------
465

2.SMTP TLS Port
---------------
587

import smtplib

emailmessage class
------------------

msg['subject'] = 'SMPT ON Mail'
msg['from] = 'sender@mail.com'
msg['to'] = receiver@gmail.com    
    

import smtplib
from email.message import EmailMessage
sender = 'bibhutipanigrahi731@gmail.com'
password = 'ejgkdzdrxgwzvteq'
msg = EmailMessage()
msg['Subject'] = 'Welcome Mail'
msg['From'] = sender
msg['To'] = 'rohansai4645@gmail.com'
msg.set_content('Your Account has been credited with Rs.75,000')
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
server.send_message(msg)
server.quit()

'''


























































