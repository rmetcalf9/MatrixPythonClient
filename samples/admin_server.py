# Administer the server
# https://github.com/element-hq/dendrite/blob/main/docs/administration/4_adminapi.md

import MatrixPythonClient
import PythonAPIClientBase

import requests
import json
from pathlib import Path

print("Start")

connections_file = "../secrets/connections.json"


my_file = Path(connections_file)
if not my_file.is_file():
    raise Exception("Connections file doesn't exist")

connections = None
with open(connections_file) as f:
    connections = json.load(f)
if connections is None:
    raise Exception("Could not load connections")

if len(connections) != 1:
    raise Exception("Not implemented multiple connection selection")

connection = connections[0]

client = MatrixPythonClient.MatrixClient(baseURL="https://" + connection["chat_server"], mock=None, verboseLogging=PythonAPIClientBase.VerboseLoggingNullLogClass())

print("Connecting to", connection["name"])
login_session = client.getLoginSessionFromUsernameAndPassword(username=connection["username"], password=connection["password"])

print("Login user id=", login_session.get_user_id())


#/_matrix/client/v3/admin/whois/{userId}

response = client.sendGetRequest("/_matrix/client/v3/admin/whois/" + login_session.get_user_id(), loginSession=login_session)
print(response.text)

print("end")
