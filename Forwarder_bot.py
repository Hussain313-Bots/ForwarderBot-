import os
import smtplib
import time
import subprocess
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from colorama import Fore

# Colors for UI
R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
B = Fore.BLUE
C = Fore.CYAN
W = Fore.WHITE

# Banner Function
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
    print(f"{G}Welcome to Multi-Function Hacking Tool!{W}")
    print(f"{Y}SMS Forwarder, SMS Bomber, Email Bomber, and IP Tracker in one tool!{W}")
    print(f"{R}⚠ WARNING: Use only for educational purposes in a lab environment! ⚠{W}")
    print("\n")

# Get Phone Number for SMS Forwarder
def get_phone_number():
    while True:
        number = input(f"{C}Enter the phone number to track (or type 'exit' to quit): {W}")
        if number.lower() == "exit":
            print(f"{R}Exiting...{W}")
            exit()
        elif number.isdigit() and len(number) >= 8:
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

# Start Tracking SMS
def start_sms_forwarding(phone_number):
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

# Email Bomber Function
def send_email(target_email, subject, message, sender_email, sender_password, smtp_server, smtp_port):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = target_email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        server.sendmail(sender_email, target_email, msg.as_string())
        server.quit()
        
        print(f"{G}[+] Email sent to {target_email}{W}")
    except Exception as e:
        print(f"{R}[-] Error sending email: {str(e)}{W}")

def start_email_bombing(target_email, subject, message, sender_email, sender_password, smtp_server, smtp_port, email_count, delay):
    for _ in range(email_count):
        send_email(target_email, subject, message, sender_email, sender_password, smtp_server, smtp_port)
        time.sleep(delay)

# SMS Bomber
def sms_bomb(phone_number, message, delay, count):
    print(f"{Y}Starting SMS Bombing...{W}")
    for _ in range(count):
        subprocess.run(f"termux-sms-send -n {phone_number} {message}", shell=True)
        time.sleep(delay)

# IP Tracker
def ip_tracker(ip_address):
    print(f"{C}Tracking IP: {ip_address}...{W}")
    response = requests.get(f"https://geolocation-db.com/json/{ip_address}&position=true").json()
    if response['country_name'] != "Not found":
        print(f"{G}[+] IP Location: {response['country_name']}, {response['city']}, {response['latitude']}, {response['longitude']}{W}")
    else:
        print(f"{R}[-] Invalid IP Address!{W}")

# Main Menu
def menu():
    banner()
    print(f"{C}Choose an option:{W}")
    print(f"{Y}1. SMS Forwarder{W}")
    print(f"{Y}2. SMS Bomber{W}")
    print(f"{Y}3. Email Bomber{W}")
    print(f"{Y}4. IP Tracker{W}")
    print(f"{C}Enter your choice (1-4): ", end="")
    choice = input()

    if choice == "1":
        phone_number = get_phone_number()
        start_sms_forwarding(phone_number)
    elif choice == "2":
        phone_number = input(f"{C}Enter target phone number: {W}")
        message = input(f"{C}Enter message to send: {W}")
        delay = int(input(f"{C}Enter delay between messages (in seconds): {W}"))
        count = int(input(f"{C}Enter the number of messages to send: {W}"))
        sms_bomb(phone_number, message, delay, count)
    elif choice == "3":
        sender_email = input(f"{C}Enter your email: {W}")
        sender_password = input(f"{C}Enter your email password (use app-specific password for Gmail): {W}")
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        target_email = input(f"{C}Enter target email: {W}")
        subject = input(f"{C}Enter the email subject: {W}")
        message = input(f"{C}Enter the email message: {W}")
        email_count = int(input(f"{C}Enter number of emails to send: {W}"))
        delay = int(input(f"{C}Enter the delay between emails (in seconds): {W}"))

        start_email_bombing(target_email, subject, message, sender_email, sender_password, smtp_server, smtp_port, email_count, delay)
    elif choice == "4":
        ip_address = input(f"{C}Enter the IP address to track: {W}")
        ip_tracker(ip_address)
    else:
        print(f"{R}Invalid choice! Exiting...{W}")
        exit()

if __name__ == "__main__":
    menu()