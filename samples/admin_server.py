# Administer the server
# https://github.com/element-hq/dendrite/blob/main/docs/administration/4_adminapi.md

import MatrixPythonClient
import PythonAPIClientBase
from MainMenu import MainMenu

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



menu_context = {
    "client": client,
    "login_session": login_session
}
mainMenu = MainMenu(menu_context)
mainMenu.run()

# users = client.getAllUsers(login_session=menu_context["login_session"])
# for user in users:
#     print("User", user)

print("end")
