import random
import string
from colorama import Fore, Style

def banner():
    banner = r"""
  _________       _____     __________                                               .___
 /   _____/____ _/ ____\____\______   \_____    ______ ________  _  _____________  __| _/
 \_____  \\__  \\   __\/ __ \|     ___/\__  \  /  ___//  ___/\ \/ \/ /  _ \_  __ \/ __ | 
 /        \/ __ \|  | \  ___/|    |     / __ \_\___ \ \___ \  \     (  <_> )  | \/ /_/ | 
/_______  (____  /__|  \___  >____|    (____  /____  >____  >  \/\_/ \____/|__|  \____ | 
        \/     \/          \/               \/     \/     \/                          \/ 
                                                                            By XenoCode.
Write your password length.
"""
    print(Fore.BLUE + banner)

def createPassword(password):
    if len(password) <= 8:
        print(f'[*][WEAK] {Fore.GREEN}{password}{Style.RESET_ALL}')
    elif len(password) <= 11:
        print(f'[*][MEDIUM] {Fore.GREEN}{password}{Style.RESET_ALL}')
    elif len(password) <= 15:
        print(f'[*][STRONG] {Fore.GREEN}{password}{Style.RESET_ALL}')
    else:
        print(f'[*][VERY STRONG] {Fore.GREEN}{password}{Style.RESET_ALL}')


if __name__ == '__main__':
    banner()
    try:
        while True:
            userInput = int(input('> '))

            if userInput <= 0:
                 print(f"{Fore.RED}Please enter a number greater than 0{Style.RESET_ALL}")
                 continue
            break

        caracteres = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(caracteres) for i in range(userInput))
        createPassword(password)
    except Exception as e:
        print(f"{Fore.RED}Please enter only numbers: {e}{Style.RESET_ALL}")
        exit()
