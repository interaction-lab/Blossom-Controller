import os
from time import sleep

import dotenv
from blossom_interface import BlossomInterface

import random

if __name__ == '__main__':
    dotenv.load_dotenv()
    bl = BlossomInterface(True, os.getenv("SERVER_IP"), os.getenv("SERVER_PORT"), 2)

    # Control blossom with bl object
    # Multi-blossom control will only work for network interface

    # Using network interface:
    bl.reset()
    print(bl.do_sequence("yes", 0, 1, 2))
    print(bl.do_sequence("no", 0, 0, 1))
    # sleep(1)
    # print(bl.do_sequence("grand/grand1", 1.0, 0))
    # print(bl.do_sequence("grand/grand2", 1.0, 1))
    # sleep(5)

    # More complex behavior
    print("Random selection of idle sequences")
    idle_sequences = ["breathing/exhale", "breathing/inhale", "fear/fear_startled", "happy/happy_lookingup",
                      "sad/sad_downcast"]
    random.shuffle(idle_sequences)
    # bl.do_sequence(idle_sequences[0], 0, 0)
    random.shuffle(idle_sequences)
    # bl.do_sequence(idle_sequences[0], 0, 1)
    input()
