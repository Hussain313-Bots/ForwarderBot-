import subprocess
import time
import re

def display_welcome_message():
    """Display the welcome message and disclaimer."""
    print("\033[1;32mWelcome to ForwarderBot!\033[0m")
    print("\033[1;34mThis bot tracks incoming SMS and forwards them to Termux.\033[0m")
    print("\033[1;31mImportant: This could be illegal. Use only for educational purposes.\033[0m")
    print("\033[1;33mPress '1' to start operation.\033[0m")

def get_phone_number():
    """Prompt user to enter the phone number to track."""
    while True:
        phone_number = input("\033[1;36mPlease enter the phone number to track (in format +1xxxxxxxxxx): \033[0m")
        # Validate phone number format
        if re.match(r'^\+?\d{1,3}?\d{10}$', phone_number):  # Example for US numbers (+1234567890)
            return phone_number
        else:
            print("\033[1;31mInvalid number format. Please use the correct format: +1xxxxxxxxxx.\033[0m")

def get_sms():
    """Get the latest SMS message using the Termux API."""
    result = subprocess.run(['termux-sms-list'], stdout=subprocess.PIPE)
    sms_list = result.stdout.decode('utf-8').strip().split("\n")
    return sms_list

def forward_sms(phone_number, message):
    """Forward the received SMS to Termux."""
    print(f"\033[1;32mMessage from {phone_number}: {message}\033[0m")

def start_sms_tracking(phone_number):
    """Start the SMS tracking and forwarding process."""
    print("\033[1;34mTracking SMS for the given number...\033[0m")
    
    while True:
        sms_list = get_sms()

        for sms in sms_list:
            # Parse the incoming message and phone number
            if "address" in sms and "body" in sms:
                address = sms.split(",")[0].split(":")[1].strip().strip('"')
                body = sms.split(",")[1].split(":")[1].strip().strip('"')
                
                if address == phone_number:
                    forward_sms(address, body)

        time.sleep(5)  # Check again after 5 seconds

if __name__ == "__main__":
    display_welcome_message()

    # Wait for the user to press '1' to start the operation
    choice = input("\033[1;36mPress '1' to start: \033[0m")
    if choice == '1':
        phone_number = get_phone_number()
        start_sms_tracking(phone_number)
    else:
        print("\033[1;31mInvalid input. Exiting.\033[0m")