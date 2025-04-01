from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

class Menu():
    menu_context = None
    def __init__(self, menu_context):
        self.menu_context = menu_context

    def _list_of_operations(self):
        raise Exception("Error should be overridden")

    def run(self):
        operations = self._list_of_operations()
        operation_list = []
        for operation in operations:
            operation_list.append(Choice(value=operation, name=operation))

        logout_text = "Exit"

        action = inquirer.select(
            message="Select an action:",
            choices=operation_list + [
                Separator(),
                Choice(value=None, name=logout_text),
            ],
            default=logout_text,
            height=8
        ).execute()
        if action is None:
            return False
        print("")
        operations[action]()
        print("")
        self.run()