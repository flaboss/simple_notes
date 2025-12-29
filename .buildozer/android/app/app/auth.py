import requests
import os
from dotenv import load_dotenv
from kivy.storage.jsonstore import JsonStore
from app.utils import get_data_dir, resource_path

# Load environment variables
load_dotenv(resource_path(".env"))

# PLACEHOLDERS - USER REPLACEMENT REQUIRED
FIREBASE_API_KEY = os.getenv("FIREBASE_API_KEY", "")
FIREBASE_DB_URL = os.getenv("FIREBASE_DB_URL", "")

AUTH_URL = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_API_KEY}"
SIGNUP_URL = (
    f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={FIREBASE_API_KEY}"
)


class AuthManager:
    def __init__(self):
        self._auth_store = None
        self._user_token = None
        self._user_local_id = None
        self._email = None
        self._initialized = False

    def _ensure_initialized(self):
        if self._initialized:
            return
        
        # Verify API Key
        if not FIREBASE_API_KEY:
            print("ERROR: FIREBASE_API_KEY not found! Check your .env file.")
        else:
            print(f"DEBUG: FIREBASE_API_KEY found (length: {len(FIREBASE_API_KEY)})")

        self.data_dir = get_data_dir()
        self._auth_store = JsonStore(os.path.join(self.data_dir, "auth_info.json"))
        
        # Load saved session
        if self._auth_store.exists("session"):
            session = self._auth_store.get("session")
            self._user_token = session.get("idToken")
            self._user_local_id = session.get("localId")
            self._email = session.get("email")
        
        self._initialized = True

    def is_logged_in(self):
        self._ensure_initialized()
        return self._user_token is not None

    def get_token(self):
        self._ensure_initialized()
        return self._user_token

    def get_user_id(self):
        self._ensure_initialized()
        return self._user_local_id

    def get_email(self):
        self._ensure_initialized()
        return self._email

    def login(self, email, password):
        self._ensure_initialized()
        try:
            payload = {"email": email, "password": password, "returnSecureToken": True}
            print(f"DEBUG: Attempting login for {email} to {AUTH_URL.split('?')[0]}")
            response = requests.post(AUTH_URL, json=payload)
            data = response.json()

            if "error" in data:
                print(f"ERROR: Login failed: {data['error']['message']}")
                return False, data["error"]["message"]

            self._save_session(data)
            return True, "Login realizado com sucesso!"

        except Exception as e:
            return False, str(e)

    def register(self, email, password):
        self._ensure_initialized()
        try:
            payload = {"email": email, "password": password, "returnSecureToken": True}
            print(f"DEBUG: Attempting register for {email} to {SIGNUP_URL.split('?')[0]}")
            response = requests.post(SIGNUP_URL, json=payload)
            data = response.json()

            if "error" in data:
                print(f"ERROR: Register failed: {data['error']['message']}")
                return False, data["error"]["message"]

            self._save_session(data)
            return True, "Conta criada com sucesso!"

        except Exception as e:
            return False, str(e)

    def logout(self):
        self._ensure_initialized()
        self._user_token = None
        self._user_local_id = None
        self._email = None
        if self._auth_store.exists("session"):
            self._auth_store.delete("session")

    def _save_session(self, data):
        self._ensure_initialized()
        self._user_token = data["idToken"]
        self._user_local_id = data["localId"]
        self._email = data["email"]

        self._auth_store.put(
            "session",
            idToken=self._user_token,
            localId=self._user_local_id,
            email=self._email,
        )


# Singleton instance
auth_manager = AuthManager()
