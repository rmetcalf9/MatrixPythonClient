import json
from pathlib import Path

connections_file = "../secrets/connections.json"


class Connections():
    connections = None
    def __init__(self):
        my_file = Path(connections_file)
        if not my_file.is_file():
            raise Exception("Connections file doesn't exist")

        connections = None
        with open(connections_file) as f:
            self.connections = json.load(f)
        if self.connections is None:
            raise Exception("Could not load connections")

        if len(self.connections) != 1:
            raise Exception("Not implemented multiple connection selection")


    def get_first_connection(self):
        return self.connections[0]
