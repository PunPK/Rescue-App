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
from kivy.core.text import LabelBase
from kivy.uix.label import Label
import gridfs
from kivy.lang import Builder
from rescue_screen import ReceiverScreen
from kivy.lang import Builder
from kivymd.icon_definitions import md_icons
from rescue_screen.db_connection import reports_collection, users_collection

from rescue_screen.ReportScreen import ReceiverScreen
from rescue_screen.LoginScreen import LoginScreen
from rescue_screen.ReceiveReport import ReceiveReportScreen
from rescue_screen.RegistrationPage import RegistrationScreen
from rescue_screen.HomePage import MainScreen
from rescue_screen.ruam_ber import Ruem_ber

# from rescue_screen.BottonNavItem import BottomNavBar

Window.size = (360, 640)


class RescueApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "900"

        # Create a screen manager
        self.screen_manager = MDScreenManager()

        # Add screens
        main_screen = MainScreen(name="main")
        self.screen_manager.add_widget(main_screen)
        self.screen_manager.add_widget(ReceiverScreen(name="receiver"))
        self.screen_manager.add_widget(LoginScreen(name="login"))
        self.screen_manager.add_widget(RegistrationScreen(name="register"))
        self.screen_manager.add_widget(Ruem_ber(name="officer"))

        # Set the current screen to main
        self.screen_manager.current = "main"

        return self.screen_manager


if __name__ == "__main__":
    RescueApp().run()
