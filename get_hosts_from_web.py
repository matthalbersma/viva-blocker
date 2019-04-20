#! usr/bin/benv python3

import requests
import subprocess

url = "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"

response = requests.get(url)

with open("hosts", "w") as out_file:
    for line in response.text:
        out_file.write(line)

out_file.close()

print("Start shell script")
subprocess.call("./convert_hosts.sh")
print("Shell script finished")


