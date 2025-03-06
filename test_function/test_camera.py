from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.image import Image as CoreImage


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

    def capture(self, instance):  # ฟังก์ชันถ่ายรูป
        texture = self.camera.texture
        size = texture.size

        # บันทึกภาพเป็นไฟล์
        img = CoreImage(texture, size=size)
        img.save("captured_image.png")
        print("ถ่ายรูป")


if __name__ == "__main__":
    CameraApp().run()
