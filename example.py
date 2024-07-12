import os
from time import sleep

import dotenv
from blossom_interface import BlossomInterface

import random

if __name__ == '__main__':
    dotenv.load_dotenv()
    bl = BlossomInterface(False, os.getenv("SERVER_IP"), os.getenv("SERVER_PORT"))

    # Control blossom with bl object
    bl.reset()
    bl.do_sequence("yes", 0, 1)
    bl.do_sequence("no", 0, 0)
    sleep(1)
    bl.do_sequence("grand/grand1", 1.0, 0)
    bl.do_sequence("grand/grand2", 1.0, 1)
    sleep(5)

    # More complex behavior
    print("Random selection of idle sequences")
    idle_sequences = ["breathing/exhale", "breathing/inhale", "fear/fear_startled", "happy/happy_lookingup",
                      "sad/sad_downcast"]
    random.shuffle(idle_sequences)
    bl.do_sequence(idle_sequences[0], 0, 0)
    random.shuffle(idle_sequences)
    bl.do_sequence(idle_sequences[0], 0, 1)
    input()
