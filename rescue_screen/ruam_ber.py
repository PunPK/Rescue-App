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
from kivymd.uix.list import MDList, TwoLineListItem
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.metrics import dp
from pymongo import MongoClient, errors
from rescue_screen.HomePage import BottomNavItem

Window.size = (360, 640)

client = MongoClient("localhost", 27017)
db = client["rescue_app"]
numbers_info_collection = db["numbers_info"]


class Ruem_ber(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "officer"

        layout = MDBoxLayout(orientation="vertical")

        toolbar = MDTopAppBar(
            title="Officer Phone number", elevation=0, pos_hint={"top": 1}
        )
        toolbar.left_action_items = [["arrow-left", lambda x: self.go_back()]]
        layout.add_widget(toolbar)

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
                icon="account-box-multiple",
                text="Officer",
                selected=True,
                screen_name="officer",
            )
        )

        bottom_nav.add_widget(
            BottomNavItem(icon="account-outline", text="Login", screen_name="login")
        )

        scroll_view = ScrollView()

        self.card_list = MDList()
        self.card_list.bind(minimum_height=self.card_list.setter("height"))

        self.load_cards()
        scroll_view.add_widget(self.card_list)
        layout.add_widget(scroll_view)
        layout.add_widget(bottom_nav)
        self.add_widget(layout)

    def load_cards(self):
        self.card_list.clear_widgets()
        numbers_info_data = numbers_info_collection.find()

        for i in numbers_info_data:
            item = TwoLineListItem(
                text=f"Phone Number: {i['phone_number']}",
                secondary_text=f"Agency: {i['agency']}",
            )
            self.card_list.add_widget(item)

    def go_back(self, *args):
        self.manager.current = "main"
