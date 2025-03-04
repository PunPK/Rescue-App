from gps3 import gps3
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock


class GPSApp(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical")
        self.label = Label(text="Waiting for GPS data...", font_size="20sp")
        self.layout.add_widget(self.label)
        return self.layout

    def on_start(self):
        # Connect to GPSD
        self.gps_socket = gps3.GPSDSocket()
        self.data_stream = gps3.DataStream()
        self.gps_socket.connect()
        self.gps_socket.watch()
        # Schedule GPS updates every second
        Clock.schedule_interval(self.update_gps, 1)

    def update_gps(self, dt):
        # Read GPS data
        for new_data in self.gps_socket:
            if new_data:
                self.data_stream.unpack(new_data)
                lat = self.data_stream.TPV["lat"]
                lon = self.data_stream.TPV["lon"]
                if lat != "n/a" and lon != "n/a":
                    self.label.text = f"Latitude: {lat}\nLongitude: {lon}"

    def on_stop(self):
        # Stop the GPS session when the app is closed
        self.gps_socket.close()


if __name__ == "__main__":
    GPSApp().run()
