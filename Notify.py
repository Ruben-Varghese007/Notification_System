from winotify import Notification,audio
import smtplib
from email.message import EmailMessage

def notifyMe(name,message):
    toast = Notification(app_id="Windows App",
                         title="New Notification!",
                         msg=message,
                         icon="file_location")
    toast.set_audio(audio.Default,loop = False)
    toast.show()

def email_alert(subject,body,to):

    text=EmailMessage()
    text.set_content(body)
    text['subject'] = subject
    text['to'] = to

    user = "emailnotifyalert01@gmail.com"
    text['from'] = user
    password = "jaltgizkhiopendv"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user,password)
    server.send_message(text)
    server.quit()

def main():

    name = input("Enter your name : ")
    email = input("Enter your mail id : ")
    message = "Hey "+name+" Take a Break !\nAn Email has been sent to : \n"+email
    notifyMe(name,message)
    email_alert("Heavy Usage Warning !","You have been using this device for more than 3 hours.\nPlease Take a Break !",email)
    print("Email sent Successfully")

main()
