import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from Clients.SenderAliceClient import SenderAliceClient
from Clients.ReceiverBobClient import Receiver
from Hacker.Cleint.HackerOscarClient import HackerOscarClient
class Main:
    def __init__(self):
         self.run_communication()
    def run_communication(self):
         # Initialize the sender client and retrieve the encrypted message
        sender = SenderAliceClient()
        encrypted_message = sender.encrypted_message
        # Initialize the receiver client and receive the encrypted message
        receiver = Receiver()
        receiver.receive_message(encrypted_message)
        print("-----Oscar's dark world-----")
        hack_attempt = input("Do you want to start Hacking (yes/no): ").strip().lower()

        # Check if the user's input is 'yes', otherwise skip the hacking attempt
        if hack_attempt in ['y', 'yes']:
            self.run_decryption(encrypted_message)
        elif hack_attempt in ['n', 'no']:
            print("Oscar's hacking attempt was skipped.")
        else:
            print("Invalid input. Please respond with 'yes' or 'no'.")

    def run_decryption(self, encrypted_message):
        print("Hacking started")
        
        # Initialize the hacker client with the path to the wordlist file
        wordlist_path = "turkish_wordsList.txt"  # Wordlist dosyasının yolunu burada belirtin
        client = HackerOscarClient(wordlist_path)
        
        # Start the decryption process with the provided encrypted message
        client.start_decryption(encrypted_message)

if __name__ == "__main__":
    Main()


