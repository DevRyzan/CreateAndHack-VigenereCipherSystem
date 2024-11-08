import subprocess
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
        sender = SenderAliceClient()
        encrypted_message = sender.encrypted_message

        receiver = Receiver()
        receiver.receive_message(encrypted_message)

        hack_attempt = input("Do you want Oscar to try hacking the message? (yes/no): ").strip().lower()

        if hack_attempt == 'yes':
            hacker = HackerOscarClient(encrypted_message, max_key_length=3)
            hacker.attempt_hack()
        else:
            print("Oscar's hacking attempt was skipped.")

if __name__ == "__main__":
    Main()