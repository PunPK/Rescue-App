import os
import datetime
import mimetypes
from bson.binary import Binary
from pymongo import MongoClient
from gridfs import GridFS

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup


class ImageUploadApp(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical")

        self.file_chooser = FileChooserListView()
        self.upload_button = Button(text="Upload Image", size_hint=(1, 0.1))
        self.upload_button.bind(on_press=self.upload_image)

        self.layout.add_widget(self.file_chooser)
        self.layout.add_widget(self.upload_button)

        return self.layout

    def upload_image(self, instance):
        selected = self.file_chooser.selection
        if selected:
            file_path = selected[0]
            file_name = os.path.basename(file_path)

            # Detect file type
            mime_type, _ = mimetypes.guess_type(file_path)
            mime_type = mime_type if mime_type else "application/octet-stream"

            # Connect to MongoDB
            client = MongoClient("localhost", 27017)
            db = client["rescue_app"]
            fs = GridFS(db, collection="media")

            # Upload the file
            with open(file_path, "rb") as f:
                file_id = fs.put(
                    f,
                    filename=file_name,
                    content_type=mime_type,
                    created_date=datetime.datetime.utcnow(),
                    owner="67bla3e8283d6eda8ff7bebc",  # Replace with actual user ID
                    status="active",
                )

            self.show_popup("Success", f"Image uploaded with ID: {file_id}")
        else:
            self.show_popup("Error", "No file selected")

    def show_popup(self, title, message):
        popup_layout = BoxLayout(orientation="vertical")
        popup_label = Label(text=message)
        popup_button = Button(text="Close")
        popup = Popup(title=title, content=popup_layout, size_hint=(0.8, 0.4))

        popup_layout.add_widget(popup_label)
        popup_layout.add_widget(popup_button)

        popup_button.bind(on_press=popup.dismiss)
        popup.open()


if __name__ == "__main__":
    ImageUploadApp().run()
