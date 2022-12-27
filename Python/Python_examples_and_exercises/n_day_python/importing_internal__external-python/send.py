import sys
from datetime import datetime

import requests
from formatting import format_msg

"""
sys.argv IS THE LIST OF COMMAND-LINE ARGUMENTS.
len(sys.argv) IS THE NUMBER OF COMMAND-LINE ARGUMENTS.
"""


def send(name, website=None, verbose=False):
    if website != None:
        msg = format_msg(my_name=name, my_website=website)
    else:
        msg = format_msg(my_name=name)
    if verbose:
        print(name, website)
    # send the message
    r = requests.get("http://httpbin.org/json")
    if r.status_code == 200:
        return r.json()
    else:
        return "There was an error"


if __name__ == "__main__":
    print(sys.argv)  # PRINT ALL ARGUMENTS PASSED
    name = "Unknown"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    response = send(name, verbose=True)
    print(response)

# OUTPUT
""" ['send.py']
Unknown None
{
    'slideshow': {
        'author': 'Yours Truly',
        'date': 'date of publication',
        'slides': [
            {
                'title': 'Wake up to WonderWidgets!',
                'type': 'all'
            },
            {
                'items':[
                    'Why <em>WonderWidgets</em> are great',
                    'Who <em>buys</em> WonderWidgets'
                    ],
                    'title': 'Overview',
                    'type': 'all'
            }
        ],
        'title':
        'Sample Slide Show'
    }
} """
