import os
import threading
from time import sleep
from time import time

import dotenv
from blossom_interface import BlossomInterface

import random

if __name__ == '__main__':
    dotenv.load_dotenv()
    # Initialize blossom interface
    # Multi-blossom setup will only work with network interface
    bl = BlossomInterface(True, os.getenv("SERVER_IP"), os.getenv("SERVER_PORT"))

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

    # You might want to control blossom without use sleep() that blocks main program. In that case, use threading.
    # In most cases, sleep() is used for playing several sequences in a row. Because bl.do_sequence() will interrupt
    # current sequence.
    # You can use threading with sleep to do this.
    # Or if your sequence is not dynamic, you can use blossom_sequence_comb.py to combine sequences to be a new
    # sequence.

    # Example:
    class MyBlossomInterface:
        def __init__(self, bli):
            self.bli = bli

        def do_idle_sequences(self, delay_time, blossom_id, total_rounds):
            my_idle_sequences = ["breathing/exhale", "breathing/inhale", "fear/fear_startled", "happy/happy_lookingup",
                              "sad/sad_downcast"]
            sleep(delay_time)
            for i in range(total_rounds):
                random.shuffle(my_idle_sequences)
                print(f"Sequence: {my_idle_sequences[0]}, Blossom ID: {0}")
                self.bli.do_sequence(my_idle_sequences[0], 0, 0)
                random.shuffle(my_idle_sequences)
                print(f"Sequence: {my_idle_sequences[0]}, Blossom ID: {1}")
                self.bli.do_sequence(my_idle_sequences[0], 0, 1)
                sleep(3)

    # import threading
    my_bl = MyBlossomInterface(bl)
    bl_thread_target = my_bl.do_idle_sequences
    bl_thread_kwargs = {"delay_time": 0, "blossom_id": 0, "total_rounds": 3}
    bl_thread = threading.Thread(target=bl_thread_target, kwargs=bl_thread_kwargs)
    bl_thread.start()
    # Doing something else
