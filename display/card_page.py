from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import MDList, OneLineListItem
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.metrics import dp

# Set window size to mobile dimensions (360x640)
Window.size = (360, 640)


class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "home"

        # Main layout
        layout = MDBoxLayout(orientation="vertical")

        # Top app bar
        toolbar = MDTopAppBar(title="My Cards", elevation=10, pos_hint={"top": 1})
        layout.add_widget(toolbar)

        # Scrollable list container
        scroll_view = ScrollView()

        # Content - List of cards (top to bottom)

        card_list = MDList()
        card_list.bind(minimum_height=card_list.setter("height"))  # Expand properly

        # Sample cards (Added in top-to-bottom order)
        for i in range(5):
            item = OneLineListItem(
                text=f"Card {i+1}",
                on_release=lambda x, i=i: print(f"Card {i+1} selected"),
            )
            card_list.add_widget(item)

        scroll_view.add_widget(card_list)
        layout.add_widget(scroll_view)

        self.add_widget(layout)

    def go_to_create_card(self, instance):
        self.manager.current = "create_card"


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
