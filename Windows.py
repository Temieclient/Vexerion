import time
import os
import requests

def cls():
    os.system("cls")
print("""
████████████████████████████████████████████████
█▄─█─▄█▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄█─▄▄─█▄─▀█▄─▄█
██▄▀▄███─▄█▀██▀─▀███─▄█▀██─▄─▄██─██─██─██─█▄▀─██
▀▀▀▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▄▀▄▄▄▀▀▄▄▀""")
print("STARTING THIS WILL MAY TAKE A BIT")
time.sleep(5)
cls()
print("CHECKING SPECS")
time.sleep(2)
print("COMPUTER MEETS SPECS")
time.sleep(5)
cls()
print("CHECKING IF THIS VERSION IS UP TO DATE.")


def check_pastebin_variable(pastebin_link, variable):
    response = requests.get(pastebin_link)
    content = response.text.strip()

    if content == variable:
        print("VERSION IS UP-TO-DATE")
    else:
        print("VERSION IS NOT UP-TO-DATE UPDATE AVAIBLE")
        print("NEW VERSION " + content)

# Example usage
pastebin_link = "https://pastebin.com/raw/dvQCGQPs"  # Replace with your Pastebin link
variable = "1.0.0"  # Replace with your variable

check_pastebin_variable(pastebin_link, variable)
cls()
time.sleep(2)
print("COULDNT FIND GAME.")