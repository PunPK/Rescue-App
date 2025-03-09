import cv2
import base64
import requests
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.screen import MDScreen
from kivy_garden.mapview import MapView, MapMarker
from kivy.lang import Builder
from kivy.core.window import Window
import platform
from pymongo import MongoClient
from datetime import datetime

# from plyer import gps

client = MongoClient("localhost", 27017)
db = client["rescue_app"]
users_collection = db["users"]
reports_collection = db["reports"]

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

Builder.load_file("rescue_screen/Screen.kv")

Window.size = (430, 740)


class ReceiverScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.mapview = MapView(zoom=13, lat=7.00724, lon=100.50176)
        self.ids.map_container.add_widget(self.mapview)
        self.marker = None
        self.current_location = None
        self.get_location_from_ip()

        self.camera_index = None
        self.capture = None
        self.image_widget = None
        self.layout = None
        self.captured_image_widget = None

        self.add_map()

    def get_location_from_ip(self):
        try:
            response = requests.get("https://ipinfo.io")
            data = response.json()
            loc = data["loc"].split(",")
            lat, lon = float(loc[0]), float(loc[1])
            print(f"Location from IP: lat={lat}, lon={lon}")
            self.current_location = [lat, lon]

            if self.marker:
                self.mapview.remove_marker(self.marker)
            self.marker = MapMarker(lat=lat, lon=lon)
            self.mapview.add_marker(self.marker)

        except Exception as e:
            print(f"Error fetching location from IP: {e}")

    def update_current_location(self, *args):
        self.get_location_from_ip()
        print(f"Using real-time IP-based location: {self.current_location}")

    def add_map(self):
        self.marker = MapMarker(lat=7.00724, lon=100.50176)
        self.mapview.add_marker(self.marker)

        get_location_btn = Button(
            text="Get Current Location", size_hint=(1, None), height="50dp"
        )
        get_location_btn.bind(on_press=self.update_current_location)
        self.ids.map_container.add_widget(get_location_btn)

    # def setup_gps(self):
    #     try:
    #         gps.configure(
    #             on_location=self.on_gps_location, on_status=self.on_gps_status
    #         )
    #         gps.start(minTime=1000, minDistance=1)
    #         print("GPS Started Successfully")

    #     except NotImplementedError:
    #         print("GPS not implemented on this platform.")
    #     except Exception as e:
    #         print(f"Error starting GPS: {e}")

    # def on_gps_location(self, **kwargs):
    #     lat = kwargs.get("lat", 0)
    #     lon = kwargs.get("lon", 0)
    #     print(f"GPS Callback Received: lat={lat}, lon={lon}")  # Debugging print

    #     if lat == 0 and lon == 0:
    #         print("Warning: GPS data is not updating correctly.")

    #     self.current_location = [lat, lon]

    #     if self.marker:
    #         self.mapview.remove_marker(self.marker)
    #     self.marker = MapMarker(lat=lat, lon=lon)
    #     self.mapview.add_marker(self.marker)

    # def on_gps_status(self, status):
    #     print(f"GPS Status: {status}")

    # def update_current_location(self, *args):
    #     self.setup_gps()
    #     print(f"Using real-time GPS location: {self.current_location}")

    # def add_map(self):
    #     self.marker = MapMarker(lat=7.00724, lon=100.50176)
    #     self.mapview.add_marker(self.marker)

    #     get_location_btn = Button(
    #         text="Get Current Location", size_hint=(1, None), height="50dp"
    #     )
    #     get_location_btn.bind(
    #         on_press=self.update_current_location
    #     )  # Update location based on IP
    #     self.ids.map_container.add_widget(get_location_btn)

    def setup_camera(self):
        if platform.system() == "Darwin":
            self.camera_index = 0
        elif platform.system() == "Linux":
            self.camera_index = 2
        elif platform.system() == "Windows":
            self.camera_index = 1
        else:
            print("ใช้ไม่ได้บอก Hopeeee")
            return

        if not self.layout:
            self.layout = BoxLayout(orientation="vertical", size_hint=(1, 1))
            self.image_widget = Image(size_hint=(1, 1))
            self.layout.add_widget(self.image_widget)

        self.ids.cam_container.add_widget(self.layout)

        self.capture = cv2.VideoCapture(self.camera_index)
        if not self.capture.isOpened():
            print("Error: Could not open camera.")
        else:
            print("Camera opened successfully!")
            Clock.schedule_interval(self.update, 1.0 / 30.0)
            self.ids.open_cam_button.opacity = 0

    def update(self, dt):
        try:
            # Read a frame from the video capture
            ret, frame = self.capture.read()

            if ret:
                print("Frame captured successfully.")
                frame = cv2.rotate(frame, cv2.ROTATE_180)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB format

                texture = Texture.create(
                    size=(frame.shape[1], frame.shape[0]), colorfmt="rgb"
                )
                texture.blit_buffer(frame.tobytes(), colorfmt="rgb", bufferfmt="ubyte")

                # Update the image widget with the texture
                self.image_widget.texture = texture
            else:
                print("Error: Could not read frame.")
        except Exception as e:
            print(f"An error occurred while updating the frame: {e}")

    def capture_photo(self):
        try:
            self.update_current_location()
            ret, frame = self.capture.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.flip(frame, 0)
                # Encode the image as base64 to store it in the database
                _, buffer = cv2.imencode(".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
                self.img_str = base64.b64encode(buffer).decode("utf-8")

                print("Photo captured. Ready to send in report.")
                self.show_popup("Success", "Photo captured successfully!")
                self.ids.photo_container.opacity = 1

                if not self.captured_image_widget:
                    self.captured_image_widget = Image()
                    self.ids.photo_container.add_widget(
                        self.captured_image_widget, index=1
                    )

                texture = Texture.create(
                    size=(frame.shape[1], frame.shape[0]), colorfmt="rgb"
                )
                texture.blit_buffer(frame.tobytes(), colorfmt="rgb", bufferfmt="ubyte")
                self.captured_image_widget.texture = texture
            else:
                print("Error: Could not capture the photo.")
                self.show_popup("Error", "Failed to capture the photo.")
        except Exception as e:
            print(f"An error occurred while capturing the photo: {e}")
            self.show_popup("Error", f"An error occurred: {e}")

    def send_report(self):
        try:
            self.update_current_location()
            location = self.ids.location_input.text
            description = self.ids.description_input.text

            if location and description:
                report = {
                    "location": location,
                    "description": description,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
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
                self.on_stop()
                self.show_popup("Success", "Report sent successfully!")
            else:
                # Show error message if fields are not filled
                self.show_popup("Error", "Please fill all fields!")
        except Exception as e:
            print(f"An error occurred while sending the report: {e}")
            self.show_popup("Error", f"An error occurred: {e}")

    def show_popup(self, title, message):
        popup = Popup(
            title=title,
            content=Label(text=message),
            size_hint=(0.8, 0.4),
        )
        popup.open()

    def on_stop(self):
        if self.capture and self.capture.isOpened() or self.setup_camera():
            self.capture.release()
            self.capture = None
            Clock.unschedule(self.update)

        if self.layout and self.layout in self.ids.cam_container.children:
            self.ids.cam_container.remove_widget(self.layout)
            self.layout = None
            self.image_widget = None
