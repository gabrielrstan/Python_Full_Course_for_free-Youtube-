import smtplib

sender = "sender@gmail.com"
receiver = "receiver@gmail.com"
password = "password123"
subject = "Python email test"
body = "I wrote an email"

#header
message = f"""From: Soop Dog{sender}
To: Nicolas Cage{receiver}
Subject: {subject}\n
{body}
"""

#server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
try:
    server.login(sender, password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been send")

except smtplib.SMTPAuthenticationError:
    print("Unable to sign in")