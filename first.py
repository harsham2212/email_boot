import smtplib
import speech_recognition as harsh
import pyttsx3
from call_me_authentication import *
from email.message import EmailMessage

listener = harsh.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()
    password = password_provider()


def get_info():
    try:
        with harsh.Microphone() as source:
            print('Listeining...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('hrshsingh00@gmail.com', password_provider())
    email = EmailMessage()
    email['From'] = 'hrshsingh00@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
    server.sendmail('hrshsingh00@gmail.com',
                    'gauravtriyar27@gmail.com',
                    'hey, i am creating email bot in python')


Email_list = {
    'abhishek': 'abhsiehkfbg08@gmail.com',
    'harsh': 'kmrharsh50@gmail.com',
    'gaurav': 'gauravtriyar27@gmail.com'
}


def get_email_info():
    talk('to whom want to send email')
    name = get_info()
    receiver = Email_list[name]
    print(receiver)
    talk('what is the subject of email')
    subject = get_info()
    talk('Tell me the motive of email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('hey! email sent successfully')
    talk('Do you want send more email')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()
