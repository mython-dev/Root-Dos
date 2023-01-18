# //Code by: myth-dev
# //Instagram: @thehackerworld_ or @mython_dev
# //Telegram: @myth_dev
# //Github: https://githun.com/mython-dev

import os
import sys
import time
from sys import stdout

class Fragments():

    red="\033[0;31m"
    yellow="\033[0;33m"
    blue="\033[0;34m"
    purple="\033[0;35m"
    cyan="\033[0;36m"
    white="\033[0;37m"
    nc="\033[00m"

    success = f"{yellow}[{white}√{yellow}] {nc}"
    error  =    f"{blue}[{white}!{blue}] {red}"
    info  =   f"{yellow}[{white}+{yellow}] {cyan}"
    info2  =   f"{nc}[{white}•{nc}] {purple}"
    ask  =     f"{nc}[{white}?{nc}] {yellow}"


class Functions(Fragments):

    def __init__(self):
        Fragments.__init__(self)
        

    def clear(self):
        os.system('clear')


    def check_root(self):
        if  os.geteuid() != 0:
            print(f'{Fragments.error}Please run: sudo python3 attack.py\n')
            sys.exit(1)

    def check_os(self):
        if sys.platform == 'windows'.lower():
            print(f'{Fragments.error}This script only for: Mac os && Linux\n')

    def sprint(text, second=0.03):
        for line in text + '\n':
            stdout.write(line)
            stdout.flush()
            time.sleep(second)


class Banner(Fragments):

    def __init__(self):
        Fragments.__init__(self)
        
    def menu(self):

        banner = f'''
_______________________________________________________________
     _____             _          _____  _____            
    |  __ \           | |        |  __ \|  __ \           
    | |__) |___   ___ | |_ ______| |  | | |  | | ___  ___ 
    |  _  // _ \ / _ \| __|______| |  | | |  | |/ _ \/ __|
    | | \ \ (_) | (_) | |_       | |__| | |__| | (_) \__ |
    |_|  \_\___/ \___/ \__|      |_____/|_____/ \___/|___/
    
                    VerSion Tool: v1.0

    // Code by: Myth-dev
    // GitHub: @mython-dev
    // Telegram: @myth_dev
    // Instagram: thehackerworld_
_______________________________________________________________
        '''  


        print(banner)

class WhatLayers(Fragments):

        def __init__(self):
            Fragments.__init__(self)
            
        def what_means_layer(self):

            print(f'''\n{self.info}Layer 7\n
            {self.nc}\tA layer 7 DDoS attack is a DDoS attack that sends HTTP/S traffic to consume 
            \tresources and hamper a website's ability to delivery content or to harm the owner of 
            \tthe site. The Web Application Firewall (WAF) service can protect layer 7 HTTP-based 
            \tresources from layer 7 DDoS and other web application attack vectors.   
            
{self.info}Layer 4\n
            {self.nc}\tLayer 4 of the OSI model, also known as the transport layer, manages network traffic 
            \tbetween hosts and end systems to ensure complete data transfers. Transport-layer 
            \tprotocols such as TCP, UDP, DCCP, and SCTP are used to control the volume of data, 
            \twhere it is sent, and at what rate.\n''')