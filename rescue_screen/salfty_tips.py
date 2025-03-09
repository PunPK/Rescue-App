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
from rescue_screen.HomePage import BottomNavItem

# Set window size to mobile dimensions (360x640)
Window.size = (360, 640)

client = MongoClient("localhost", 27017)
db = client["rescue_app"]
tips_info_collection = db["safty_tips"]


class Tips_page(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "tipsview"

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

        bottom_nav = MDBoxLayout(adaptive_height=True, md_bg_color=(1, 1, 1, 1))

        bottom_nav.add_widget(
            BottomNavItem(
                icon="compass-outline",
                text="Explore",
                screen_name="main",
            )
        )

        bottom_nav.add_widget(
            BottomNavItem(
                icon="file-document-outline", text="Reports", screen_name="receiver"
            )
        )

        bottom_nav.add_widget(
            BottomNavItem(
                icon="account-box-multiple", text="Officer", screen_name="officer"
            )
        )

        bottom_nav.add_widget(
            BottomNavItem(icon="account-outline", text="Login", screen_name="login")
        )

        scroll_view.add_widget(self.card_list)
        layout.add_widget(scroll_view)
        layout.add_widget(bottom_nav)

        self.add_widget(layout)

    def load_cards(self):
        self.card_list.clear_widgets()
        tip_info_collection = tips_info_collection.find()

        for i in tip_info_collection:
            item = OneLineListItem(
                text=f"name: {i['name']}",
                on_release=lambda x, i=i: webbrowser.open(i["url"]),
            )
            self.card_list.add_widget(item)
