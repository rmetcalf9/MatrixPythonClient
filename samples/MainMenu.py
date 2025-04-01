from _Menu import Menu

class MainMenu(Menu):
    def _list_of_operations(self):
        return {
            "Admin - Who am I": self.admin_who_am_i,
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
