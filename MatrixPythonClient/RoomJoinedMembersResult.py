
class RoomJoinedMembersResult():
    result = None

    def __init__(self, result):
        self.result = result

    def getMembershipForUser(self, user_id):
        for chunk in self.result["chunk"]:
            if chunk["sender"] == user_id:
                return chunk
        return None
