from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import MDList, TwoLineListItem, OneLineListItem
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.metrics import dp
from pymongo import MongoClient, errors
import webbrowser

# Set window size to mobile dimensions (360x640)
Window.size = (360, 640)

client = MongoClient("localhost", 27017)
db = client["rescue_app"]
tips_info_collection = db["safty_tips"]


class Tips_page(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "tips-page"

        # Main layout
        layout = MDBoxLayout(orientation="vertical")

        # Top app bar
        toolbar = MDTopAppBar(
            title="Safty_tips_management", elevation=0, pos_hint={"top": 1}
        )
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

        fab = MDFloatingActionButton(
            icon="plus",
            pos_hint={"center_x": 0.85, "center_y": 0.1},
            on_release=self.go_to_create_card,
        )
        self.add_widget(fab)

    def load_cards(self):
        self.card_list.clear_widgets()
        tip_info_collection = tips_info_collection.find()

        for i in tip_info_collection:
            item = OneLineListItem(
                text=f"name: {i['name']}",
                on_release=lambda x, i=i: webbrowser.open(i["url"]),
            )
            self.card_list.add_widget(item)
