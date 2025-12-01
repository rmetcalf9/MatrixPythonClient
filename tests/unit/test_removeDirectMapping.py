import MatrixPythonClient
import PythonAPIClientBase
from unittest.mock import patch, MagicMock
import copy

def test_removeDirectMapping_noneexisting():
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
        res = client.updateDirectMappingRemoveRoomId(login_session=None, roomId=testRoomId)

        args, kwargs = mock_set.call_args

        assert kwargs["data_type"] == "m.direct"
        assert kwargs["data"] == {}

def test_removeDirectMapping_todelexists():
    client = MatrixPythonClient.MatrixClient(
        chat_domain="Test",
        mock=None,
        forceOneRequestAtATime=False,
        verboseLogging=PythonAPIClientBase.VerboseLoggingNullLogClass(),
        debug=False
    )

    testUserId = "testUserId"
    testRoomId = "testRoomId"

    mock_account_data = {testUserId: [testRoomId]}

    with patch.object(client, "getAccountData", return_value=mock_account_data), \
            patch.object(client, "setAccountData") as mock_set:
        res = client.updateDirectMappingRemoveRoomId(login_session=None, roomId=testRoomId)

        args, kwargs = mock_set.call_args

        assert kwargs["data_type"] == "m.direct"
        assert kwargs["data"] == {}

def test_removeDirectMapping_anothersameuserexists_todelmissing():
    client = MatrixPythonClient.MatrixClient(
        chat_domain="Test",
        mock=None,
        forceOneRequestAtATime=False,
        verboseLogging=PythonAPIClientBase.VerboseLoggingNullLogClass(),
        debug=False
    )

    testUserId = "testUserId"
    testRoomId = "testRoomId"
    testRoomId2 = "testRoomId2"

    mock_account_data = {testUserId: [testRoomId2]}
    expectedResult = copy.deepcopy(mock_account_data)
    expectedResult[testUserId] = [testRoomId2]

    with patch.object(client, "getAccountData", return_value=mock_account_data), \
            patch.object(client, "setAccountData") as mock_set:
        res = client.updateDirectMappingRemoveRoomId(login_session=None, roomId=testRoomId)

        args, kwargs = mock_set.call_args

        assert kwargs["data_type"] == "m.direct"
        assert kwargs["data"] == expectedResult

def test_removeDirectMapping_anothersameuserexists_topresent():
    client = MatrixPythonClient.MatrixClient(
        chat_domain="Test",
        mock=None,
        forceOneRequestAtATime=False,
        verboseLogging=PythonAPIClientBase.VerboseLoggingNullLogClass(),
        debug=False
    )

    testUserId = "testUserId"
    testRoomId = "testRoomId"
    testRoomId2 = "testRoomId2"

    mock_account_data = {testUserId: [testRoomId, testRoomId2]}
    expectedResult = copy.deepcopy(mock_account_data)
    expectedResult[testUserId] = [testRoomId2]

    with patch.object(client, "getAccountData", return_value=mock_account_data), \
            patch.object(client, "setAccountData") as mock_set:
        res = client.updateDirectMappingRemoveRoomId(login_session=None, roomId=testRoomId)

        args, kwargs = mock_set.call_args

        assert kwargs["data_type"] == "m.direct"
        assert kwargs["data"] == expectedResult

def test_removeDirectMapping_anotheruseruntouched():
    client = MatrixPythonClient.MatrixClient(
        chat_domain="Test",
        mock=None,
        forceOneRequestAtATime=False,
        verboseLogging=PythonAPIClientBase.VerboseLoggingNullLogClass(),
        debug=False
    )

    testUserId = "testUserId"
    testRoomId = "testRoomId"
    testRoomId2 = "testRoomId2"

    testUserId2 = "testUserId2"
    testRoomId3 = "testRoomId3"


    mock_account_data = {
        testUserId: [testRoomId, testRoomId2],
        testUserId2: [testRoomId3]
    }
    expectedResult = copy.deepcopy(mock_account_data)
    expectedResult[testUserId] = [testRoomId2]

    with patch.object(client, "getAccountData", return_value=mock_account_data), \
            patch.object(client, "setAccountData") as mock_set:
        res = client.updateDirectMappingRemoveRoomId(login_session=None, roomId=testRoomId)

        args, kwargs = mock_set.call_args

        assert kwargs["data_type"] == "m.direct"
        assert kwargs["data"] == expectedResult
