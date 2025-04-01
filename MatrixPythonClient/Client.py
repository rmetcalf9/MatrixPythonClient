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
