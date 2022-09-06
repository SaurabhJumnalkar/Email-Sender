from email.message import EmailMessage
from password import v
import ssl
import smtplib



email_sender='saurabhjum@gmail.com'
email_password=v

email_receiver='kediv53724@oncebar.com'
subject="Hello People"
body=""""
Mail is sent by python program,Have a nice day!
"""

em=EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['subject']=subject
em.set_content(body)

context=ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())



