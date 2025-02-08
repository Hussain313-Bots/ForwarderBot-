import os
import time
import smtplib
import schedule
from termcolor import colored

# Clear screen function
def clear_screen():
    os.system('clear')  # For Linux/Termux
    # os.system('cls')  # For Windows

# Function to get current time
def get_current_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

# Function to display the welcome message
def display_welcome_message():
    """Display the welcome message with colors and emojis."""
    print(colored("💀💀 Welcome to ForwarderBot 💀💀", "red", attrs=["bold"]))
    print(colored("This bot tracks incoming SMS and forwards them to Termux.", "green"))
    print(colored("Press '1' to start tracking messages from a specific phone number.", "yellow"))
    print(colored("Press '2' for SMS bombing all country.", "blue"))
    print(colored("Press '3' to schedule SMS forwarding.", "magenta"))
    print(colored("Press '4' to exit.", "cyan"))

# Function to log SMS
def log_sms(phone_number, message):
    """Log forwarded SMS to a file."""
    with open("sms_log.txt", "a") as log_file:
        log_file.write(f"💀💀 Message from {phone_number} at {get_current_time()}: {message} 💀💀\n")
    print(colored("💀💀 SMS logged 💀💀", "yellow"))

# Function to forward SMS to email
def forward_sms_to_email(message, subject="SMS Forwarded"):
    """Forward SMS to a specified email."""
    sender_email = "your_email@gmail.com"
    receiver_email = "receiver_email@gmail.com"
    password = "your_email_password"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    body = f"Subject: {subject}\n\n{message}"
    server.sendmail(sender_email, receiver_email, body)
    server.quit()
    print(colored("💀💀 SMS forwarded to email! 💀💀", "cyan"))

# Function to filter SMS based on keywords
def filter_sms(message, keywords=["Alert", "Important"]):
    """Check if the SMS message contains any of the keywords."""
    return any(keyword in message for keyword in keywords)

# Function to forward SMS
def forward_sms(phone_number, message):
    """Forward the received SMS to Termux with timestamp."""
    timestamp = get_current_time()
    if filter_sms(message):
        print(colored(f"💀💀 Message from {phone_number} at {timestamp}: {message} 💀💀", "green"))
        log_sms(phone_number, message)
        forward_sms_to_email(message)  # Forward to email
    else:
        print(colored("💀💀 Message filtered out 💀💀", "red"))

# Function to handle SMS bombing
def sms_bomb(number):
    """Send multiple SMS to a number (SMS bombing)."""
    print(colored(f"💀💀 Bombing {number} with SMS 💀💀", "red"))
    # Add your bombing logic here (ensure it complies with legal boundaries)
    for _ in range(5):  # Adjust the count as needed
        print(colored(f"💀💀 Bombing message sent to {number}! 💀💀", "blue"))
        time.sleep(1)  # Delay between SMS for better control

# Function to get phone numbers (support for multiple numbers)
def get_phone_numbers():
    """Prompt user to enter multiple phone numbers to track."""
    phone_numbers = input("Please enter phone numbers to track (separate by commas): ")
    phone_numbers = [num.strip() for num in phone_numbers.split(',')]
    return phone_numbers

# Function to choose language
def choose_language():
    """Let the user choose a language."""
    print(colored("Select Language:", "yellow"))
    print(colored("1: English", "green"))
    print(colored("2: Español", "blue"))
    choice = input("Choose an option: ")
    return choice

# Function to handle main menu
def main_menu():
    """Display the main menu."""
    clear_screen()
    display_welcome_message()
    choice = input("Choose an option: ")
    return choice

# Function to schedule SMS forwarding
def job():
    """Scheduled job to forward SMS."""
    print(colored("💀💀 Forwarding scheduled SMS 💀💀", "cyan"))

# Function to start scheduling
def start_scheduling():
    """Schedule the SMS forwarding to run periodically."""
    schedule.every(1).minute.do(job)  # Schedule every 1 minute
    while True:
        schedule.run_pending()
        time.sleep(1)

# Main bot function to drive the logic
def run_bot():
    """Main bot loop to interact with the user."""
    while True:
        choice = main_menu()
        if choice == '1':
            phone_numbers = get_phone_numbers()
            for phone_number in phone_numbers:
                message = input(f"Enter the message from {phone_number}: ")
                forward_sms(phone_number, message)
        elif choice == '2':
            phone_number = input("Enter phone number to bomb (e.g. +968 7738 4814): ")
            sms_bomb(phone_number)
        elif choice == '3':
            print("💀💀 SMS Forwarding is now scheduled 💀💀")
            start_scheduling()
        elif choice == '4':
            print(colored("💀💀 Exiting the bot... 💀💀", "red"))
            break
        else:
            print(colored("Invalid choice, please try again.", "yellow"))

if __name__ == "__main__":
    run_bot()