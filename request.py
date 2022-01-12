#!/usr/bin/python

import requests

res = requests.get('https://inventwithpython.com/page_that_doesnt_exist')

try:
    res.raise_for_status()
except Exception as exc:
    print(f'There was a priblem opening the page: {exc}')
