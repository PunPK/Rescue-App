from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel


class Home_Admin(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "home-admin"
        self.add_widget(
            MDLabel(text="Welcome to the Home Admin Screen", halign="center")
        )
