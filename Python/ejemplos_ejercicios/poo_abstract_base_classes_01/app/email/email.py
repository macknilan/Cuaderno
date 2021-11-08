class Email:
    _host: str
    _username: str
    _password: str

    def __init__(self, host: str, username: str, password: str):
        self._host = host
        self._username = username
        self._password = password

    def send(self,subject:str,body:str)->None:
        self._connect()
        print(self._parseContent(subject,body))
        self._close() 

    def _parseContent(self,subject:str,body:str)->str:
        pass

    def _connect(self)->None:
        pass

    def _close(self)->None:
        pass
