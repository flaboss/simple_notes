from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, BooleanProperty
from app.auth import auth_manager


class LoginScreen(Screen):
    status_message = StringProperty("")
    is_logged_in = BooleanProperty(False)
    user_email = StringProperty("")

    def on_pre_enter(self):
        self.update_auth_status()

    def update_auth_status(self):
        self.is_logged_in = auth_manager.is_logged_in()
        self.user_email = auth_manager.get_email() or ""
        self.status_message = ""

    def do_login(self, email, password):
        if not email or not password:
            self.status_message = "Por favor, preencha todos os campos."
            return

        self.status_message = "Entrando..."
        success, message = auth_manager.login(email, password)
        self.status_message = message

        if success:
            self.update_auth_status()
            # Go back to list and refresh
            self.manager.transition.direction = "right"
            self.manager.get_screen("list").on_pre_enter()  # Force reload
            self.manager.current = "list"

    def do_register(self, email, password):
        if not email or not password:
            self.status_message = "Por favor, preencha todos os campos."
            return

        self.status_message = "Criando conta..."
        success, message = auth_manager.register(email, password)
        self.status_message = message

        if success:
            self.update_auth_status()
            # Go back to list and refresh (auto login happens on register usually?
            # Implementation in auth.py does save session, so yes)
            self.manager.transition.direction = "right"
            self.manager.get_screen("list").on_pre_enter()
            self.manager.current = "list"

    def do_logout(self):
        auth_manager.logout()
        self.update_auth_status()
        self.status_message = "Sessão encerrada."

    def go_back(self):
        self.manager.transition.direction = "right"
        self.manager.current = "list"
