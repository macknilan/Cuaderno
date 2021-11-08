from app.email.email import Email

class Gmail(Email):

    def __init__(self, host: str, username: str, password: str):
        Email.__init__(self,host,username,password)

    def _parseContent(self,subject:str,body:str)->str:
        return f"""
            <html>
            <head>
                <title>{subject}</title>
            </head>
            <body>
                {body}
            </body>
            </html>
        """

    def _connect(self)->None:
        print(f"connecting to google --> {self._host}/{self._username}:{self._password}")

    def _close(self)->None:
        print(f"closing connection to google")