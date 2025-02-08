from termcolor import colored
import os
import time

# Function to clear the screen
def clear_screen():
    os.system('clear')  # For Linux/Termux
    # os.system('cls')  # For Windows

# Function to display the welcome message with TBomb-like interface
def display_welcome_message():
    """Display the welcome message with TBomb-like interface and emojis."""
    print(colored("💀💀💀💀💀💀💀💀💀💀", "red"))
    print(colored("💀💀💀 Welcome to ForwarderBot 💀💀💀", "red", attrs=["bold"]))
    print(colored("💀💀 This bot tracks incoming SMS and forwards them to Termux 💀💀", "green"))
    print(colored("💀💀 Press '1' to start tracking messages from a specific phone number 💀💀", "yellow"))
    print(colored("💀💀 Press '2' for SMS bombing all country 💀💀", "blue"))
    print(colored("💀💀 Press '0' to exit 💀💀", "magenta"))
    print(colored("💀💀💀💀💀💀💀💀💀💀", "red"))

# Function to get phone numbers from user
def get_phone_numbers():
    """Prompt user to enter phone numbers to track."""
    phone_numbers = input(colored("💀💀 Please enter phone numbers to track (separate by commas): 💀💀", "cyan"))
    phone_numbers = [num.strip() for num in phone_numbers.split(',')]
    return phone_numbers

# Function to simulate receiving an SMS
def receive_sms(phone_number, message):
    """Simulate receiving an SMS and forward it with a timestamp."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    print(colored(f"💀💀 Message from {phone_number} at {timestamp}: {message} 💀💀", "yellow"))

# Function to forward SMS to another number (or mock action)
def forward_sms(phone_number, message):
    """Forward the received SMS to Termux with timestamp."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    print(colored(f"💀💀 Forwarding message from {phone_number} at {timestamp}: {message} 💀💀", "green"))

# Function to handle SMS bombing
def sms_bombing():
    """Simulate SMS bombing all countries."""
    print(colored("💀💀💀 Starting SMS bombing... 💀💀💀", "red"))
    # Add SMS bombing logic here (mock)
    time.sleep(2)
    print(colored("💀💀💀 SMS bombing completed! 💀💀💀", "green"))

# Main menu function
def main_menu():
    """Display the main menu with cool emojis."""
    print(colored("💀💀💀💀💀💀💀💀💀💀", "red"))
    print(colored("1: Track messages from a phone number", "yellow"))
    print(colored("2: SMS bomb a number", "yellow"))
    print(colored("0: Exit", "magenta"))
    print(colored("💀💀💀💀💀💀💀💀💀💀", "red"))
    choice = input(colored("💀💀 Choose an option: 💀💀", "cyan"))
    return choice

# Main script function
def main():
    clear_screen()
    display_welcome_message()
    while True:
        choice = main_menu()

        if choice == '1':
            phone_numbers = get_phone_numbers()
            for phone_number in phone_numbers:
                message = input(f"💀💀 Enter message for {phone_number}: 💀💀")
                receive_sms(phone_number, message)
                forward_sms(phone_number, message)
        elif choice == '2':
            sms_bombing()
        elif choice == '0':
            print(colored("Exiting... Goodbye! 💀💀", "red"))
            break
        else:
            print(colored("Invalid choice! Please try again.", "yellow"))

if __name__ == "__main__":
    main()