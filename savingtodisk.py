#!./venv/bin/python
import requests
res = requests.get('https://inventwithpython.com/files/zigzag.py')

try:
    # Check if 200OK, raise exception if not
    res.raise_for_status()
    playFile = open('zigzag.txt', 'wb')

    for chunk in res.iter_content(10000):
        playFile.write(chunk)

    playFile.close()
    print(f'Done writing data...')

except Exception as exc:
    # Print a verbose message, if there was an exception
    print(f'There was an error retrieving the page: {exc}')
