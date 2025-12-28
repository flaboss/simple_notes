from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import ListProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.factory import Factory

from database import NoteManager


class NoteListScreen(Screen):
    notes_data = ListProperty([])
    filtered_notes = ListProperty([])

    def on_pre_enter(self):
        self.notes_data = NoteManager.get_all()
        self.filtered_notes = self.notes_data
        self.ids.search_input.text = ""
        self.populate_notes()

    def filter_notes(self, query):
        if not query.strip():
            self.filtered_notes = self.notes_data
        else:
            self.filtered_notes = [n for n in self.notes_data if query.lower() in n["title"].lower() or query.lower() in n["content"].lower()]

        # update UI
        self.populate_notes()

    def open_note(self, note_id):
        self.manager.transition.direction = "left"
        self.manager.get_screen("view").note_id = note_id
        self.manager.current = "view"

    def populate_notes(self):
        box = self.ids.get('notes_box')
        if not box:
            return
        box.clear_widgets()
        for item in self.filtered_notes:
            btn = Factory.NoteItem(text=f"{item['title']}\n[color=888888][size=13sp]{item['date']}[/size][/color]", markup=True)
            btn.bind(on_release=lambda inst, id=item['id']: self.open_note(id))
            box.add_widget(btn)


class CreateNoteScreen(Screen):
    def save_note(self, title, content):
        if not title.strip():
            return
        NoteManager.save(title, content)
        self.manager.transition.direction = "right"
        self.manager.current = "list"


class ViewNoteScreen(Screen):
    note_id = StringProperty("")

    def on_pre_enter(self):
        note = NoteManager.get_one(self.note_id)
        if note:
            self.ids.title_input.text = note["title"]
            self.ids.content_input.text = note["content"]

    def save_changes(self):
        NoteManager.update(
            self.note_id, self.ids.title_input.text, self.ids.content_input.text
        )
        self.manager.transition.direction = "right"
        self.manager.current = "list"

    def show_delete_confirmation(self):
        content = ConfirmPopup(on_confirm=self.delete_note)
        self.popup = Popup(
            title="Confirmar Exclusão", content=content, size_hint=(0.8, 0.4)
        )
        content.popup = self.popup
        self.popup.open()

    def delete_note(self):
        NoteManager.delete(self.note_id)

        # Fechamos o popup após a exclusão
        if hasattr(self, "popup"):
            self.popup.dismiss()

        self.manager.transition.direction = "right"
        self.manager.current = "list"


class ConfirmPopup(BoxLayout):
    def __init__(self, on_confirm, **kwargs):
        super().__init__(**kwargs)
        self.on_confirm = on_confirm
        self.popup = None


class NotesApp(App):
    def build(self):
        print('DEBUG: NotesApp.build() called')
        Builder.load_file("ui/style.kv")
        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(NoteListScreen(name="list"))
        sm.add_widget(CreateNoteScreen(name="create"))
        sm.add_widget(ViewNoteScreen(name="view"))
        print('DEBUG: NotesApp.build() returning ScreenManager')
        return sm

    def on_start(self):
        print('DEBUG: NotesApp.on_start()')


if __name__ == "__main__":
    NotesApp().run()
