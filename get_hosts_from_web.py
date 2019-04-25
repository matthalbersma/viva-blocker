#! usr/bin/benv python3

import requests


def format(unprocessed):
    return unprocessed.replace('0.0.0.0 ', '*://*./*')

url = 'https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts'
response = requests.get(url)
hosts = [format(line) for line in response.text.splitlines()
         if line.startswith('0.0.0.0 ')]
with open('blocked_domains.js', 'w') as f:
    f.write('var blocked_domains = [\n')
    for host in hosts:
        f.write(f'"{host}",\n')
    f.write('];')
