"""
WEB SCRAPING
sys.argv IS THE LIST OF COMMAND-LINE ARGUMENTS.
len(sys.argv) IS THE NUMBER OF COMMAND-LINE ARGUMENTS.
"""
import os
import sys
import requests
import datetime
import pandas as pd

# https://docs.python-requests.org/projects/requests-html/en/latest/index.html
# IT TURNS OUT TO BE A BETTER PACKAGE / WAY TO DO WEB SCRAPING
# BETTER THAN beautifulsoup

from requests_html import HTMLSession

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print(f"BASE_DIR -> {BASE_DIR}")


def url_to_txt(start_year=None, save=True):
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    if start_year == None:
        start_year = year
    assert isinstance(start_year, int)
    assert len(f"{start_year}") == 4
    URL = f"https://www.boxofficemojo.com/year/world/{start_year}"
    session = HTMLSession()
    # r = requests.get(URL)
    r = session.get(URL)
    table_data = []
    header_names = []

    if r.status_code == 200:
        # html_text = r.text
        header_cols = r.html.find("table > tr > th")
        header_names = [x.text for x in header_cols]
        rows = r.html.find("tr")
        for row in rows[1:]:
            # print(row.text)
            row_data = []
            row_dict_data = {}
            std_data_cell = row.find("td")
            # print(f"std_data_cell -> {std_data_cell}")
            # table_data = [stndr.text for stndr in std_data_cell]
            # print(f"table_data -> {table_data}")
            for i, cols in enumerate(std_data_cell):
                # print(i, cols.text, '\n')
                row_data.append(cols.text)
            table_data.append(row_data)

        # print(f"table_data -> {table_data}")
        # print(f"table_data[5] -> {table_data[5]}")
        # print(f"header_names -> {header_names}")
        df = pd.DataFrame(table_data, columns=header_names)
        path = os.path.join(BASE_DIR, "data")
        os.makedirs(path, exist_ok=True)
        filepath = os.path.join("data", f"{datetime.datetime.now()}.csv")
        print(f"filepath -> {filepath}")
        df.to_csv(filepath, index=False)
        return True

        # if save:
        #     with open(f"world-{year}-{month}-{day}.html", "w") as f:
        #         f.write(str(header_names))
        # return header_names


if __name__ == "__main__":
    try:
        start = int(sys.argv[1])
    except:
        start = None

    url_to_txt(start_year=start)

# python3 web_scraping.py 2021
# or
# python3 web_scraping.py
