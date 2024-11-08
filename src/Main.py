import subprocess
import sys
import os

# Path ayarlaması yapılıyor
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from Clients.SenderAliceClient import SenderAliceClient
from Clients.ReceiverBobClient import Receiver

class Main:
    def __init__(self):
        sender = SenderAliceClient()
        
        encrypted_message = sender.encrypted_message
        print(f"Main received encrypted message: {encrypted_message}")

        receiver = Receiver()
        receiver.receive_message(encrypted_message)

if __name__ == "__main__":
    main = Main()