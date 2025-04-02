# Administer the server
# https://github.com/element-hq/dendrite/blob/main/docs/administration/4_adminapi.md

import MatrixPythonClient
import PythonAPIClientBase
from MainMenu import MainMenu
from Connections import Connections

print("Start")

connections = Connections()
connection = connections.get_first_connection()
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
