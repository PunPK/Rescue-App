from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.label import Label

# from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from pymongo import MongoClient, errors

# from kivy.core.text import LabelBase
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
import gridfs
from kivy_garden.mapview import MapView, MapMarker

from kivy.lang import Builder


from kivy.core.window import Window

Builder.load_file("rescue_screen/Screen.kv")

Window.size = (430, 740)

client = MongoClient("localhost", 27017)
db = client["rescue_app"]
users_collection = db["users"]
reports_collection = db["reports"]
fs = gridfs.GridFS(db)

# ตรวจสอบและสร้างข้อมูลผู้ใช้และรายงานหากไม่มี
if users_collection.count_documents({}) == 0:
    users_collection.insert_many(
        [
            {"username": "admin", "password": "admin123", "role": "admin"},
            {"username": "user", "password": "user123", "role": "user"},
        ]
    )

# ตรวจสอบว่าคอลเลกชัน reports ว่างเปล่า
if reports_collection.count_documents({}) == 0:
    # เพิ่มเอกสารเริ่มต้นหากคอลเลกชันว่าง
    reports_collection.insert_one(
        {"location": "Initial Location", "description": "Initial Description"}
    )


class ReceiverScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mapview = MapView(
            zoom=15, lat=7.00724, lon=100.50176
        )  # Default in CoE PSU
        self.ids.map_container.add_widget(self.mapview)
        self.marker = None
        self.current_location = [7.00724, 100.50176]

    # def start_gps(self):
    #     try:
    #         gps.configure(
    #             on_location=self.on_gps_location, on_status=self.on_gps_status
    #         )
    #         gps.start()
    #     except NotImplementedError:
    #         print("GPS is not supported on this platform.")

    # def on_gps_location(self, **kwargs):
    #     lat = kwargs.get("lat")
    #     lon = kwargs.get("lon")

    #     if lat is not None and lon is not None:
    #         self.current_location = (lat, lon)
    #         if self.mapview:
    #             self.mapview.center_on(lat, lon)

    #         if self.marker:
    #             self.marker.lat = lat
    #             self.marker.lon = lon
    #         else:
    #             self.marker = MapMarker(lat=lat, lon=lon)
    #             self.mapview.add_marker(self.marker)

    def send_report(self):
        location = self.ids.location_input.text
        description = self.ids.description_input.text
        # image_path = self.ids.image_input.text

        if location and description:
            report = {"location": location, "description": description}
            if self.current_location:
                report["latitude"] = self.current_location[0]
                report["longitude"] = self.current_location[1]

            # อัปโหลดรูปภาพเข้า MongoDB GridFS
            # if image_path:
            #     with open(image_path, "rb") as image_file:
            #         image_id = fs.put(image_file, filename=os.path.basename(image_path))
            #     report["image_id"] = str(image_id)

            # เพิ่มรายงานใหม่ใน MongoDB
            reports_collection.insert_one(report)

            # ล้างช่อง input
            self.ids.location_input.text = ""
            self.ids.description_input.text = ""
            # self.ids.image_input.text = ""

            # แสดง Popup แจ้งเตือน
            popup = Popup(
                title="Success",
                content=Label(text="Report sent successfully!"),
                size_hint=(0.8, 0.4),
            )
            popup.open()
        else:
            popup = Popup(
                title="Error",
                content=Label(text="Please fill all fields!"),
                size_hint=(0.8, 0.4),
            )
            popup.open()

    def open_file_chooser(self):
        filechooser = FileChooserListView()
        popup = Popup(
            title="Select Image",
            content=filechooser,
            size_hint=(0.9, 0.9),
        )

    def on_selection(instance, selection):
        if selection:
            self.ids.image_input.text = selection[0]  # เก็บที่อยู่ไฟล์
        popup.dismiss()
        filechooser.bind(on_submit=on_selection)
        popup.open()

    def add_map(self):
        self.mapview = MapView(zoom=15, lat=13.7563, lon=100.5018)  # Default to Bangkok
        self.marker = MapMarker(lat=13.7563, lon=100.5018)
        self.mapview.add_marker(self.marker)
        self.ids.map_container.add_widget(self.mapview)

        # Add a button to get current location
        get_location_btn = Button(
            text="Get Current Location", size_hint=(1, None), height="50dp"
        )
        get_location_btn.bind(on_press=lambda instance: self.start_gps())
        self.ids.map_container.add_widget(get_location_btn)

    def load_reports(self):
        reports = reports_collection.find()

        # ล้างรายการเก่า
        self.ids.reports_container.clear_widgets()

        # แสดงรายงานใหม่
        for report in reports:
            report_text = f"Location: {report['location']}\nDescription: {report['description']}\n"
            self.ids.reports_container.add_widget(
                Label(
                    text=report_text, font_name="ThaiFont", size_hint_y=None, height=100
                )
            )
