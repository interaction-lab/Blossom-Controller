# Description: This file contains the BlossomNetworkInterface class which is used to send data to the server.
# This is not a standalone script. Use BlossomInterface instead.
import logging
import requests
import json
import time

logger = logging.getLogger(__name__)


class BlossomNetworkInterface:
    def __init__(self, server_ip, server_port):
        # dotenv.load_dotenv()
        # self.server_ip = os.getenv("SERVER_IP")
        # self.server_port = os.getenv("SERVER_PORT")
        self.server_ip = server_ip
        self.server_port = server_port
        # self.blossom_id = blossom_id
        # self.q = queue

        self.url = f"http://{self.server_ip}:{self.server_port}/data"

        # Example data
        # tells blossom to do reset sequence after 0.5 seconds
        self.data = {
            "function": "do_sequence",
            "kwargs": {
                "blossom_id": 0,
                "delay_time": 0.5,
                "seq": "reset"
            }
        }

    def do_sequence(self, seq, delay_time=0, blossom_id=0, sleep_time=0):
        print("=====================================================")
        print(f"blossom_id: {blossom_id}")
        print(f"seq: {seq}")
        print("=====================================================")
        self.data["function"] = "do_sequence"
        self.data["kwargs"] = dict()
        self.data["kwargs"]["seq"] = seq
        self.data["kwargs"]["delay_time"] = delay_time
        self.data["kwargs"]["blossom_id"] = blossom_id
        response = requests.post(self.url, json=self.data)
        logger.info(f"Sending data to server: {json.dumps(self.data, indent=2)}")
        logger.info(f"Response from server: {response.text}")
        logger.info(f"Sleeping for {sleep_time} seconds.")
        time.sleep(sleep_time)
        self.data = dict()
        # self.q.put(True)

    def reset(self, blossom_id=0, sleep_time=0):
        self.data["function"] = "reset"
        self.data["kwargs"] = dict()
        self.data["kwargs"]["blossom_id"] = blossom_id
        response = requests.post(self.url, json=self.data)
        logger.info(f"Sending data to server: {json.dumps(self.data, indent=2)}")
        logger.info(f"Response from server: {response.text}")
        logger.info(f"Sleeping for {sleep_time} seconds.")
        self.data = dict()
        # self.q.put(True)
