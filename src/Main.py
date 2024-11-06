import subprocess
import sys
import os

class Main:
    def __init__(self):
        self.start_sender_and_receiver()

    def start_sender_and_receiver(self):
        sender_path = os.path.join(os.path.dirname(__file__), 'Clients/SenderAliceClient.py')
        receiver_path = os.path.join(os.path.dirname(__file__), 'Clients/ReceiverBobClient.py')


        sender_process = subprocess.Popen([sys.executable, sender_path])

        receiver_process = subprocess.Popen([sys.executable, receiver_path])

        sender_process.wait()
        receiver_process.wait()

if __name__ == "__main__":
    Main()