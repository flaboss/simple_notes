import logging
import os
from kivy.storage.jsonstore import JsonStore
from datetime import datetime
from kivy.utils import platform

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_data_dir():
    if platform == 'macosx':
        from os.path import expanduser
        return os.path.join(expanduser("~"), "Library", "Application Support", "MinhasNotas")
    return "."

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
    @staticmethod
    def set_storage(filename):
        # allows changing the storage file
        global store
        store = get_store(filename)

    @staticmethod
    def get_all():
        try:
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
            note_id = str(datetime.now().timestamp())
            date_str = datetime.now().strftime("%d/%m/%Y %H:%M")
            store.put(note_id, title=title, content=content, date=date_str)
        except Exception as e:
            logger.error(f"Erro ao salvar a nota: {e}")
            return False

    @staticmethod
    def update(note_id, title, content):
        date_str = datetime.now().strftime("%d/%m/%Y %H:%M")
        store.put(note_id, title=title, content=content, date=date_str)

    @staticmethod
    def delete(note_id):
        try:
            if store.exists(note_id):
                store.delete(note_id)
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

            return [n for n in all_notes if query in n['title'].lower() or query in n['content'].lower()]
        except Exception as e:
            logger.error(f"Erro ao buscar notas: {e}")
            return []
