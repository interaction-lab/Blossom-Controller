# Description: This file is used to control Blossom robot using the Blossom API.
# This is not a standalone script. Use BlossomInterface instead.
import random
import sys
import time
import logging

sys.path.append("./blossom-public")
from blossompy import Blossom

logger = logging.getLogger(__name__)


class BlossomLocalInterface:
    def __init__(self):
        self.bl = Blossom(sequence_dir='./blossom-public/blossompy/src/sequences')
        self.bl.connect()  # safe init and connects to blossom and puts blossom in reset position
        self.bl.load_sequences()
        self.bl.do_sequence("reset")
        logger.info("Blossom Connected & Initialized.")

    def reset(self, blossom_id=0, sleep_time=0):
        self.bl.do_sequence("reset")
        time.sleep(sleep_time)

    def do_sequence(self, seq="reset", delay_time=0, blossom_id=0, sleep_time=0):
        logger.info(f"Blossom start playing sequence {seq} with {delay_time}s of delay.")
        time.sleep(delay_time)
        logger.info(f"Blossom playing sequence {seq}")
        self.bl.do_sequence(seq)
        time.sleep(sleep_time)
