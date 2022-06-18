import smtplib, ssl
import os
from dotenv import load_dotenv

load_dotenv()

MY_ENV_VAR = os.getenv('MY_ENV_VAR')
def send_mail(self):
        port = os.getenv("port")  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = os.getenv("sender_email") # Enter your address
        receiver_email = self.email # Enter receiver address
        password = os.getenv("password")
        message = """\
        Subject: Hi there

        You are successfully registered to Insight Workshop Academy Program."""

        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
        except Exception as e :
            raise Exception("Invalid Email address")
            
        