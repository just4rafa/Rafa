from email import message
import smtplib
import ssl
from email.message import EmailMessage

from matplotlib.style import context

subject = "Email from Python"
body = input("Enter the text: ")
sender_email = "rafajust4@gmail.com"
receiver_email = "rafajust4@gmail.com"
password = "123e321e"

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

print("Sending Email!")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    
print("Succes!")
    