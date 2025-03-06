import cv2
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.graphics.texture import Texture


class CameraApp(App):
    def build(self):
        self.capture = cv2.VideoCapture("/dev/video2")
        if not self.capture.isOpened():
            print("Error: Could not open video device.")
            return

        self.layout = BoxLayout(orientation="vertical")
        self.image_widget = Image()  # Create an image widget to display the video

        # Create a button to take a photo
        button = Button(text="Take Photo", size_hint=(1, 0.2), height=50)
        button.bind(
            on_press=self.capture_photo
        )  # Bind the button to capture_photo method

        # Add the button and image widget to the layout
        self.layout.add_widget(button)
        self.layout.add_widget(self.image_widget)

        # Start a Clock event to update the frame at a regular interval
        Clock.schedule_interval(self.update, 1.0 / 30.0)  # Update 30 frames per second
        return self.layout

    def update(self, dt):
        # Read the next frame from the video capture
        ret, frame = self.capture.read()
        if ret:
            # Convert the frame to RGB (Kivy uses RGB format)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Create a texture from the frame
            texture = Texture.create(
                size=(frame.shape[1], frame.shape[0]), colorfmt="rgb"
            )
            texture.blit_buffer(frame.tobytes(), colorfmt="rgb", bufferfmt="ubyte")

            # Update the image widget with the texture
            self.image_widget.texture = texture

    def capture_photo(self, instance):
        # Capture a single frame and save it as a photo when the button is pressed
        ret, frame = self.capture.read()
        if ret:
            # Convert the frame to RGB (Kivy uses RGB format)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Save the photo to a file (you can change the file name as needed)
            photo_filename = "captured_photo.jpg"
            cv2.imwrite(photo_filename, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
            print(f"Photo saved as {photo_filename}")

    def on_stop(self):
        # Release the camera when the app stops
        if self.capture.isOpened():
            self.capture.release()


if __name__ == "__main__":
    CameraApp().run()
