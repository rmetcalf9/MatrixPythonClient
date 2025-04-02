from Connections import Connections
import MatrixPythonClient
import PythonAPIClientBase


# This script has the process for an externally autnenticated user will have a chat account created
#  and be added to a particular room

print("Start auto getister user in room")

connections = Connections()
connection = connections.get_first_connection()
client = MatrixPythonClient.MatrixClient(baseURL="https://" + connection["chat_server"], mock=None, verboseLogging=PythonAPIClientBase.VerboseLoggingNullLogClass())

def password_fetch_function(username):
    print("Password fetch called", username)
    return "abc123"

def password_store_function(username, password):
    print("Password store called", username, password)
    return None

room_topic = "talk about test stuff"
room_name = "Test room"
room_alias_name = room_name

#POST /_matrix/client/v3/createRoom
create_room_body = {
    "creation_content": {},
    "initial_state": [],
    "invite": [], #TODO Add requesting user
    "invite_3pid": [],
    "is_direct": True,
    "name": room_name,
    PRESET???,
    "room_alias_name": room_alias_name
    "room_version": TODO
    "topic": room_topic
    "visibility": "private"
}
response = client.auto_register_user_in_room(
    username="username",
    password_fetch_function=password_fetch_function,
    password_store_function=password_store_function
)

print("End auto getister user in room")
