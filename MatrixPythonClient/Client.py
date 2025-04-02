# Matrix client class
import PythonAPIClientBase
from .MatrixLoginSession import MatrixLoginSession
import json

class MatrixClient(PythonAPIClientBase.APIClientBase):

    def getLoginSessionFromUsernameAndPassword(self, username, password):
        return MatrixLoginSession(client=self, username=username, password=password)

    def getAllUsers(self, login_session):
        postData={
            "limit": 1
        }
        response = self.sendPostRequest(
            "/_matrix/client/v3/user_directory/search", loginSession=login_session,
            data=json.dumps(postData)
        )

        print("rs", response.text)
        print("h", response.headers)

        return [1,2,3]

    def isUsernameAvailiable(self, login_session, username):
        response = self.sendGetRequest(
            url="/_matrix/client/v3/register/available?username=" + username,
            loginSession=login_session
        )
        if response.status_code==200:
            return True
        return False

    def update_own_display_name(self, login_session, display_name):
        return self.update_display_name(login_session=login_session, userid=login_session.get_user_id(), display_name=display_name)

    def update_display_name(self, login_session, userid, display_name):
        put_body = {
            "displayname": display_name
        }
        response = self.sendPutRequest(
            url="/_matrix/client/v3/profile/" + userid + "/displayname",
            loginSession=login_session,
            data=json.dumps(put_body)
        )
        if response.status_code==200:
            return True
        raise Exception("FAiled to change display name")
