from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty
from pymongo import MongoClient, errors
from kivy.core.text import LabelBase
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy_garden.mapview import MapView, MapMarker
from kivy.lang import Builder
from test_camera import CameraApp
from db_connection import reports_collection, users_collection

# Set the window size to simulate a mobile device
Window.size = (360, 640)

# KV string for custom widgets and styling
KV = """
<ServiceCard>:
    orientation: "vertical"
    padding: dp(8)
    size_hint: None, None
    size: dp(100), dp(100)
    radius: dp(15)
    ripple_behavior: True
    md_bg_color: 1, 0.4, 0.1, 1  # Orange color
    
    MDBoxLayout:
        orientation: "vertical"
        adaptive_height: True
        spacing: dp(5)
        padding: dp(5)
        pos_hint: {"center_x": .5}
        
        Image:
            source: root.icon_source
            size_hint: None, None
            size: dp(50), dp(50)
            pos_hint: {"center_x": .5}
            
        MDLabel:
            text: root.title
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            font_style: "Caption"
            adaptive_height: True

<CircularButton>:
    size_hint: None, None
    size: dp(70), dp(70)
    md_bg_color: 1, 0.6, 0.1, 1  # Light orange
    radius: dp(35)
    
    MDBoxLayout:
        orientation: "vertical"
        adaptive_height: True
        spacing: dp(2)
        padding: dp(5)
        pos_hint: {"center_x": .5, "center_y": .5}
        
        Image:
            source: root.icon_source
            size_hint: None, None
            size: dp(40), dp(40)
            pos_hint: {"center_x": .5}
            
        MDLabel:
            text: root.title
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            font_style: "Caption"
            font_size: "10sp"
            adaptive_height: True

<BottomNavItem>:
    orientation: "vertical"
    adaptive_height: True
    spacing: dp(2)
    padding: dp(5)
    
    MDIconButton:
        icon: root.icon
        pos_hint: {"center_x": .5}
        theme_icon_color: "Custom"
        icon_color: (1, 0.6, 0.1, 1) if root.selected else (0.5, 0.5, 0.5, 1)
        on_release: root.navigate()
        
    MDLabel:
        text: root.text
        halign: "center"
        theme_text_color: "Custom"
        text_color: (1, 0.6, 0.1, 1) if root.selected else (0.5, 0.5, 0.5, 1)
        font_style: "Caption"
        adaptive_height: True
"""

Builder.load_string(KV)
Builder.load_file("rescue.kv")

# ตั้งค่าฟอนต์ที่รองรับภาษาไทย
LabelBase.register(name="ThaiFont", fn_regular="../fonts/THSarabunNew.ttf")


# ใช้ฟอนต์ใน Label
label = Label(text="สวัสดี", font_name="ThaiFont")

# เชื่อมต่อกับ MongoDB


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


class ServiceCard(MDCard):
    icon_source = StringProperty("")
    title = StringProperty("")


class CircularButton(MDCard):
    icon_source = StringProperty("")
    title = StringProperty("")


class BottomNavItem(MDBoxLayout):
    icon = StringProperty("")
    text = StringProperty("")
    selected = BooleanProperty(False)
    screen_name = StringProperty("")  # Name of the screen to navigate to

    def navigate(self):
        """Switch to the specified screen."""
        app = MDApp.get_running_app()
        app.root.current = self.screen_name


