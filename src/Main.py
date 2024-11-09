import subprocess
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from Clients.SenderAliceClient import SenderAliceClient
from Clients.ReceiverBobClient import Receiver
from Hacker.Cleint.HackerOscarClient import HackerOscarClient

url = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"


class Main:
    def __init__(self):
        """Initialize the Main class and run the communication process."""
        self.run_communication()

    def run_communication(self):
        """Handle the communication process: sending and receiving the encrypted message."""
        # Initialize the sender client and retrieve the encrypted message
        sender = SenderAliceClient()
        encrypted_message = sender.encrypted_message

        # Initialize the receiver client and receive the encrypted message
        receiver = Receiver()
        receiver.receive_message(encrypted_message)
        
        # Prompt the user to decide whether Oscar (the hacker) should attempt to decrypt the message
        print("-----Oscar's dark world-----")
        hack_attempt = input("Hello Do you want to start Hacking (yes/no): ").strip().lower()

        # Check if the user's input is 'y' or 'yes', otherwise skip the hacking attempt
        if hack_attempt in ['y', 'yes']:
            self.run_decryption()
        elif hack_attempt in ['n', 'no']:
            print("Oscar's hacking attempt was skipped.")
        else:
            print("Invalid input. Please respond with 'yes' or 'no'.")

    def run_decryption(self):
        print("Hacking started")
        
        # Initialize the hacker client and start the decryption process
        client = HackerOscarClient()
        client.start_decryption()

if __name__ == "__main__":
    Main()