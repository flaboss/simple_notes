from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from app.auth import auth_manager


class LoginScreen(Screen):
    status_message = StringProperty("")

    def do_login(self, email, password):
        if not email or not password:
            self.status_message = "Por favor, preencha todos os campos."
            return

        self.status_message = "Entrando..."
        success, message = auth_manager.login(email, password)
        self.status_message = message

        if success:
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
            # Go back to list and refresh (auto login happens on register usually?
            # Implementation in auth.py does save session, so yes)
            self.manager.transition.direction = "right"
            self.manager.get_screen("list").on_pre_enter()
            self.manager.current = "list"

    def go_back(self):
        self.manager.transition.direction = "right"
        self.manager.current = "list"
