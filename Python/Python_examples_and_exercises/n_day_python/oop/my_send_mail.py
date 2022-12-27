import os
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(FILE_PATH)
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

# Create a secure SSL context
CONTEXT = ssl.create_default_context()

# ENVIRONMENT VARIABLES
USERNAME = ""
PASSWORD = ""


class Emailer:
    """DOCSTRING"""

    # FOR THE TEMPLATE PART
    template_name = ""
    context = None

    def __init__(
        self,
        to_emails,
        subject,
        # body_text,
        from_email,
        html,
        template_name="",
        context=None,
        *args,
        **kwargs,
    ):
        """Constructor ..."""
        self.to_emails = to_emails
        self.subject = subject
        # self.body_text = body_text
        self.from_email = from_email
        self.html = html
        # self.template_name = template_name
        self.context = context

    def get_template(self):
        """FUNCTION THAT IS RESPONSIBLE FOR FINDING THE TEMPLATE AND READING IT"""
        if self.html == True:
            print(f"ES self.html -> {self.html}")
            template_path = os.path.join(TEMPLATE_DIR, "hello.html")
        elif self.html == False:
            print(f"ES self.html -> {self.html}")
            template_path = os.path.join(TEMPLATE_DIR, "hello.txt")
        else:
            print(f"ES self.html -> {self.html}")
            template_path = os.path.join(TEMPLATE_DIR, "hello.html")
        # print(f'template_path -> {template_path}')
        # print(f'self.template_name -> {self.template_name}')
        if not os.path.exists(template_path):
            raise Exception("This path does not exist")
        template_string = ""
        with open(template_path, "r") as f:
            template_string = f.read()
        # print(f'template_string -> {template_string}')
        return template_string

    def render(self, context=None):
        """
        FUNCTION THAT IS RESPONSABLE FOR MAKE THE
        RENDER FOR THE TEMPLATE WITH THE INFO OF THE
        DICCIONARY PASSED IN CONTEXT
        """
        render_ctx = context
        # print(f'render_ctx -> {render_ctx}')
        if self.context != None:
            render_ctx = self.context
            # print(f'render_ctx -> {render_ctx}')
        if not isinstance(render_ctx, dict):  # MAKE SURE THAT IS A DICTIONARY
            render_ctx = {}
        template_string = self.get_template()
        # print(f'template_string -> {template_string}')
        return template_string.format(**render_ctx)

    def format_msg(self):
        msg_render = self.render()
        assert isinstance(self.to_emails, list)
        msg = MIMEMultipart("alternative")
        msg["From"] = self.from_email
        msg["To"] = ", ".join(self.to_emails)
        msg["Subject"] = self.subject
        if self.html == True:
            html_part = MIMEText(msg_render, "html")
            msg.attach(html_part)
        elif self.html == False:
            txt_part = MIMEText(msg_render, "plain")
            msg.attach(txt_part)
        else:
            html_part = MIMEText(msg_render, "html")
            msg.attach(html_part)

        # txt_part = MIMEText(self.context, "plain")
        # msg.attach(txt_part)
        # if self.html != None:
        #     html_part = MIMEText(self.html, "html")
        #     msg.attach(html_part)
        msg_str = msg.as_string()
        return msg_str

    def send(self):
        """LOGIN TO MY SMTP SERVER"""
        msg_str_format = self.format_msg()
        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        server.ehlo()
        server.starttls(context=CONTEXT)
        server.login(USERNAME, PASSWORD)
        try:
            server.sendmail(self.from_email, self.to_emails, msg_str_format)
            did_send = True
        except:
            did_send = False
        server.quit()
        return did_send


# python3 -i send_mail.py
# send_mail(to_emails=['la.bodega.services@gmail.com'])


# python3 -i send_mail.py
# obj = Emailer(to_emails=["la.bodega.services@gmail.com"], subject="Hello World.", body_text="Email Body, part of the body mail.", from_email="Testing send email <mack@gmail.com>", html=None, template_name='hello.txt', context={'name': 'Mack'})
# obj = Emailer(to_emails=["la.bodega.services@gmail.com"], subject="Hello World.", from_email="Testing send email <mack@gmail.com>", html=True, context={'name': 'Mack', 'body_text': 'Texto dinamico'})
# obj.send()
