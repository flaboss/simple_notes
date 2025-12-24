from kivy.storage.jsonstore import JsonStore
from datetime import datetime

# funtion to define the storage
def get_store(filename="notes.json"):
    return JsonStore(filename)

store = get_store()

class NoteManager:
    @staticmethod
    def set_storage(filename):
        # allows changing the storage file
        global store
        store = get_store(filename)

    @staticmethod
    def get_all():
        notes = []
        for key in store.keys():
            note = store.get(key)
            note["id"] = key
            notes.append(note)
        # Ordena por data (mais recente primeiro)
        return sorted(notes, key=lambda x: x["date"], reverse=True)

    @staticmethod
    def get_one(note_id):
        if store.exists(note_id):
            return store.get(note_id)
        return None

    @staticmethod
    def save(title, content):
        note_id = str(datetime.now().timestamp())
        date_str = datetime.now().strftime("%d/%m/%Y %H:%M")
        store.put(note_id, title=title, content=content, date=date_str)

    @staticmethod
    def update(note_id, title, content):
        date_str = datetime.now().strftime("%d/%m/%Y %H:%M")
        store.put(note_id, title=title, content=content, date=date_str)

    @staticmethod
    def delete(note_id):
        if store.exists(note_id):
            store.delete(note_id)
