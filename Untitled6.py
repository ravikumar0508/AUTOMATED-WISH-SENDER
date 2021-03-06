#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import pandas as pd
import smtplib
from email.message import EmailMessage
from getpass import getpass
sender_email =input("enter the email id")
sender_password =getpass("enter your password")
df =pd.read_excel("Greetings needs to send.xlsx")
recievers_email =df["Email ID"].values
sub =("test mail")
attach_file = df["Files_to_be_attached"]
name =df["NAME"].values



zipped = zip(recievers_email,attach_file,name)
for (a,b,c) in zipped:
    msg =EmailMessage()
    files =[(r"Happy.pdf".format(b))]
    for file in files:
        with open (file,'rb') as f:
            file_data =f.read()
            file_name =f.name
        msg['from']=sender_email
        msg['to']=a
        msg['sub']=sub
        msg.set_content(f"hello{c}! I am Wishing You,")
        #msg.add_attachment =(file_data, maintype='application',subtype='octet-stream',filename="{}.pdf")
        
        
    with smtplib.SMTP_SSL('smtp.gmail.com' , 465) as smtp:
        smtp.login(sender_email,sender_password)
        smtp.send_message(msg)
print("All mail sent")

