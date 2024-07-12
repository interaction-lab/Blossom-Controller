# Description: This is the client script that runs on the machine connected to Blossom via USB.
# This is only needed if you want to use network controller.
# This is the standalone script that runs on the machine connected to Blossom via USB.
blossom_id_ = 0
# Define blossom ID above

import socketio
import os
import json
import dotenv
import logging
from blossom_local_interface import BlossomLocalInterface

logger = logging.getLogger(__name__)
logger.info("Client Started.")

example_data = {
    "function": "do_start_sequence",
    "kwargs": {
        "blossom_id": 0,
        "delay_time": 0.5,
        "audio_length": 20,
        "seq": "reset"
    }
}


class BlossomClient:
    def __init__(self, server_ip, server_port, blossom_id=0):
        self.bl = BlossomLocalInterface()
        self.blossom_id = blossom_id
        self.sio = socketio.Client()
        self.sio.connect(f"http://{server_ip}:{server_port}")
        self.sio.on('data_update', self.on_data_update)
        self.sio.on('connect', self.on_connect)
        self.sio.on('disconnect', self.on_disconnect)
        # self.sio.wait()

    def on_data_update(self, data):
        logger.info(f"Received data: {json.dumps(data, indent=2)}")
        if data["kwargs"]["blossom_id"] == self.blossom_id:
            if data["function"] == "do_sequence":
                self.bl.do_sequence(data["kwargs"]["seq"], data["kwargs"]["delay_time"])
            elif data["function"] == "reset":
                self.bl.reset()
            else:
                logger.error(f"Function {data['function']} not found.")

    def wait(self):
        self.sio.wait()

    def on_connect(self):
        logger.info("Connected to server.")

    def on_disconnect(self):
        logger.info("Disconnected from server.")


if __name__ == '__main__':
    dotenv.load_dotenv()
    client = BlossomClient(os.getenv("SERVER_IP"), os.getenv("SERVER_PORT"), blossom_id_)
    client.wait()
