# Description: This file is used to control Blossom robot using the Blossom API.
# This is not a standalone script. Use BlossomInterface instead.
import random
import sys
import time
import logging

import sys
from pathlib import Path

HERE   = Path(__file__).resolve().parent
Bl_PATH = (HERE / "blossom-public").resolve()

if str(Bl_PATH) not in sys.path:
    sys.path.insert(0, str(Bl_PATH))

from blossompy import Blossom

SEQ_DIR = Bl_PATH / "blossompy" / "src" / "sequences"

logger = logging.getLogger(__name__)


class BlossomLocalInterface:
    def __init__(self):
        self.bl = Blossom(sequence_dir=SEQ_DIR)
        self.bl.connect()  # safe init and connects to blossom and puts blossom in reset position
        self.bl.load_sequences()
        self.bl.do_sequence("reset")
        logger.info("Blossom Connected & Initialized.")

    def reset(self, blossom_id=0):
        self.bl.do_sequence("reset")

    def do_sequence(self, seq="reset", delay_time=0, blossom_id=0):
        logger.info(f"Blossom start playing sequence {seq} with {delay_time}s of delay.")
        time.sleep(delay_time)
        logger.info(f"Blossom playing sequence {seq}")
        self.bl.do_sequence(seq)
