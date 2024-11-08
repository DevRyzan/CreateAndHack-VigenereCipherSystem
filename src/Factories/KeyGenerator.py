import random
import string


def generate_key(length=3):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
