#!./venv/bin/python

import requests, bs4

res = requests.get('https://nostarch.com')

try:
    res.raise_for_status()

    # bs4 function needs to be called with string (res.text) containing the HTML it will parse.
    # html.parser here is a parser built in w/ python. Alternative is lxml.
    noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')

    # this will return a BeautifulSoup object
    print(type(noStarchSoup))

    # selects all elements named 'article' with class field-name-field-author
    authors = noStarchSoup.select('article > .field-name-field-author')

    # this returns a bs4 ResultSet object
    print(type(authors))

    # prints out the text/name(ONLY) of the author at the 3rd index
    # without getText() it shows the result, complete with tags/elements/class etc
    print(authors[3].getText())


except Exception as exc:
    print(f'There was an error: {exc}')
