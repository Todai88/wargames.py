import requests, binascii, base64, re
from requests.auth import HTTPBasicAuth

def pattern_lookup(line):
    """
    Will iterate through lines
    to find a matching string that
    is 32 characters long and only
    holds alphanumerical characters.
    -----
    :param lines: The lines to be iterated.
    :return: The line holding the matched string,
             or None if not found
    """
    pattern = re.compile("^([A-Za-z0-9]{32})$")
    print(line)
    if pattern.match(line):
        return line
    else:
        return None

def get_secret(host, credentials):
    """
    Grabs the hint(flag) from the 
    host by splitting the response on
    semicolon (;) then performing
    pattern matching using regex.
    ----
    :param host: The host we are sending 
                 requests to.
    :param credentials: The credentials required
                        to sign into the host.
    :return: The hex encoded secret.
    """
    try:
        response = requests.get(host, auth=HTTPBasicAuth(*credentials))
        response_lines = response.content.decode('ascii').replace('"', '').split(';')
        return next((line
                 for line in response_lines
                 if pattern_lookup(line)),
                None)
    except requests.RequestException as e:
        print(e)

def prepare_payload(secret):
    decoded_secret = base64.b64decode(binascii.unhexlify(secret)[::-1])
    payload = {'secret': decoded_secret, 'submit': 'placeholder'}
    return payload

def get_password(host, credentials, secret):
    """
    Uses a post-request injected with the 
    reverse engineered secret to get access
    to the password to natas9.
    :param host: The host that holds the 
                 password.
    :param credentials: 
    :param decoded_hint: 
    :return: The password to Natas9
    """
    payload = prepare_payload(secret)
    try:
        response = requests.post(host, auth=HTTPBasicAuth(*credentials), data=payload)
        response_lines = response.content.decode('utf-8').split(' ')
        return next((line
                     for line in response_lines
                     if pattern_lookup(line.strip())),
                    None)
    except requests.RequestException as e:
        print(e)


def main():
    host = 'http://natas8.natas.labs.overthewire.org/index-source.html'
    credentials = ['natas8', 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe']
    secret = get_secret(host, credentials)
    print(get_password(host.split('index')[0], credentials, secret))

if __name__ == '__main__':
    main()