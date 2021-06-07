import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Create a secure SSL context
context = ssl.create_default_context()

# environment variables
username = "la.bodega.services@gmail.com"
password = "kxbemfbutkmmefkt"


def send_mail(
    text="Email Body, part of the body mail.",
    subject="Hello World.",
    from_email="Testing send email <mack@gmail.com>",
    to_emails=None,
    html=None,
):
    assert isinstance(to_emails, list)
    msg = MIMEMultipart("alternative")
    msg["From"] = from_email
    msg["To"] = ", ".join(to_emails)
    msg["Subject"] = subject
    txt_part = MIMEText(text, "plain")
    msg.attach(txt_part)
    if html != None:
        html_part = MIMEText(html, "html")
        msg.attach(html_part)
    msg_str = msg.as_string()
    # login to my smtp server
    server = smtplib.SMTP(host="smtp.gmail.com", port=587)
    server.ehlo()
    server.starttls(context=context)
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)
    server.quit()

# python3 -i send_mail.py
# send_mail(to_emails=['la.bodega.services@gmail.com'])
