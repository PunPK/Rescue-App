from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.image import Image as CoreImage
from datetime import datetime
from pymongo import MongoClient
import io
from gridfs import GridFS
from db_connection import reports_collection


class CameraApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        self.camera = Camera(index=0, play=True)
        self.camera.resolution = (640, 480)

        button = Button(text="take photo", size_hint=(1, 0.2), height=50)
        button.bind(on_press=self.capture)

        layout.add_widget(self.camera)
        layout.add_widget(button)

        return layout

    def capture(self, instance):
        texture = self.camera.texture
        image_data = texture.pixels

        # Save image as binary data
        print("Taking photo...")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        image_filename = f"captured_image_{timestamp}.png"

        image_binary = io.BytesIO(image_data)

        fs = GridFS(reports_collection.database)
        file_id = fs.put(
            image_binary.getvalue(), filename=image_filename, content_type="image/png"
        )

        report_data = {
            "image_filename": image_filename,
            "timestamp": timestamp,
            "file_id": file_id,
        }

        reports_collection.insert_one(report_data)
        print("เข้า mongo")


if __name__ == "__main__":
    CameraApp().run()
