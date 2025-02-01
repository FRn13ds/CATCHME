import time
import os
from colorama import *
import pyfiglet
from random import *
import sys

init(autoreset=True)


def generate_logo():
    logo = pyfiglet.figlet_format("CRACKER")
    return Fore.CYAN + logo

menu_list = ''' [1] Start Cracking
[2] About this tool
[3] Creators
[4] View Log
[0] Exit
'''

def clear_screen():
    """Clear the screen in a platform-independent way."""
    if os.name == 'nt':
        os.system('cls')
    else:  
        os.system('clear')

def show_logo():
    print(generate_logo())
    print(Fore.GREEN + "Welcome user to this tool!")
    print(Fore.LIGHTMAGENTA_EX+"                      CREATED BY FRn13ds & SALIMxx")

def show_exit_logo():
    print(generate_logo())
    print(Fore.RED + "Thank you for using the Cracker Tool! Exiting...")

def show_menu():
    print(Fore.LIGHTBLUE_EX + menu_list)

def about_tool():
    print(Fore.YELLOW + "\nAbout this tool:")
    print("This tool simulates cracking a code for educational purposes only.")
    print("The goal is to understand the process of brute-forcing and how long it could take.")

def show_creators():
    print(Fore.YELLOW + "\nCreators:")
    print("This tool was created by FRn13ds. Feel free to contribute or make improvements!")

def view_log():
    if os.path.exists("crack_log.txt"):
        with open("crack_log.txt", "r") as log_file:
            print(Fore.YELLOW + "\nCrack Log:")
            print(log_file.read())
    else:
        print(Fore.RED + "No log found. Start a cracking process first.")

def cracking_process(code):
    attempts = 0
    x = randint(0, 9999999)
    print(Fore.YELLOW + "\nStarting the cracking process... This may take a while...")
    
    while True:
        x = randint(0, 9999999)  
        attempts += 1
        if attempts % 100 == 0:  
            sys.stdout.write(Fore.GREEN + f"\rAttempt {attempts}: {x}")
            sys.stdout.flush()
        
        if x == code:
            print(Fore.GREEN + f"\nSuccess! Cracked code: {x} after {attempts} attempts.")
            with open("crack_log.txt", "a") as log_file:
                log_file.write(f"Cracked Code: {x} in {attempts} attempts\n")
            break

def main():
    show_logo()
    time.sleep(2)
    clear_screen()
    
    while True:
        show_menu()
        choice = input(Fore.WHITE + "Select an option: ")

        if choice == '1':
            try:
                code = int(input(Fore.WHITE + "Enter the code to crack (only numbers): "))
                if code < 0 or code > 9999999:
                    print(Fore.RED + "Please enter a code between 0 and 9999999.")
                    continue
                cracking_process(code)
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a number.")
        elif choice == '2':
            about_tool()
        elif choice == '3':
            show_creators()
        elif choice == '4':
            view_log()
        elif choice == '0':
            show_exit_logo()
            break
        else:
            print(Fore.RED + "Invalid option. Please try again.")
        
        time.sleep(1)
        clear_screen()

if __name__ == "__main__":
    main()

