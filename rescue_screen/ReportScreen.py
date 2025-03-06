import cv2
import base64
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy_garden.mapview import MapView, MapMarker
from kivy.lang import Builder
from kivy.core.window import Window
import platform
from pymongo import MongoClient
import gridfs

# MongoDB setup
client = MongoClient("localhost", 27017)
db = client["rescue_app"]
users_collection = db["users"]
reports_collection = db["reports"]
fs = gridfs.GridFS(db)

# Create user and report collections if they don't exist
if users_collection.count_documents({}) == 0:
    users_collection.insert_many(
        [
            {"username": "admin", "password": "admin123", "role": "admin"},
            {"username": "user", "password": "user123", "role": "user"},
        ]
    )

if reports_collection.count_documents({}) == 0:
    reports_collection.insert_one(
        {"location": "Initial Location", "description": "Initial Description"}
    )

# Load KV file for UI
Builder.load_file("rescue_screen/Screen.kv")

Window.size = (430, 740)


class ReceiverScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Map setup
        self.mapview = MapView(zoom=15, lat=7.00724, lon=100.50176)
        self.ids.map_container.add_widget(self.mapview)
        self.marker = None
        self.current_location = [7.00724, 100.50176]

        # Initialize camera and layout

        # Set up the camera
        self.setup_camera()

        # Add map and location button
        self.add_map()

    def setup_camera(self):
        # Set camera index based on platform
        if platform.system() == "Darwin":  # For MacOS
            self.camera_index = 0
        elif platform.system() == "Linux":  # For Linux
            self.camera_index = 2  # Or 0 depending on the number of connected cameras
        elif platform.system() == "Windows":  # For Windows
            self.camera_index = 1  # Or 1 depending on the number of connected cameras
        else:
            print("Unsupported platform for camera setup")
            return

        # Create the layout for the camera feed
        self.layout = BoxLayout(orientation="vertical")
        self.image_widget = Image()  # Image widget to display the video
        self.layout.add_widget(self.image_widget)

        # Add the layout to the screen's container (make sure the screen has a container for widgets)
        self.ids.map_container.add_widget(self.layout)  # Add camera feed layout here

        # Open the camera
        self.capture = cv2.VideoCapture(
            self.camera_index
        )  # Open the camera with the correct index
        if not self.capture.isOpened():
            print("Error: Could not open camera.")
        else:
            print("Camera opened successfully!")
            Clock.schedule_interval(self.update, 1.0 / 30.0)

    def update(self, dt):
        # Read a frame from the video capture
        ret, frame = self.capture.read()

        if ret:
            # Rotate and convert the frame to RGB
            print("Frame captured successfully.")
            frame = cv2.rotate(frame, cv2.ROTATE_180)  # Rotate the frame 180 degrees
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB format

            texture = Texture.create(
                size=(frame.shape[1], frame.shape[0]), colorfmt="rgb"
            )
            texture.blit_buffer(frame.tobytes(), colorfmt="rgb", bufferfmt="ubyte")

            # Update the image widget with the texture
            self.image_widget.texture = texture
        else:
            print("Error: Could not read frame.")

    def capture_photo(self, instance):
        # Capture a single frame when the button is pressed
        ret, frame = self.capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Encode the image as base64 to store it in the database
            _, buffer = cv2.imencode(".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
            self.img_str = base64.b64encode(buffer).decode("utf-8")

            print("Photo captured. Ready to send in report.")

    def send_report(self):
        location = self.ids.location_input.text
        description = self.ids.description_input.text

        if location and description:
            report = {"location": location, "description": description}
            if self.current_location:
                report["latitude"] = self.current_location[0]
                report["longitude"] = self.current_location[1]

            # Include the captured photo in the report
            if hasattr(self, "img_str"):
                report["image"] = self.img_str  # Attach the base64 image

            # Insert the report into MongoDB
            reports_collection.insert_one(report)

            # Reset fields after submission
            self.ids.location_input.text = ""
            self.ids.description_input.text = ""

            # Show success message
            self.show_popup("Success", "Report sent successfully!")
        else:
            # Show error message if fields are not filled
            self.show_popup("Error", "Please fill all fields!")

    def show_popup(self, title, message):
        popup = Popup(
            title=title,
            content=Label(text=message),
            size_hint=(0.8, 0.4),
        )
        popup.open()

    def add_map(self):
        # Add map markers and controls here
        self.marker = MapMarker(lat=7.00724, lon=100.50176)
        self.mapview.add_marker(self.marker)

        # Add a button to get current location
        get_location_btn = Button(
            text="Get Current Location", size_hint=(1, None), height="50dp"
        )
        get_location_btn.bind(on_press=self.get_current_location)
        self.ids.map_container.add_widget(get_location_btn)

    def get_current_location(self, instance):
        # This method can be used to update location based on GPS or other methods
        print(f"Current Location: {self.current_location}")

    def load_reports(self):
        # Fetch reports from the MongoDB database
        reports = reports_collection.find()

        # Clear existing widgets in the reports container
        self.ids.reports_container.clear_widgets()

        # Loop through the fetched reports and display them
        for report in reports:
            report_text = f"Location: {report['location']}\nDescription: {report['description']}\n"
            if "image" in report:
                report_text += "Image: [Image included in the report]\n"
            if "latitude" in report and "longitude" in report:
                report_text += f"Latitude: {report['latitude']}, Longitude: {report['longitude']}\n"

            # Add each report to the container
            self.ids.reports_container.add_widget(
                Label(
                    text=report_text, font_name="ThaiFont", size_hint_y=None, height=100
                )
            )

    def on_stop(self):
        # Release the camera when the app stops
        if self.capture and self.capture.isOpened():
            self.capture.release()
