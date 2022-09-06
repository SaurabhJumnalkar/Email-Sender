from email.message import EmailMessage
from password import v
import ssl
import smtplib



email_sender=''  #Enter your mail id in email_sender
email_password=v 

email_receiver=''  #Enter receiver's mail id
subject="Hello People"  # This will be Subject
#This is Body of mail
body=""""               
Mail is sent by python program,Have a nice day!
"""

em=EmailMessage()   #Created instance of EmailMessage
em['From']=email_sender
em['To']=email_receiver
em['subject']=subject
em.set_content(body)

context=ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)  #Login as per sender
    smtp.sendmail(email_sender,email_receiver,em.as_string()) # Mail is sent from here


