from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import ListProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

from database import NoteManager


class NoteListScreen(Screen):
    notes_data = ListProperty([])

    def on_pre_enter(self):
        self.notes_data = NoteManager.get_all()

    def open_note(self, note_id):
        self.manager.transition.direction = "left"
        self.manager.get_screen("view").note_id = note_id
        self.manager.current = "view"


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
        Builder.load_file("ui/style.kv")
        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(NoteListScreen(name="list"))
        sm.add_widget(CreateNoteScreen(name="create"))
        sm.add_widget(ViewNoteScreen(name="view"))
        return sm


if __name__ == "__main__":
    NotesApp().run()
