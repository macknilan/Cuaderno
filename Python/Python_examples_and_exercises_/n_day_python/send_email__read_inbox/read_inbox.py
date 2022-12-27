import email
import imaplib  # https://docs.python.org/3/library/imaplib.html

# environment variables
host = "imap.gmail.com"
username = "la.bodega.services@gmail.com"
password = ""


def get_inbox():
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select("inbox")
    _, search_data = mail.search(None, "UNSEEN")
    my_message = []
    for e in search_data[0].split():
        email_data = {}
        _, data = mail.fetch(e, "(RFC822)")
        _, b = data[0]
        # https://docs.python.org/3/library/email.parser.html
        email_message = email.message_from_bytes(b)
        for header in ["subject", "to", "from", "date"]:
            print("{}: {}".format(header, email_message[header]))
            email_data[header] = email_message[header]
        for part in email_message.walk():  # https://docs.python.org/3.9/library/email.message.html
            # print(f' -> {part}')
            if part.get_content_type() == "text/plain":  # https://docs.python.org/3.9/library/email.message.html
                body = part.get_payload(decode=True)
                email_data["body"] = body.decode()
            elif part.get_content_type() == "text/html":
                html_body = part.get_payload(decode=True)
                email_data["html_body"] = html_body.decode()
        my_message.append(email_data)
        return my_message

    mail.close()
    mail.logout()


if __name__ == "__main__":
    my_inbox = get_inbox()
    print(my_inbox)
