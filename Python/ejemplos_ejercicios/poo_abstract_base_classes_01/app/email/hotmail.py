from app.email.email import Email
import base64
import json


class Hotmail(Email):
    def __init__(self, host: str, username: str, password: str):
        Email.__init__(self, host, username, password)

    def _parseContent(self, subject: str, body: str) -> str:
        output = {"subject": subject, "body": body}
        return json.dumps(output)

    def __encodeConnection(self, connection: str) -> str:
        connectionAscii = connection.encode("ascii")
        return base64.b64encode(connectionAscii).decode("ascii")

    def _connect(self) -> None:
        connectionEncoded = self.__encodeConnection(
            f"{self._host}/{self._username}:{self._password}"
        )
        print(f"connecting to hotmail -->{connectionEncoded}")

    def _close(self) -> None:
        print(f"closing connection to hotmail")
