import random
import sys
import colorama
from colorama import *
from colorama import init
init()



def generate_1():
  chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
  for i in range(1):
    first = ''.join((random.choice(chars) for i in range (4)))
    second = ''.join((random.choice(chars) for i in range (4)))
    third = ''.join((random.choice(chars) for i in range (4)))

    result = first + '-' + second + '-' + third

    print(result)

def generate_2():
  chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
  for i in range(5):
    first = ''.join((random.choice(chars) for i in range (4)))
    second = ''.join((random.choice(chars) for i in range (4)))
    third = ''.join((random.choice(chars) for i in range (4)))

    result = first + '-' + second + '-' + third
    print(result)

def generate_3():
  chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
  for i in range(10):
    first = ''.join((random.choice(chars) for i in range (4)))
    second = ''.join((random.choice(chars) for i in range (4)))
    third = ''.join((random.choice(chars) for i in range (4)))

    result = first + '-' + second + '-' + third
    print(result)

def generate_4():
  chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
  for i in range(20):
    first = ''.join((random.choice(chars) for i in range (4)))
    second = ''.join((random.choice(chars) for i in range (4)))
    third = ''.join((random.choice(chars) for i in range (4)))

    result = first + '-' + second + '-' + third
    print(result)

def generate_5():
  chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
  for i in range(50):
    first = ''.join((random.choice(chars) for i in range (4)))
    second = ''.join((random.choice(chars) for i in range (4)))
    third = ''.join((random.choice(chars) for i in range (4)))

    result = first + '-' + second + '-' + third
    print(result)

def generate_6():
  chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
  for i in range(500):
    first = ''.join((random.choice(chars) for i in range (4)))
    second = ''.join((random.choice(chars) for i in range (4)))
    third = ''.join((random.choice(chars) for i in range (4)))
    third1 = ''.join((random.choice(chars) for i in range (4)))

    result = first + '-' + second + '-' + third + '-' + third1

    print(result)





print(Fore.RED + """

 ██▓     ██▓ ▄████▄    ▄████ ▓█████  ███▄    █ 
▓██▒    ▓██▒▒██▀ ▀█   ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
▒██░    ▒██▒▒▓█    ▄ ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
▒██░    ░██░▒▓▓▄ ▄██▒░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
░██████▒░██░▒ ▓███▀ ░░▒▓███▀▒░▒████▒▒██░   ▓██░
░ ▒░▓  ░░▓  ░ ░▒ ▒  ░ ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
░ ░ ▒  ░ ▒ ░  ░  ▒     ░   ░  ░ ░  ░░ ░░   ░ ▒░
  ░ ░    ▒ ░░        ░ ░   ░    ░      ░   ░ ░ 
    ░  ░ ░  ░ ░            ░    ░  ░         ░ 
            ░  

            Generate Random License Keys With PYTHON
############################
GitHub: github.com/WooxHimself
############################
            
            """)

print(Style.RESET_ALL + "How many keys you would like to generate? ")
print(Fore.CYAN + Style.RESET_ALL + " 1 | 1 Key")
print(Fore.CYAN + Style.RESET_ALL + " 2 | 5 Keys")
print(Fore.CYAN + Style.RESET_ALL + " 3 | 10 Keys")
print(Fore.CYAN + Style.RESET_ALL + " 4 | 20 Keys")
print(Fore.CYAN + Style.RESET_ALL + " 5 | 50 Keys")
print(" 6 | 500 Keys")

choice = input("Enter number (1-6): ")





input ("Press ENTER to start ")

if choice == '1':
    generate_1()

elif choice == '2':
    generate_2()

elif choice == '3':
    generate_3()

elif choice == '4':
    generate_4()

elif choice == '5':
    generate_5()

elif choice == '6':
    generate_6()




