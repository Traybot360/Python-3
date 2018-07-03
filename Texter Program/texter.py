import smtplib

to = input("Who is this to ??")
user_number = input("Who is this from")
carrier  = input("what is the carier of the person : bell, telus,koodo,virgin,rogers ")
'''
contacts = ["None lul"]
print("These are ur preset contacts ")
for i in range(len(contacts)):
    print(contacts[i])
if(user_email == "1"):
    y_n = input("Add a new contact? y/n")
    if(y_n == "y"):
        new_contact = input("name and email")
        contacts.append(new_contact) 
'''
if(carrier == "bell"):
    to = to +"@txt.bell.ca"
elif (carrier == "telus" or carrier == "koodo"):
    to = to +"@msg.telus.com"
elif(carrier == "virgin"):
    to = to+"@vmobl.com"
elif(carrier == "rogers"):
    to = to+"@rogers.sms.com"
content = input("what do you want to text?")

mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()

mail.login(user_number,input("Whats ur password"))

mail.sendmail(user_number,to,content)

mail.close()
print("text sent")
#make a contacts list and to be able to add contacts 
