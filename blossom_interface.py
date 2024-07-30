# Description: This file is the main interface to the Blossom robot.
# Note: Set use_network_interface to False if you want to control blossom from the same machine.
# Import this file into your project
import time
import queue
import threading
from blossom_network_interface import BlossomNetworkInterface
from blossom_local_interface import BlossomLocalInterface


class BlossomInterface:
    def __init__(self, use_network_interface=True, server_ip=None, server_port=None, num_blossoms=1,
                 sleep_check_threshold=0.1):
        self.bli = None
        self.timer = [time.time()] * num_blossoms
        self.threshold = sleep_check_threshold
        self.last_parameters = []
        for i in range(num_blossoms):
            self.last_parameters.append({"sleep_time": 0, "delay_time": 0})
        if use_network_interface:
            self.bli = BlossomNetworkInterface(server_ip, server_port)
        else:
            self.bli = BlossomLocalInterface()

    def do_sequence(self, seq, delay_time=0, blossom_id=0, sleep_time=0):
        print(f"blossom_id: {blossom_id}")
        print(f"seq: {seq}")
        print(f"timer: {self.timer[blossom_id]}")
        print(f"last_parameters: {self.last_parameters[blossom_id]}")
        print(f"time diff: {time.time() - self.timer[blossom_id] - (
                self.last_parameters[blossom_id]["sleep_time"] - self.threshold + self.last_parameters[blossom_id][
            "delay_time"])}")
        if blossom_id >= len(self.timer):
            raise ValueError(f"blossom_id {blossom_id} is out of range.")
        if time.time() - self.timer[blossom_id] - (
                self.last_parameters[blossom_id]["sleep_time"] - self.threshold + self.last_parameters[blossom_id][
            "delay_time"]) < 0:
            return False
        else:
            self.last_parameters[blossom_id]["sleep_time"] = sleep_time
            self.last_parameters[blossom_id]["delay_time"] = delay_time
            self.timer[blossom_id] = time.time()
            threading.Thread(target=self.bli.do_sequence, args=(seq, delay_time, blossom_id, sleep_time)).start()
            return True
        # self.bli.do_sequence(seq, delay_time, blossom_id)

    def reset(self, blossom_id=0, sleep_time=0):
        if blossom_id >= len(self.timer):
            raise ValueError(f"blossom_id {blossom_id} is out of range.")
        if time.time() - self.timer[blossom_id] - (
                self.last_parameters[blossom_id]["sleep_time"] - self.threshold + self.last_parameters[blossom_id][
            "delay_time"]) < 0:
            return False
        else:
            self.last_parameters[blossom_id]["sleep_time"] = sleep_time
            self.last_parameters[blossom_id]["delay_time"] = 0
            self.timer[blossom_id] = time.time()
            threading.Thread(target=self.bli.reset, args=(blossom_id, sleep_time)).start()
            return True
        # self.bli.reset(blossom_id)
