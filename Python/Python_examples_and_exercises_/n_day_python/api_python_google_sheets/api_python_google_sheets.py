from pprint import pprint
from google.oauth2 import service_account
from googleapiclient.discovery import build

SERVICE_ACCOUNT_FILE = "keys.json"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1bLKddg9AdJh7cDEHG7i9NDj6NkmJCSIuVQC0ey5pV4k"
# SAMPLE_RANGE_NAME = "Class Data!A2:E"


service = build("sheets", "v4", credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Hoja 1!A2:L2").execute()

values = result.get("values", [])

pprint(f"values ---> {values}")
