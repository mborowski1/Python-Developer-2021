import requests

r = requests.get('https://www.onet.pl')
print(r.status_code)
