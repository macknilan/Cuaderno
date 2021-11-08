
from app.email.gmail import Gmail
from app.email.hotmail import Hotmail

gmail = Gmail("smtp.google.com","user123","pass123")
gmail.send("Hello","World")

print()

hotmail = Hotmail("smtp.microsoft.com","user123","pass123")
hotmail.send("Hello","World")