class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_ui()

    def create_ui(self):
        # Main layout
        main_layout = MDBoxLayout(orientation="vertical")

        # Top app bar with menu icon
        # top_bar = MDBoxLayout(
        #     md_bg_color=(1, 0.6, 0.1, 1),  # Orange color
        #     padding=[dp(10), dp(10), dp(10), dp(10)],
        #     adaptive_height=True,
        # )

        # menu_button = MDIconButton(
        #     icon="menu",
        #     pos_hint={"center_y": 0.5},
        #     theme_icon_color="Custom",
        #     icon_color=(1, 1, 1, 1),
        # )
        # top_bar.add_widget(menu_button)

        # Logo and app name
        logo_layout = MDBoxLayout(
            orientation="vertical",
            adaptive_height=True,
            padding=[0, dp(20), 0, dp(20)],
            md_bg_color=(1, 0.6, 0.1, 1),  # Orange color
        )

        # Logo image in a white circle
        logo_box = MDBoxLayout(
            size_hint=(None, None),
            size=(dp(100), dp(100)),
            pos_hint={"center_x": 0.5},
            padding=dp(10),
        )

        logo_card = MDCard(
            size_hint=(None, None),
            size=(dp(80), dp(80)),
            radius=[dp(40)],
            md_bg_color=(1, 1, 1, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )

        # For testing, we'll use a placeholder for the logo
        logo_image = Image(
            source="../Image/logo.png",  # Replace with your logo or use a placeholder
            size_hint=(None, None),
            # size=(dp(50), dp(50)),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )

        logo_card.add_widget(logo_image)
        logo_box.add_widget(logo_card)
        logo_layout.add_widget(logo_box)

        app_name = MDLabel(
            text="Rescue App",
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_style="H5",
            adaptive_height=True,
        )
        logo_layout.add_widget(app_name)

        Creator_name = MDLabel(
            text="BY 67 [005, 270, 280]",
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_style="H6",
            adaptive_height=True,
        )
        logo_layout.add_widget(Creator_name)

        # Services section
        content_layout = MDBoxLayout(
            orientation="vertical",
            padding=[dp(15), dp(15), dp(15), dp(15)],
            spacing=dp(15),
            md_bg_color=(1, 1, 1, 1),
        )

        services_label = MDLabel(
            text="Services",
            theme_text_color="Primary",
            font_style="H6",
            adaptive_height=True,
        )
        content_layout.add_widget(services_label)

        # Grid for service cards (2 rows of 3 cards)
        services_grid1 = MDBoxLayout(
            adaptive_height=True, spacing=dp(10), padding=[0, dp(5), 0, dp(5)]
        )

        services_grid2 = MDBoxLayout(
            adaptive_height=True, spacing=dp(10), padding=[0, dp(5), 0, dp(5)]
        )

        # Service cards - first row
        services_grid1.add_widget(
            ServiceCard(
                icon_source="map_icon.png",  # Replace with your icon or use a placeholder
                title="Send Rescue\nalert",
            )
        )

        services_grid1.add_widget(
            ServiceCard(icon_source="emergency_icon.png", title="Emergency\nContact")
        )

        services_grid1.add_widget(
            ServiceCard(icon_source="ambulance_icon.png", title="Ambulance")
        )

        # Service cards - second row
        services_grid2.add_widget(
            ServiceCard(icon_source="news_icon.png", title="News")
        )

        services_grid2.add_widget(
            ServiceCard(icon_source="safety_icon.png", title="Safety Tips")
        )

        services_grid2.add_widget(
            ServiceCard(icon_source="bookmarks_icon.png", title="Bookmarks")
        )

        content_layout.add_widget(services_grid1)
        content_layout.add_widget(services_grid2)

        # Circular buttons row
        circular_buttons = MDBoxLayout(
            adaptive_height=True,
            spacing=dp(50),
            padding=[dp(20), dp(20), dp(20), dp(20)],
            pos_hint={"center_x": 0.5},
        )

        circular_buttons.add_widget(
            CircularButton(icon_source="hotline_icon.png", title="HOTLINE")
        )

        # Add a spacer
        circular_buttons.add_widget(MDBoxLayout(size_hint_x=None, width=dp(50)))

        circular_buttons.add_widget(
            CircularButton(icon_source="fire_app_icon.png", title="Fire Rescue App")
        )

        content_layout.add_widget(circular_buttons)

        # Bottom navigation bar
        bottom_nav = MDBoxLayout(adaptive_height=True, md_bg_color=(1, 1, 1, 1))

        bottom_nav.add_widget(
            BottomNavItem(
                icon="compass-outline",
                text="Explore",
                selected=True,
                screen_name="main",
            )
        )

        bottom_nav.add_widget(
            BottomNavItem(
                icon="file-document-outline", text="Reports", screen_name="receiver"
            )
        )

        bottom_nav.add_widget(
            BottomNavItem(icon="message-outline", text="Chat", screen_name="chat")
        )

        bottom_nav.add_widget(
            BottomNavItem(icon="account-outline", text="Profile", screen_name="profile")
        )

        # Add all sections to main layout
        # main_layout.add_widget(top_bar)
        main_layout.add_widget(logo_layout)

        # Wrap content in ScrollView
        scroll_view = ScrollView()
        scroll_view.add_widget(content_layout)
        main_layout.add_widget(scroll_view)

        main_layout.add_widget(bottom_nav)

        self.add_widget(main_layout)


# class ReceiverScreen(MDScreen):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.name = "receiver"
#         self.add_widget(MDLabel(text="Receiver Screen", halign="center"))
class ReceiverScreen(MDScreen):
    def __init__(self, **kwargs):
        super(ReceiverScreen, self).__init__(**kwargs)
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
        # อ่านรายงานจาก MongoDB
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


class FireRescueApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        # Create a screen manager
        self.screen_manager = MDScreenManager()
        # Add screens
        self.screen_manager.add_widget(MainScreen(name="main"))
        self.screen_manager.add_widget(ReceiverScreen(name="receiver"))
        return self.screen_manager


if __name__ == "__main__":
    FireRescueApp().run()
