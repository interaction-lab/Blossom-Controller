# Description: This file is the main interface to the Blossom robot.
# Note: Set use_network_interface to False if you want to control blossom from the same machine.
# Import this file into your project
from blossom_network_interface import BlossomNetworkInterface
from blossom_local_interface import BlossomLocalInterface


class BlossomInterface:
    def __init__(self, use_network_interface=True, server_ip=None, server_port=None):
        self.bli = None
        if use_network_interface:
            self.bli = BlossomNetworkInterface(server_ip, server_port)
        else:
            self.bli = BlossomLocalInterface()

    def do_sequence(self, seq, delay_time=0, blossom_id=0):
        self.bli.do_sequence(seq, delay_time, blossom_id)

    def reset(self, blossom_id=0):
        self.bli.reset(blossom_id)
