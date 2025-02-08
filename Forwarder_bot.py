import subprocess
import time
import sys
import os

def clear():
    """Clear the terminal screen."""
    os.system('clear' if os.name == 'posix' else 'cls')

def display_welcome_message():
    """Display the welcome message and disclaimer."""
    clear()
    print("\033[1;32m" + "*"*50)
    print("   Welcome to ForwarderBot!  \033[1;34m SMS Forwarding Made Easy!")
    print("\033[1;32m" + "*"*50)
    print("\n\033[1;37mThis bot tracks incoming SMS and forwards them to Termux.")
    print("Important: This could be illegal. Use only for educational purposes.")
    print("\nPress '1' to start operation.\n")

def get_phone_number():
    """Prompt user to enter the phone number to track."""
    phone_number = input("\033[1;33mEnter the phone number to track: \033[1;37m")
    if phone_number.isdigit() and len(phone_number) >= 10:
        return phone_number
    else:
        print("\033[1;31mInvalid phone number. Please enter a valid number.\033[1;37m")
        return get_phone_number()

def get_sms():
    """Get the latest SMS message using the Termux API."""
    result = subprocess.run(['termux-sms-list'], stdout=subprocess.PIPE)
    sms_list = result.stdout.decode('utf-8').strip().split("\n")
    return sms_list

def forward_sms(phone_number, message):
    """Forward the received SMS to Termux."""
    print(f"\033[1;36mMessage from {phone_number}:\033[1;37m {message}")

def start_sms_tracking(phone_number):
    """Start the SMS tracking and forwarding process."""
    print("\033[1;32mTracking SMS for the given number...\033[1;37m")

    while True:
        # Get the latest SMS messages using the Termux API
        sms_list = get_sms()

        for sms in sms_list:
            # Parse the incoming message and phone number
            if "address" in sms and "body" in sms:
                address = sms.split(",")[0].split(":")[1].strip().strip('"')
                body = sms.split(",")[1].split(":")[1].strip().strip('"')
                
                # If the SMS is from the tracked phone number, forward it
                if address == phone_number:
                    forward_sms(address, body)

        time.sleep(5)  # Sleep for a while before checking again

if __name__ == "__main__":
    display_welcome_message()

    # Wait for the user to press '1' to start the operation
    choice = input("\n\033[1;37mPress '1' to start: ")
    if choice == '1':
        phone_number = get_phone_number()
        start_sms_tracking(phone_number)
    else:
        print("\033[1;31mInvalid input. Exiting...\033[1;37m")