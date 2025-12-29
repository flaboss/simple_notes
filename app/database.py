import logging
import os
import requests
from kivy.storage.jsonstore import JsonStore
from datetime import datetime
from app.auth import auth_manager, FIREBASE_DB_URL
from app.utils import get_data_dir

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# funtion to define the storage
def get_store(filename="notes.json"):
    data_dir = get_data_dir()
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    full_path = os.path.join(data_dir, filename)

    try:
        return JsonStore(full_path)
    except Exception as e:
        logger.error(f"Erro ao carregar o arquivo de dados {full_path}: {e}")
        return JsonStore(os.path.join(data_dir, ".temp_notes.json"))


store = get_store()


class NoteManager:
    enable_sync = True

    @staticmethod
    def set_storage(filename):
        # allows changing the storage file
        global store
        store = get_store(filename)

    @staticmethod
    def _sync_from_remote():
        if not NoteManager.enable_sync or not auth_manager.is_logged_in():
            return

        try:
            uid = auth_manager.get_user_id()
            token = auth_manager.get_token()
            url = f"{FIREBASE_DB_URL}/users/{uid}/notes.json?auth={token}"

            response = requests.get(url)
            if response.status_code == 200 and response.json():
                remote_notes = response.json()
                # Update local store with remote data
                for note_id, note_data in remote_notes.items():
                    store.put(note_id, **note_data)
        except Exception as e:
            logger.error(f"Sync error (pull): {e}")

    @staticmethod
    def _sync_to_remote(note_id, data, method="PUT"):
        if not NoteManager.enable_sync or not auth_manager.is_logged_in():
            return

        try:
            uid = auth_manager.get_user_id()
            token = auth_manager.get_token()
            url = f"{FIREBASE_DB_URL}/users/{uid}/notes/{note_id}.json?auth={token}"

            if method == "PUT":
                requests.put(url, json=data)
            elif method == "DELETE":
                requests.delete(url)
        except Exception as e:
            logger.error(f"Sync error (push): {e}")

    @staticmethod
    def get_all():
        try:
            # Try to fetch fresh data if logged in
            NoteManager._sync_from_remote()

            notes = []
            for key in store.keys():
                note = store.get(key)
                note["id"] = key
                notes.append(note)
            # Ordena por data (mais recente primeiro)
            return sorted(notes, key=lambda x: x["date"], reverse=True)
        except Exception as e:
            logger.error(f"Erro ao recuperar as notas: {e}")
            return []

    @staticmethod
    def get_one(note_id):
        if store.exists(note_id):
            return store.get(note_id)
        return None

    @staticmethod
    def save(title, content):
        try:
            note_id = str(datetime.now().timestamp()).replace(".", "")
            date_str = datetime.now().strftime("%d/%m/%Y %H:%M")
            data = {"title": title, "content": content, "date": date_str}

            store.put(note_id, **data)
            NoteManager._sync_to_remote(note_id, data, "PUT")
            return True
        except Exception as e:
            logger.error(f"Erro ao salvar a nota: {e}")
            return False

    @staticmethod
    def update(note_id, title, content):
        try:
            date_str = datetime.now().strftime("%d/%m/%Y %H:%M")
            data = {"title": title, "content": content, "date": date_str}

            store.put(note_id, **data)
            NoteManager._sync_to_remote(note_id, data, "PUT")
            return True
        except Exception as e:
            logger.error(f"Update error: {e}")
            return False

    @staticmethod
    def delete(note_id):
        try:
            if store.exists(note_id):
                store.delete(note_id)
                NoteManager._sync_to_remote(note_id, None, "DELETE")
                return True
            return False
        except Exception as e:
            logger.error(f"Erro ao deletar a nota: {e}")
            return False

    @staticmethod
    def search(query):
        try:
            query = query.lower()
            all_notes = NoteManager.get_all()
            if not query:
                return all_notes

            return [
                n
                for n in all_notes
                if query in n["title"].lower() or query in n["content"].lower()
            ]
        except Exception as e:
            logger.error(f"Erro ao buscar notas: {e}")
            return []
