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
        
        # Print the file path for the wordlist file
        print("Looking for wordlist file at:", os.path.join(os.path.dirname(__file__), "turkish_wordsList.txt"))
        
        # Prompt the user to decide whether Oscar (the hacker) should attempt to decrypt the message
        hack_attempt = input("Hello Oscar Do you want to use Brut Forth Tec (yes/no): ").strip().lower()

        # If user agrees, initiate the decryption process
        if hack_attempt == 'y' or "yes":
            self.run_decryption()
        if hack_attempt=="n"or "no":
            print("Oscar's hacking attempt was skipped.")
        else:
            print("Oscar's hacking attempt was skipped.")

    def run_decryption(self):
        print("Hacking started")
        
        # Initialize the hacker client and start the decryption process
        client = HackerOscarClient()
        client.start_decryption()


# Main execution entry point
if __name__ == "__main__":
    Main()