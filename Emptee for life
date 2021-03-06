/// Python code for sending a post request very fast to the website manually ///

import requests
import hashlib

URI = "http://165.22.124.155:32010"
PROXIES = {} # {'http':'http://127.0.0.1:8080'}

def get_and_hash(ret):
    begin = ret.find("<h3 align='center'>") + 19
    end = ret.find("</h3>")
    md5_string = ret[begin:end].encode('utf-8')
    digest = hashlib.md5(md5_string).hexdigest()
    return digest

session = requests.Session()
req = session.get(URI, proxies=PROXIES)
md5 = get_and_hash(req.text)
req = session.post(URI, data={"hash":md5}, proxies=PROXIES)
print(req.text)
