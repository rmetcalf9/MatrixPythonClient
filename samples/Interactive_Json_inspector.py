from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
import json

DUMMY_ACTION_TYPE="dfsgbjr34trhgfdsadfgDFDSsdfR£45terfd"
FULL_EXIT_ACTION_TYPE="dfsgbjr34trhgfdsgadfgDFDSsdfR£45terfd"
RAW_ACTION_TYPE="dfsg2bjr34trhgfdsgadfgDFDSsdfR£45terfd"
RAW_PRETTY_ACTION_TYPE="dfsgbjr34trhgfdsdfgDFrrDSsdfR£45terfd"

def get_type_data(item_key, item_value):
    if isinstance(item_value, str):
        return {
            "text": str(item_key) + "=\"" + str(item_value) + "\"",
            "action": DUMMY_ACTION_TYPE,
            "islist": False,
        }
    if isinstance(item_value, int):
        return {
            "text": str(item_key) + "=" + str(item_value),
            "action": DUMMY_ACTION_TYPE,
            "islist": False,
        }
    if isinstance(item_value, dict):
        if len(item_value.keys())==0:
            return {
                "text": str(item_key) + "={}",
                "action": DUMMY_ACTION_TYPE,
                "islist": False,
            }
        return {
            "text": str(item_key) + "=...{Dict}",
            "action": item_key,
            "islist": False,
        }
    if isinstance(item_value, list):
        if len(item_value)==0:
            return {
                "text": str(item_key) + "=[]",
                "action": DUMMY_ACTION_TYPE,
                "islist": False,
            }
        return {
            "text": str(item_key) + "=...[List]",
            "action": item_key,
            "islist": True,
        }
    return {
        "text": str(item_key) + "=???",
        "action": DUMMY_ACTION_TYPE,
        "islist": False,
    }


class InteractiveJsonInspector:
    json = None
    def __init__(self, json):
        self.json = json

    def run(self):
        self.inspect_from(jsonstr=self.json, root=True)

    def inspect_from(self, jsonstr, root=False, path="", parent_is_list=False):
        # inspect json from this tree
        operation_list = []
        if isinstance(jsonstr, list):
            for idx in range(0, len(jsonstr)):
                action_type = get_type_data(idx, jsonstr[idx])
                operation_list.append(Choice(value=action_type, name=action_type["text"]))
        else:
            items = []
            for operation in jsonstr.keys():
                action_type = get_type_data(operation, jsonstr[operation])
                operation_list.append(Choice(value=action_type, name=action_type["text"]))

        operation_list.append(Separator())
        operation_list.append(Choice(value={"action": RAW_ACTION_TYPE}, name="Raw"))
        operation_list.append(Choice(value={"action": RAW_PRETTY_ACTION_TYPE}, name="Raw (Pretty)"))
        if not root:
            operation_list.append(Choice(value={"action": None}, name="...Up"))
        operation_list.append(Choice(value={"action": FULL_EXIT_ACTION_TYPE}, name="Finish"))

        while True:
            action = inquirer.select(
                message="Select: (" + path + ")",
                choices=operation_list,
                default="Finish",
                height=8
            ).execute()
            if action["action"] is None:
                return False
            if action["action"] == FULL_EXIT_ACTION_TYPE:
                return True #True triggers full exit
            print("")
            if action["action"] == RAW_ACTION_TYPE:
                print(jsonstr)
                print("")
            elif action["action"] == RAW_PRETTY_ACTION_TYPE:
                print(json.dumps(jsonstr, indent=2))
                print("")
            elif action["action"] != DUMMY_ACTION_TYPE:
                new_path = path + "[\"" + str(action["action"]) + "\"]"
                if parent_is_list:
                    new_path =path + "[" + str(action["action"]) + "]"
                full_exit = self.inspect_from(jsonstr=jsonstr[action["action"]], path=new_path, parent_is_list=action["islist"])
                if full_exit:
                    return True
                print("")
