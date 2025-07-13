from Connections import Connections
import MatrixPythonClient
import PythonAPIClientBase
from KeyValueStore import KeyValueStore

# This script has the process for an externally autnenticated user will have a chat account created
#  and be added to a particular room

print("Start auto getister user in room")

connections = Connections()
connection = connections.get_first_connection()
client = MatrixPythonClient.MatrixClient(chat_domain=connection["chat_server"], mock=None, verboseLogging=PythonAPIClientBase.VerboseLoggingNullLogClass())
admin_login_session = client.getLoginSessionFromUsernameAndPassword(connection["username"], connection["password"])

password_store = KeyValueStore("../secrets/auto_reg_password.json")
room_store = KeyValueStore("../secrets/auto_reg_room.json")

def password_fetch_function(username):
    print("Password fetch called", username)
    return password_store.get(username)

def password_store_function(username, password):
    print("Password store called", username, password)
    return password_store.set(username, password)

def room_fetch_function(roomname):
    print("Room fetch called", roomname)
    return room_store.get(roomname)

def room_store_function(roomname, roomid):
    print("Room store called", roomname, roomid)
    return room_store.set(roomname, roomid)

test_num = "12"
username = "created_username" + test_num
user_displayname = "created_username_display"

room_name = "Test room" + test_num
clubchat_room_id = "someclubchat_idx" + test_num
room_topic = "talk about test stuff"
room_alias_name = None

response = client.auto_register_user_in_room(
    admin_login_session=admin_login_session,
    registration_shared_secret=connection["registration_shared_secret"],
    username=username,
    displayname=user_displayname,
    user_password_fetch_function=password_fetch_function,
    user_password_store_function=password_store_function,
    clubchat_room_id=clubchat_room_id,  # unique identifier of clubchat room
    room_topic=room_topic,
    room_name=room_name,
    room_alias_name=room_alias_name,
    room_fetch_function=room_fetch_function,  # fetch room id's
    room_store_function=room_store_function,  # Store room id's
)

print("username", username)
print("login session user_id", response["login_session"].get_user_id())
print("Result=", response)

print("End auto getister user in room")
