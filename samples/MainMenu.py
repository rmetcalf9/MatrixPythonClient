from _Menu import Menu
from InquirerPy import inquirer
from Interactive_Json_inspector import InteractiveJsonInspector
import json

class MainMenu(Menu):
    def _list_of_operations(self):
        return {
            "Admin - Who am I": self.admin_who_am_i,
            "Check username availability": self.is_username_availaivble,
            "get_capabilities": self.get_capabilities,
            "server sync": self.get_sync,
            "update_display_name": self.update_display_name,
        }

    def admin_who_am_i(self):
        # /_matrix/client/v3/admin/whois/{userId}
        user_id = self.menu_context["login_session"].get_user_id()
        print("Calling whois " + user_id)
        response = self.menu_context["client"].sendGetRequest(
            "/_matrix/client/v3/admin/whois/" + user_id,
            loginSession=self.menu_context["login_session"]
        )
        print("Result:", response.text)

    def is_username_availaivble(self):
        username = inquirer.text(message="Enter username to test:", default="admin").execute()
        if self.menu_context["client"].isUsernameAvailiable(login_session=self.menu_context["login_session"], username=username):
            print("Available")
        else:
            print("Not Available")

    def get_capabilities(self):
        response = self.menu_context["client"].sendGetRequest(
            "/_matrix/client/v3/capabilities",
            loginSession=self.menu_context["login_session"]
        )
        print("Result:", response.text)

    def get_sync(self):
        response = self.menu_context["client"].sendGetRequest(
            "/_matrix/client/v3/sync",
            loginSession=self.menu_context["login_session"]
        )
        inspector = InteractiveJsonInspector(json.loads(response.text))
        inspector.run()

    def update_display_name(self):
        new_display_name = inquirer.text(message="Enter new display name:", default="Admin Display").execute()
        response = self.menu_context["client"].update_own_display_name(
            login_session=self.menu_context["login_session"],
            display_name=new_display_name
        )
        print("Response:", response)
