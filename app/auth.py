import requests
import os
from dotenv import load_dotenv
from kivy.storage.jsonstore import JsonStore
from app.utils import get_data_dir

# Load environment variables
load_dotenv()

# PLACEHOLDERS - USER REPLACEMENT REQUIRED
FIREBASE_API_KEY = os.getenv("FIREBASE_API_KEY", "")
FIREBASE_DB_URL = os.getenv("FIREBASE_DB_URL", "")

AUTH_URL = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_API_KEY}"
SIGNUP_URL = (
    f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={FIREBASE_API_KEY}"
)


class AuthManager:
    def __init__(self):
        self.data_dir = get_data_dir()
        self.auth_store = JsonStore(os.path.join(self.data_dir, "auth_info.json"))
        self._user_token = None
        self._user_local_id = None
        self._email = None

        # Load saved session
        if self.auth_store.exists("session"):
            session = self.auth_store.get("session")
            self._user_token = session.get("idToken")
            self._user_local_id = session.get("localId")
            self._email = session.get("email")

    def is_logged_in(self):
        return self._user_token is not None

    def get_token(self):
        return self._user_token

    def get_user_id(self):
        return self._user_local_id

    def get_email(self):
        return self._email

    def login(self, email, password):
        try:
            payload = {"email": email, "password": password, "returnSecureToken": True}
            response = requests.post(AUTH_URL, json=payload)
            data = response.json()

            if "error" in data:
                return False, data["error"]["message"]

            self._save_session(data)
            return True, "Login realizado com sucesso!"

        except Exception as e:
            return False, str(e)

    def register(self, email, password):
        try:
            payload = {"email": email, "password": password, "returnSecureToken": True}
            response = requests.post(SIGNUP_URL, json=payload)
            data = response.json()

            if "error" in data:
                return False, data["error"]["message"]

            self._save_session(data)
            return True, "Conta criada com sucesso!"

        except Exception as e:
            return False, str(e)

    def logout(self):
        self._user_token = None
        self._user_local_id = None
        self._email = None
        if self.auth_store.exists("session"):
            self.auth_store.delete("session")

    def _save_session(self, data):
        self._user_token = data["idToken"]
        self._user_local_id = data["localId"]
        self._email = data["email"]

        self.auth_store.put(
            "session",
            idToken=self._user_token,
            localId=self._user_local_id,
            email=self._email,
        )


# Singleton instance
auth_manager = AuthManager()
