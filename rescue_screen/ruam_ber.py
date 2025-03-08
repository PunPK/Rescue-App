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

Window.size = (360, 640)

client = MongoClient("localhost", 27017)
db = client["rescue_app"]
numbers_info_collection = db["numbers_info"]


class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "home"

        # Main layout
        layout = MDBoxLayout(orientation="vertical")

        # Top app bar
        toolbar = MDTopAppBar(
            title="Officer Phone number", elevation=0, pos_hint={"top": 1}
        )
        layout.add_widget(toolbar)

        scroll_view = ScrollView()

        self.card_list = MDList()
        self.card_list.bind(minimum_height=self.card_list.setter("height"))

        self.load_cards()

        scroll_view.add_widget(self.card_list)
        layout.add_widget(scroll_view)

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


class CardApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.theme_style = "Light"

        sm = MDScreenManager()
        sm.add_widget(HomeScreen())
        return sm


if __name__ == "__main__":
    CardApp().run()
