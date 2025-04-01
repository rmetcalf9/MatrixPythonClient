# Matrix client class
import PythonAPIClientBase
from .MatrixLoginSession import MatrixLoginSession

class MatrixClient(PythonAPIClientBase.APIClientBase):

    def getLoginSessionFromUsernameAndPassword(self, username, password):
        return MatrixLoginSession(client=self, username=username, password=password)