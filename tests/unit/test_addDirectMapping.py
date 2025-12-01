import MatrixPythonClient
import PythonAPIClientBase
from unittest.mock import patch, MagicMock
import copy

def test_addNewDirectMapping_noneexisting():
    client = MatrixPythonClient.MatrixClient(
        chat_domain="Test",
        mock=None,
        forceOneRequestAtATime=False,
        verboseLogging=PythonAPIClientBase.VerboseLoggingNullLogClass(),
        debug=False
    )

    testUserId = "testUserId"
    testRoomId = "testRoomId"

    mock_account_data = {}

    with patch.object(client, "getAccountData", return_value=mock_account_data), \
            patch.object(client, "setAccountData") as mock_set:
        res = client.updateDirectMappingAddRoomId(login_session=None, userId=testUserId, roomId=testRoomId)

        args, kwargs = mock_set.call_args

        assert kwargs["data_type"] == "m.direct"
        assert kwargs["data"] == {testUserId: [testRoomId]}

def test_addNewDirectMapping_anotherfordiffetentuser():
    client = MatrixPythonClient.MatrixClient(
        chat_domain="Test",
        mock=None,
        forceOneRequestAtATime=False,
        verboseLogging=PythonAPIClientBase.VerboseLoggingNullLogClass(),
        debug=False
    )

    testUserId = "testUserId"
    testRoomId = "testRoomId"

    mock_account_data = {
        "testUserId2": ["testUser2Rooms"]
    }
    expectedResult = copy.deepcopy(mock_account_data)
    expectedResult[testUserId] = [testRoomId]

    with patch.object(client, "getAccountData", return_value=mock_account_data), \
            patch.object(client, "setAccountData") as mock_set:
        res = client.updateDirectMappingAddRoomId(login_session=None, userId=testUserId, roomId=testRoomId)

        args, kwargs = mock_set.call_args

        assert kwargs["data_type"] == "m.direct"
        assert kwargs["data"] == expectedResult

def test_addNewDirectMapping_anotherforsameuser():
    client = MatrixPythonClient.MatrixClient(
        chat_domain="Test",
        mock=None,
        forceOneRequestAtATime=False,
        verboseLogging=PythonAPIClientBase.VerboseLoggingNullLogClass(),
        debug=False
    )

    testUserId = "testUserId"
    testRoomId = "testRoomId"

    mock_account_data = {
        testUserId: ["testUser2Rooms"]
    }
    expectedResult = copy.deepcopy(mock_account_data)
    expectedResult[testUserId] = ["testUser2Rooms", testRoomId]

    with patch.object(client, "getAccountData", return_value=mock_account_data), \
            patch.object(client, "setAccountData") as mock_set:
        res = client.updateDirectMappingAddRoomId(login_session=None, userId=testUserId, roomId=testRoomId)

        args, kwargs = mock_set.call_args

        assert kwargs["data_type"] == "m.direct"
        assert kwargs["data"] == expectedResult

def test_addNewDirectMapping_updateroomid():
    client = MatrixPythonClient.MatrixClient(
        chat_domain="Test",
        mock=None,
        forceOneRequestAtATime=False,
        verboseLogging=PythonAPIClientBase.VerboseLoggingNullLogClass(),
        debug=False
    )

    testUserId = "testUserId"
    testOldRoomId = "testOldRoomId"
    testRoomId = "testRoomId"

    mock_account_data = {
        testUserId: [testOldRoomId]
    }
    expectedResult = copy.deepcopy(mock_account_data)
    expectedResult[testUserId] = [testOldRoomId, testRoomId]

    with patch.object(client, "getAccountData", return_value=mock_account_data), \
            patch.object(client, "setAccountData") as mock_set:
        res = client.updateDirectMappingAddRoomId(login_session=None, userId=testUserId, roomId=testRoomId)

        args, kwargs = mock_set.call_args

        assert kwargs["data_type"] == "m.direct"
        assert kwargs["data"] == expectedResult

def test_addNewDirectMapping_updateroomid_exactlythesam():
    client = MatrixPythonClient.MatrixClient(
        chat_domain="Test",
        mock=None,
        forceOneRequestAtATime=False,
        verboseLogging=PythonAPIClientBase.VerboseLoggingNullLogClass(),
        debug=False
    )

    testUserId = "testUserId"
    testRoomId = "testRoomId"

    mock_account_data = {
        testUserId: [testRoomId]
    }
    expectedResult = copy.deepcopy(mock_account_data)
    expectedResult[testUserId] = [testRoomId]

    with patch.object(client, "getAccountData", return_value=mock_account_data), \
            patch.object(client, "setAccountData") as mock_set:
        res = client.updateDirectMappingAddRoomId(login_session=None, userId=testUserId, roomId=testRoomId)

        args, kwargs = mock_set.call_args

        assert kwargs["data_type"] == "m.direct"
        assert kwargs["data"] == expectedResult



