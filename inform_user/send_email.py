import re
import os
from dotenv import load_dotenv
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def email_is_valid(email):
    if re.search(r"^[\w+\.]+@([\w+]+\.)+[\w+]{2,4}$", email, re.IGNORECASE):
        return True
    else:
        return False

def get_recipient_email():
    while True:
        email = input("Type in your email to which you'd like to receive notifications: ")
        if email_is_valid(email):
            return email
        else:
            print("Incorrect email format, try again")

def record_email(email, file_path):
    with open(file_path, "w") as file:
        file.write(email)

def set_email(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            email = file.read()
            if email_is_valid(email):
                print(f"Email is {email}")
                return email
            else:
                print("Recorded email in invalid format. Input a correct email")
                email = get_recipient_email()
    else:
        print("There is no recorder email.")
        email = get_recipient_email()
    record_email(email, file_path)
    return email

def send_email(recipient_email, subject, message ):
    load_dotenv()
    sender_email = os.environ.get('EMAIL_TURING')
    password = os.environ.get('WUPHF_PASSWORD')
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context()) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        print(f"The email was sent to {recipient_email}")
    except Exception as e:
        print("Error: Incorrect sender's email account credentials.")

