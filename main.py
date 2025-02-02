import time
import os
from colorama import init, Fore, Style
import pyfiglet
from random import *
import sys

init(convert=True)

def generate_logo():
    logo = pyfiglet.figlet_format("CRACKER")
    return Fore.CYAN + logo

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def animated_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def show_logo():
    clear_screen()
    print(generate_logo())
    animated_text(Fore.GREEN + "Welcome user to the Cracker Tool!")
    animated_text(Fore.LIGHTMAGENTA_EX+"Created by FRn13ds & SALIMxx\n")
    time.sleep(1)

def show_exit_logo():
    clear_screen()
    print(generate_logo())
    animated_text(Fore.RED + "Thank you for using the Cracker Tool! Exiting...")
    time.sleep(2)
    clear_screen()

def show_menu():
    print(Fore.LIGHTBLUE_EX + "="*40)
    print(Fore.YELLOW + "[1] Start Cracking")
    print(Fore.YELLOW + "[2] About this tool")
    print(Fore.YELLOW + "[3] Creators")
    print(Fore.YELLOW + "[4] View Log")
    print(Fore.RED + "[0] Exit")
    print(Fore.LIGHTBLUE_EX + "="*40)

def about_tool():
    animated_text(Fore.YELLOW + "\nAbout this tool:")
    print("This tool simulates cracking a code for educational purposes only.")
    print("The goal is to understand the process of brute-forcing and its challenges.")

def show_creators():
    animated_text(Fore.YELLOW + "\nCreators:")
    print("This tool was created by FRn13ds & SALIMxx. Feel free to contribute!")

def view_log():
    if os.path.exists("crack_log.txt"):
        with open("crack_log.txt", "r") as log_file:
            lines = log_file.readlines()[-10:]
            print(Fore.YELLOW + "\nCrack Log (Last 10 Entries):")
            print("".join(lines))
    else:
        print(Fore.RED + "No log found. Start a cracking process first.")

def cracking_process(code):
    attempts = 0
    animated_text(Fore.YELLOW + "\nStarting the cracking process... Please wait...")
    
    while True:
        x = randint(0, 9999999)
        attempts += 1
        
        if attempts % 100 == 0:
            sys.stdout.write(Fore.GREEN + f"\rAttempt {attempts}: {x}... ")
            sys.stdout.flush()
        
        if x == code:
            print(Fore.GREEN + f"\nSuccess! Cracked code: {x} after {attempts} attempts.")
            with open("crack_log.txt", "a") as log_file:
                log_file.write(f"Cracked Code: {x} in {attempts} attempts\n")
            break

def main():
    show_logo()
    while True:
        show_menu()
        choice = input(Fore.WHITE + "Select an option: ")

        if choice == '1':
            try:
                code = int(input(Fore.WHITE + "Enter the code to crack (0-9999999): "))
                if 0 <= code <= 9999999:
                    cracking_process(code)
                else:
                    print(Fore.RED + "Invalid range! Please enter a number between 0 and 9999999.")
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a numeric code.")
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
        
        time.sleep(2)
        clear_screen()

if __name__ == "__main__":
    main()
