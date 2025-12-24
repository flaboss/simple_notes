import json
from datetime import datetime
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, StringProperty
from kivy.storage.jsonstore import JsonStore
from kivy.lang import Builder
from kivy.properties import ListProperty, StringProperty, ObjectProperty

store = JsonStore('notes.json')

class NoteListScreen(Screen):
    notes_data = ListProperty([])

    def on_pre_enter(self):
        # loads the notes when the screen is about to be entered 
        self.load_notes()

    def load_notes(self):
        # Transform stored notes into a list
        temp_notes = []
        for key in store.keys():
            note = store.get(key)
            temp_notes.append({
                'id': key,
                'title': note['title'],
                'date': note['date']
            })
        
        self.notes_data = sorted(temp_notes, key=lambda x: x['date'], reverse=True)

    def open_note(self, note_id):
        self.manager.transition.direction = 'left'
        self.manager.get_screen('view').note_id = note_id
        self.manager.current = 'view'

class CreateNoteScreen(Screen):
    def save_note(self, title, content):
        if not title.strip(): return  # Title is required

        note_id = str(datetime.now().timestamp())
        date_str = datetime.now().strftime("%d/%m/%Y %H:%M")
        store.put(note_id, title=title, content=content, date=date_str)
        self.manager.current = 'list' # Go back to the list screen
    
class ConfirmPopup(BoxLayout):
    def __init__(self, on_confirm, **kwargs):
        super().__init__(**kwargs)
        self.on_confirm = on_confirm
        self.popup = None

class ViewNoteScreen(Screen):
    note_id = StringProperty('')

    def on_pre_enter(self):
        note = store.get(self.note_id)
        self.ids.title_input.text = note['title']
        self.ids.content_input.text = note['content']
    
    def save_changes(self):
        # atualiza a nota existente
        store.put(self.note_id,
                  title=self.ids.title_input.text,
                  content=self.ids.content_input.text,
                  date=datetime.now().strftime("%d/%m/%Y %H:%M"))
        self.manager.current = 'list'
    
    def show_delete_confirmation(self):
        # cria o conteudo do popup
        content = ConfirmPopup(on_confirm=self.delete_note)
        popup = Popup(title='Confirmar Exclusão',
                      content=content,
                      size_hint=(0.8, 0.4),
                      auto_dismiss=True)
        content.popup = popup
        popup.open()
    
    def delete_note(self):
        self.manager.transition.direction = 'right'
        store.delete(self.note_id)
        self.manager.current = 'list'

class NoteApp(App):
    def build(self):
        # loads the design file
        Builder.load_file('notes.kv')

        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(NoteListScreen(name='list'))
        sm.add_widget(CreateNoteScreen(name='create'))
        sm.add_widget(ViewNoteScreen(name='view'))
        return sm

if __name__ == '__main__':
    NoteApp().run()
