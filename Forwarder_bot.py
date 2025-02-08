import subprocess
import time

def display_welcome_message():
    """Display the welcome message and disclaimer."""
    print("Welcome to ForwarderBot!")
    print("This bot tracks incoming SMS and forwards them to Termux.")
    print("Important: This could be illegal. Use only for educational purposes.")
    print("Press '1' to start operation.")

def get_phone_number():
    """Prompt user to enter the phone number to track."""
    phone_number = input("Please enter the phone number to track: ")
    return phone_number

def get_sms():
    """Get the latest SMS message using the Termux API."""
    # Using the Termux API to get the most recent SMS.
    result = subprocess.run(['termux-sms-list'], stdout=subprocess.PIPE)
    sms_list = result.stdout.decode('utf-8').strip().split("\n")
    return sms_list

def forward_sms(phone_number, message):
    """Forward the received SMS to Termux."""
    print(f"Message from {phone_number}: {message}")

def start_sms_tracking():
    """Start the SMS tracking and forwarding process."""
    print("Tracking SMS for the given number...")

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
    choice = input("Press '1' to start: ")
    if choice == '1':
        phone_number = get_phone_number()
        start_sms_tracking()
    else:
        print("Invalid input. Exiting.")