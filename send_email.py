import smtplib, ssl
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def send_email(mesg):
    host = "smtp.gmail.com"
    port = 465

    password = os.getenv("PASSWORD")
    username = "edrenaline0@gmail.com"

    receiver = "mohammad.khan06@northsouth.edu"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, mesg)


