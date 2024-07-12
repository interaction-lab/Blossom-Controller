# Description: This file contains the BlossomNetworkInterface class which is used to send data to the server.
# This is not a standalone script. Use BlossomInterface instead.
import logging
import requests
import json

logger = logging.getLogger(__name__)


class BlossomNetworkInterface:
    def __init__(self, server_ip, server_port):
        # dotenv.load_dotenv()
        # self.server_ip = os.getenv("SERVER_IP")
        # self.server_port = os.getenv("SERVER_PORT")
        self.server_ip = server_ip
        self.server_port = server_port
        # self.blossom_id = blossom_id

        self.url = f"http://{self.server_ip}:{self.server_port}/data"
        self.data = {
            "function": "do_start_sequence",
            "kwargs": {
                "blossom_id": 0,
                "delay_time": 0.5,
                "audio_length": 20,
                "seq": "reset"
            }
        }

    def do_sequence(self, seq, delay_time=0, blossom_id=0):
        self.data["function"] = "do_sequence"
        self.data["kwargs"]["seq"] = seq
        self.data["kwargs"]["delay_time"] = delay_time
        self.data["kwargs"]["blossom_id"] = blossom_id
        response = requests.post(self.url, json=self.data)
        logger.info(f"Sending data to server: {json.dumps(self.data, indent=2)}")
        logger.info(f"Response from server: {response.text}")

    def reset(self, blossom_id=0):
        self.data["function"] = "reset"
        self.data["kwargs"]["blossom_id"] = blossom_id
        response = requests.post(self.url, json=self.data)
        logger.info(f"Sending data to server: {json.dumps(self.data, indent=2)}")
        logger.info(f"Response from server: {response.text}")
