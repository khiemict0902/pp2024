#!/usr/bin/python3

import subprocess
while True:
    command = str(input("~$ "))

    if command == "exit":
        exit()

    subprocess.run(command)
