import os
import subprocess
import time
import requests
from colorama import Fore, init
init(autoreset=True)

# Colors
R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
B = Fore.BLUE
C = Fore.CYAN
W = Fore.WHITE

# Banner
def banner():
    os.system("clear")
    print(f"""{R}
███████╗ ██████╗ ██████╗ ██╗    ██╗ █████╗ ██████╗ ███████╗
██╔════╝██╔════╝██╔═══██╗██║    ██║██╔══██╗██╔══██╗██╔════╝
█████╗  ██║     ██║   ██║██║ █╗ ██║███████║██║  ██║█████╗  
██╔══╝  ██║     ██║   ██║██║███╗██║██╔══██║██║  ██║██╔══╝  
██║     ╚██████╗╚██████╔╝╚███╔███╔╝██║  ██║██████╔╝███████╗
╚═╝      ╚═════╝ ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝
    {W}
    {G}Made by AllahAkbar313{W}
    """)
    print(f"{G}Welcome to ForwarderBot!{W}")
    print(f"{Y}This tool forwards incoming SMS to Termux in real-time.{W}")
    print(f"{R}⚠ WARNING: This could be illegal! Use only for educational purposes! ⚠{W}")
    print("\n")

# Get Phone Number
def get_phone_number():
    while True:
        number = input(f"{C}Enter the phone number to track (or type 'exit' to quit): {W}")
        if number.lower() == "exit":
            print(f"{R}Exiting...{W}")
            exit()
        elif number.isdigit() and len(number) >= 8:  # Basic validation
            return number
        else:
            print(f"{R}Invalid number! Please enter a valid phone number.{W}")

# Get SMS using Termux API
def get_sms():
    result = subprocess.run(["termux-sms-list"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    sms_list = result.stdout.decode("utf-8").strip().split("\n")
    return sms_list

# Forward SMS
def forward_sms(phone_number, message):
    print(f"{G}[+] New Message from {phone_number}: {W}{message}")

# Start Tracking
def start_tracking(phone_number):
    print(f"{Y}Tracking SMS for {phone_number}...{W}")
    print(f"{C}Press CTRL + C to stop.{W}\n")

    try:
        while True:
            sms_list = get_sms()
            for sms in sms_list:
                if "address" in sms and "body" in sms:
                    sender = sms.split(",")[0].split(":")[1].strip().strip('"')
                    body = sms.split(",")[1].split(":")[1].strip().strip('"')
                    if sender == phone_number:
                        forward_sms(sender, body)
            time.sleep(5)  # Refresh every 5 seconds
    except KeyboardInterrupt:
        print(f"{R}\nTracking stopped. Exiting...{W}")

# SMS Bombing Function
def sms_bomber(phone_number):
    print(f"{Y}SMS Bombing started on {phone_number}...{W}")
    # Add your custom bombing logic here, delayed or multiple messages to bomb the target
    for i in range(10):  # This example sends 10 messages
        subprocess.run(f"termux-sms-send {phone_number} 'This is a test bomb message!'")

# Main Function
if __name__ == "__main__":
    banner()
    input(f"{Y}Press ENTER to continue...{W}")
    phone_number = get_phone_number()
    option = input(f"{C}Choose Option:\n1. Track SMS\n2. SMS Bomber\n{W}")
    
    if option == "1":
        start_tracking(phone_number)
    elif option == "2":
        sms_bomber(phone_number)
    else:
        print(f"{R}Invalid option. Exiting...{W}")
        exit()