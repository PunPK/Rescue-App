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

# Set window size to mobile dimensions (360x640)
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
        toolbar = MDTopAppBar(title="My Cards", elevation=0, pos_hint={"top": 1})
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
        numbers_info_data = numbers_info_collection.find()

        for i in numbers_info_data:
            item = TwoLineListItem(
                text=f"Phone Number: {i['phone_number']}",
                secondary_text=f"Agency: {i['agency']}",
                on_release=lambda x, i=i: self.edit_card(i),
            )
            self.card_list.add_widget(item)

    def go_to_create_card(self, instance):
        self.manager.current = "create_card"

    def edit_card(self, card_data):
        self.manager.get_screen("edit_card").set_card_data(card_data)
        self.manager.current = "edit_card"


class CreateCardScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "create_card"

        # Main layout
        layout = MDBoxLayout(orientation="vertical", spacing=dp(10), padding=dp(10))

        # Top app bar
        toolbar = MDTopAppBar(title="Create New Card", elevation=0, pos_hint={"top": 1})
        toolbar.left_action_items = [["arrow-left", lambda x: self.go_back()]]
        layout.add_widget(toolbar)

        # Content layout with padding
        content = MDBoxLayout(
            orientation="vertical",
            spacing=dp(20),
            padding=[dp(15), dp(20), dp(15), dp(20)],
            size_hint_y=None,
            height=dp(500),
        )

        # Card form
        card_form = MDCard(
            orientation="vertical",
            size_hint=(1, None),
            height=dp(450),
            padding=dp(15),
            elevation=2,
            radius=[dp(10)],
        )

        # Form fields
        self.title_field = MDTextField(
            hint_text="Card Title",
            helper_text="Enter the title for your card",
            helper_text_mode="on_focus",
            size_hint_x=1,
            mode="rectangle",
        )

        self.phone_number_field = MDTextField(
            hint_text="Phone Number",
            helper_text="Enter Phone Number",
            helper_text_mode="on_focus",
            multiline=True,
            size_hint_x=1,
            mode="rectangle",
        )

        buttons_layout = MDBoxLayout(
            orientation="horizontal",
            spacing=dp(10),
            size_hint=(1, None),
            height=dp(50),
            padding=[0, dp(20), 0, 0],
        )

        cancel_button = MDFlatButton(
            text="CANCEL", size_hint=(0.5, None), height=dp(50), on_release=self.go_back
        )

        save_button = MDRaisedButton(
            text="SAVE",
            size_hint=(0.5, None),
            height=dp(50),
            md_bg_color=MDApp.get_running_app().theme_cls.primary_color,
            on_release=self.save_card,
        )

        buttons_layout.add_widget(cancel_button)
        buttons_layout.add_widget(save_button)

        card_form.add_widget(self.title_field)
        card_form.add_widget(self.phone_number_field)
        card_form.add_widget(buttons_layout)

        content.add_widget(card_form)

        layout.add_widget(content)

        self.add_widget(layout)

    def go_back(self, *args):
        self.manager.current = "home"

    def save_card(self, instance):
        title = self.title_field.text
        phone_number = self.phone_number_field.text
        data = {"agency": title, "phone_number": phone_number}
        numbers_info_collection.insert_one(data)

        self.manager.current = "home"


class EditCardScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "edit_card"

        # Main layout
        layout = MDBoxLayout(orientation="vertical", spacing=dp(10), padding=dp(10))

        # Top app bar
        toolbar = MDTopAppBar(title="Edit Card", elevation=0, pos_hint={"top": 1})
        toolbar.left_action_items = [["arrow-left", lambda x: self.go_back()]]
        layout.add_widget(toolbar)

        # Content layout with padding
        content = MDBoxLayout(
            orientation="vertical",
            spacing=dp(20),
            padding=[dp(15), dp(20), dp(15), dp(20)],
            size_hint_y=None,
            height=dp(500),
        )

        # Card form
        card_form = MDCard(
            orientation="vertical",
            size_hint=(1, None),
            height=dp(450),
            padding=dp(15),
            elevation=2,
            radius=[dp(10)],
        )

        # Form fields
        self.title_field = MDTextField(
            hint_text="Card Title",
            helper_text="Enter the title for your card",
            helper_text_mode="on_focus",
            size_hint_x=1,
            mode="rectangle",
        )

        self.phone_number_field = MDTextField(
            hint_text="Phone Number",
            helper_text="Enter Phone Number",
            helper_text_mode="on_focus",
            multiline=True,
            size_hint_x=1,
            mode="rectangle",
        )

        buttons_layout = MDBoxLayout(
            orientation="horizontal",
            spacing=dp(10),
            size_hint=(1, None),
            height=dp(50),
            padding=[0, dp(20), 0, 0],
        )

        cancel_button = MDFlatButton(
            text="CANCEL", size_hint=(0.5, None), height=dp(50), on_release=self.go_back
        )

        save_button = MDRaisedButton(
            text="SAVE",
            size_hint=(0.5, None),
            height=dp(50),
            md_bg_color=MDApp.get_running_app().theme_cls.primary_color,
            on_release=self.save_card,
        )

        delete_button = MDRaisedButton(
            text="DELETE",
            size_hint=(0.5, None),
            height=dp(50),
            md_bg_color=(1, 0, 0, 1),  # Red color for delete button
            on_release=self.delete_card,
        )

        buttons_layout.add_widget(cancel_button)
        buttons_layout.add_widget(save_button)
        buttons_layout.add_widget(delete_button)

        card_form.add_widget(self.title_field)
        card_form.add_widget(self.phone_number_field)
        card_form.add_widget(buttons_layout)

        content.add_widget(card_form)

        layout.add_widget(content)

        self.add_widget(layout)

        self.card_data = None

    def set_card_data(self, card_data):
        self.card_data = card_data
        self.title_field.text = card_data["agency"]
        self.phone_number_field.text = card_data["phone_number"]

    def go_back(self, *args):
        self.manager.current = "home"

    def save_card(self, instance):
        title = self.title_field.text
        phone_number = self.phone_number_field.text
        numbers_info_collection.update_one(
            {"_id": self.card_data["_id"]},
            {"$set": {"agency": title, "phone_number": phone_number}},
        )

        self.manager.current = "home"
        self.manager.get_screen("home").load_cards()

    def delete_card(self, instance):
        numbers_info_collection.delete_one({"_id": self.card_data["_id"]})
        self.manager.current = "home"
        self.manager.get_screen("home").load_cards()


class CardApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.theme_style = "Light"

        sm = MDScreenManager()
        sm.add_widget(HomeScreen())
        sm.add_widget(CreateCardScreen())
        sm.add_widget(EditCardScreen())

        return sm


if __name__ == "__main__":
    CardApp().run()
