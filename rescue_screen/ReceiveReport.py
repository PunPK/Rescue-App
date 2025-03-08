from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.uix.boxlayout import BoxLayout
from pymongo import MongoClient
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar.toolbar import MDTooltip  # ใช้ MDToolbar แทน MDTopAppBar
from kivymd.uix.button import MDIconButton
from kivymd.uix.list import MDList, TwoLineListItem
from kivy.uix.scrollview import ScrollView


# MongoDB setup
try:
    client = MongoClient("localhost", 27017)
    db = client["rescue_app"]
    reports_collection = db["reports"]

    Builder.load_file("rescue_screen/Screen.kv")
except Exception as e:
    print(f"An error occurred: {e}")


class ReceiveReportScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "home"

        # Main layout
        layout = MDBoxLayout(orientation="vertical")

        # Top app bar (toolbar)
        toolbar = MDTooltip(
            title="My Cards", elevation=0, pos_hint={"top": 1}
        )  # ใช้ MDTopAppBar
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

        icon_button = MDIconButton(
            icon="plus",  # เลือกไอคอนที่ต้องการ
            pos_hint={"center_x": 0.85, "center_y": 0.1},
            on_release=self.go_to_create_card,
        )
        self.add_widget(icon_button)

    def load_cards(self):
        self.card_list.clear_widgets()
        reports = reports_collection.find()

        for report in reports:
            # Create a TwoLineListItem for each report
            item = TwoLineListItem(
                text=f"Location: {report['location']}",
                secondary_text=f"Time: {report['timestamp']}",
                on_release=lambda x, report=report: self.edit_card(
                    report
                ),  # Fix lambda to capture current report
            )
            self.card_list.add_widget(item)

            # Adding additional description with a label
            description_label = MDLabel(
                text=f"Description: {report['description']}",
                theme_text_color="Secondary",
                size_hint_y=None,
                height="40dp",
            )
            self.card_list.add_widget(description_label)

    def edit_card(self, report):
        # Logic to edit the card
        print(f"Editing report: {report}")
        # Add the edit card functionality here

    def go_to_create_card(self, instance):
        # Logic for the Floating Action Button (FAB)
        print("Navigating to create card")
        # Add the navigation to create card screen here
