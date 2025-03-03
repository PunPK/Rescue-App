from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout


class CameraApp(App):
    def build(self):
        layout = BoxLayout()

        camera = Camera(index=0, play=True)
        camera.resolution = (640, 480)

        layout.add_widget(camera)

        return layout


if __name__ == "__main__":
    CameraApp().run()
