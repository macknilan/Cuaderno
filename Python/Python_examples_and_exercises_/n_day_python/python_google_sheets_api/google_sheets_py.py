from pprint import pprint

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

sheet = client.open("my_datasample_airports").worksheet("Hoja 1")  # Open the spreadhseet


# data = sheet.get_all_records()  # Get a list of all records

cell = sheet.cell(3, 3)  # Get a specific row

# col = sheet.col_values(3)  # Get a specific column
# cell = sheet.cell(1, 2).value  # Get the value of a specific cell
#
# insertRow = ["hello", 5, "red", "blue"]
# sheet.add_rows(insertRow, 4)  # Insert the list as a row at index 4
#
# sheet.update_cell(2, 2, "CHANGED")  # Update one cell
#
# numRows = sheet.row_count  # Get the number of rows in the sheet

# pprint(data)
pprint(cell)
