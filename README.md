# Blossom-Controller
Blossom controller scripts that contain a interface to control blossom robot either via USB or via network.

## TLDR;
- Setup `.env` file for server IP and port.
- Import `BlossomInterface` from `blossom_interface.py` and implement your logic.
- Run `blossom_client.py` on the machine that is connected to blossom via USB.
- Run `blossom_server.py` on the server.
- Run your script.

## Notes:
- `blossom_interface.py`: Entry point of the interface, import this file to use the interface.
- `blossom_client.py`: Client class for the interface. Run this script on the machine connects to Blossom.
- `blossom_server.py`: Server class for the interface. Run this script on cloud server.
- `blossom_local_interface.py`: Wrapper class for the Blossom API, used in `blossom_interface.py`.
- `blossom_network_interface.py`: This class sends data to server, used in `blossom_interface.py`.
- `blossom_sequence_comb.py`: Utility class for combining sequences. See comments in the file for more details.
- `note.py`: Initially used as `__init__.py` for the package, but because of the blossom-public package, it is better to
  keep it as a separate file.
- `.env`: Server IP and port goes in here.
    - ```
        SERVER_IP=192.168.0.1
        SERVER_PORT=5000
