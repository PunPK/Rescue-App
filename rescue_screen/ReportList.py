from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from pymongo import MongoClient
from kivymd.uix.button import MDIconButton
from kivymd.uix.list import MDList, TwoLineListItem
from kivy.uix.scrollview import ScrollView
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from kivy.core.text import LabelBase
from kivy.core.window import Window
import base64
from io import BytesIO
from PIL import Image as PILImage
from kivy.graphics.texture import Texture


LabelBase.register(name="ThaiFont", fn_regular="fonts/THSarabunNew.ttf")

# MongoDB setup
client = MongoClient("localhost", 27017)
db = client["rescue_app"]
users_collection = db["users"]
reports_collection = db["reports"]
try:
    Builder.load_file("rescue_screen/Screen.kv")
    print("KV file loaded successfully")
except Exception as e:
    print(f"Error loading KV file: {e}")
Window.size = [360, 640]


# ReceiveReportScreen class
class ReportList(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "home"

        # Main layout
        layout = MDBoxLayout(orientation="vertical")

        # Top app bar (toolbar)
        toolbar = MDTopAppBar(title="Reports list", elevation=0, pos_hint={"top": 1})
        layout.add_widget(toolbar)

        # Scrollable list container
        scroll_view = ScrollView()

        # Content - List of cards (top to bottom)
        self.card_list = MDList()
        self.card_list.bind(
            minimum_height=self.card_list.setter("height")
        )  # Expand properly

        self.load_cards()

        scroll_view.add_widget(self.card_list)
        layout.add_widget(scroll_view)

        self.add_widget(layout)

        # Floating Action Button (FAB) to create a new report

    def load_cards(self):
        self.card_list.clear_widgets()
        reports = reports_collection.find()

        for report in reports:
            location = report.get("location", "Unknown Location")
            timestamp = report.get("timestamp", "Unknown Time")
            item = TwoLineListItem(
                text=f"Location: {location}",
                secondary_text=f"Time: {timestamp}",
            )
            item.bind(
                on_release=lambda x, report=report: self.view_report_details(report)
            )

            self.card_list.add_widget(item)

    def view_report_details(self, report):
        self.manager.current = "report_details_screen"
        report_details_screen = self.manager.get_screen("report_details_screen")
        report_details_screen.show_report_details(report)


class ReportDetailsScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "report_details_screen"

    def show_report_details(self, report):
        self.ids.report_location.text = f"Location: {report.get('location', 'Unknown')}"
        self.ids.report_timestamp.text = (
            f"Timestamp: {report.get('timestamp', 'Unknown')}"
        )
        self.ids.report_description.text = (
            f"Description: {report.get('description', 'No Description')}"
        )
        self.ids.report_location.font_name = "ThaiFont"
        self.ids.report_timestamp.font_name = "ThaiFont"
        self.ids.report_description.font_name = "ThaiFont"

        image_data = report.get("image", None)

        if image_data:
            try:
                image_bytes = base64.b64decode(image_data)
                image = PILImage.open(BytesIO(image_bytes))

                image = image.convert("RGBA")
                img_data = image.tobytes()

                texture = Texture.create(
                    size=(image.width, image.height), colorfmt="rgba"
                )
                texture.blit_buffer(img_data, colorfmt="rgba", bufferfmt="ubyte")

                self.ids.report_image.texture = texture

            except Exception as e:
                print(f"Error loading image: {e}")
                self.ids.report_image.source = "image.jpg"
        else:
            self.ids.report_image.source = "image.jpg"


class MyApp(MDApp):
    def build(self):
        # Create a ScreenManager to handle screen transitions
        screen_manager = MDScreenManager()
        screen_manager.add_widget(ReportList(name="home"))
        screen_manager.add_widget(ReportDetailsScreen(name="report_details_screen"))
        return screen_manager


# Run the app
if __name__ == "__main__":
    MyApp().run()
