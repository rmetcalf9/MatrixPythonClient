# Contains my code relating to room powerlevels

def get_trusted_private_chat_power_levels(creator_user_ids):
    if len(creator_user_ids) == 0:
        raise Exception("No users specified")
    retVal = {
        "ban": 50,
        "events": {
            "m.room.name": 100,
            "m.room.power_levels": 100,
            "m.room.history_visibility": 100,
            "m.room.canonical_alias": 100,
            "m.room.avatar": 100,
            "m.room.tombstone": 100
        },
        "events_default": 0,
        "invite": 100,
        "kick": 100,
        "notifications": {
            "room": 50
        },
        "redact": 100,
        "state_default": 100,
        "users": {
        },
        "users_default": 0
    }
    for creator_user_id in creator_user_ids:
        retVal["users"][creator_user_id] = 100
    return retVal