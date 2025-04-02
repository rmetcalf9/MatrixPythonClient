from _Menu import Menu
from InquirerPy import inquirer
from Interactive_Json_inspector import InteractiveJsonInspector
import json

class MainMenu(Menu):
    def _list_of_operations(self):
        return {
            "get_shared_secret_nonce": self.get_shared_secret_nonce,
            "Admin - Who am I": self.admin_who_am_i,
            "Check username availability": self.is_username_availaivble,
            "get_capabilities": self.get_capabilities,
            "server sync": self.get_sync,
            "get_display_name": self.get_display_name,
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
        if self.menu_context["client"].isUsernameAvailiable(username=username):
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

    def get_display_name(self):
        print("Response:", self.menu_context["client"].get_own_display_name(
            login_session=self.menu_context["login_session"]
        ))

    def get_shared_secret_nonce(self):
        a = self.menu_context["client"].get_shared_secret_nonce()
        print("Nonce=", a)