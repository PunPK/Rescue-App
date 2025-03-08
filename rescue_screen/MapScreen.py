from kivy.lang import Builder
from kivy.uix.button import Button
from kivy_garden.mapview import MapView, MapMarker
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from geopy.geocoders import Nominatim
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.screenmanager import ScreenManager
from kivy.clock import Clock

Window.size = (360, 640)

KV = """
<MapViewScreen>:
    MDBoxLayout:
        orientation: 'vertical'
        spacing: 10

        BoxLayout:
            size_hint_y: None
            height: '60dp'
            padding: [10, 0]
            canvas.before:
                Color:
                    rgba: utils.get_color_from_hex('#023282')  # Dark blue header
                Rectangle:
                    pos: self.pos
                    size: self.size

            Image:
                source: 'Image/logo.png'
                size_hint: (None, None)
                size: (50, 50)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            Label:
                text: 'Map View'
                font_name: 'ThaiFont'
                font_size: '20sp'
                color: 1, 1, 1, 1
                halign: 'left'
                text_size: self.size
                valign: 'center'
                padding_x: 10

        MapView:
            id: mapview
            zoom: 15
            lat: 7.00724
            lon: 100.50176
            size_hint: (1, 1)  # Make the MapView take up all available space

        MDBoxLayout:
            adaptive_height: True
            md_bg_color: (1, 1, 1, 1)
            padding: [0, dp(5), 0, dp(5)]
            spacing: dp(10)

            BottomNavItem:
                icon: "compass-outline"
                text: "Explore"
                screen_name: "main"

            BottomNavItem:
                icon: "file-document-outline"
                text: "Reports"
                screen_name: "receiver"

            BottomNavItem:
                icon: "account-box-multiple"
                text: "Officer"
                screen_name: "officer"

            BottomNavItem:
                icon: "account-outline"
                text: "Login"
                screen_name: "login"
"""

Builder.load_string(KV)


class BottomNavItem(MDBoxLayout):
    icon = StringProperty("")
    text = StringProperty("")
    selected = BooleanProperty(False)
    screen_name = StringProperty("")

    def navigate(self):
        app = MDApp.get_running_app()
        app.root.current = self.screen_name


class MapViewScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.marker = None
        self.current_location = [7.00724, 100.50176]

        # Schedule adding widgets after the widget tree is built
        Clock.schedule_once(self.setup_map)

    def setup_map(self, dt):
        # Add map markers and controls here
        self.marker = MapMarker(lat=7.00724, lon=100.50176)
        self.ids.mapview.add_marker(self.marker)

        # Add a button to get current location
        get_location_btn = Button(
            text="Get Current Location", size_hint=(1, None), height="50dp"
        )
        get_location_btn.bind(on_press=self.update_current_location)
        self.ids.mapview.add_widget(get_location_btn)

    def get_current_location(self, instance):
        # This method can be used to update location based on GPS or other methods
        print(f"Current Location: {self.current_location}")

    def update_current_location(self, *args):
        try:
            # Update the current location based on GPS or other methods
            geolocator = Nominatim(user_agent="rescue_app")
            location = geolocator.geocode("R202")
            if location:
                self.current_location = [location.latitude, location.longitude]
                print(f"Updated current location: {self.current_location}")
                self.ids.mapview.center_on(location.latitude, location.longitude)
                if self.marker:
                    self.marker.lat = location.latitude
                    self.marker.lon = location.longitude
            else:
                print("Could not get the current location")
        except Exception as e:
            print(f"An error occurred while updating the current location: {e}")


class RescueApp(MDApp):
    def build(self):
        return MapViewScreen()


if __name__ == "__main__":
    RescueApp().run()
