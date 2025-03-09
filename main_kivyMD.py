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

# from rescue_screen import ReceiverScreen
from kivy.lang import Builder
from kivymd.icon_definitions import md_icons
from rescue_screen.db_connection import reports_collection, users_collection

from rescue_screen.ReportScreen import ReceiverScreen
from rescue_screen.LoginScreen import LoginScreen
from rescue_screen.ReportList import ReportList
from rescue_screen.RegistrationPage import RegistrationScreen
from rescue_screen.HomePage import MainScreen
from rescue_screen.ruam_ber import Ruem_ber
from rescue_screen.MyDevelopPage import MyDevelop
from rescue_screen.ApplicationInfo import ApplicationInfoScreen
from rescue_screen.MapScreen import MapViewScreen
from rescue_screen.salfty_tips import Tips_page
from rescue_screen.SymbolPage import SymbolScreen

# from launcher import RescueAdminApp

# from rescue_screen.BottonNavItem import BottomNavBar

Window.size = (360, 640)


class RescueApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "900"

        self.screen_manager = MDScreenManager()

        main_screen = MainScreen(name="main")
        self.screen_manager.add_widget(main_screen)
        self.screen_manager.add_widget(ReceiverScreen(name="receiver"))
        self.screen_manager.add_widget(LoginScreen(name="login"))
        self.screen_manager.add_widget(RegistrationScreen(name="register"))
        self.screen_manager.add_widget(Ruem_ber(name="officer"))
        self.screen_manager.add_widget(MyDevelop(name="mydevelop"))
        self.screen_manager.add_widget(ApplicationInfoScreen(name="applicationinfo"))
        self.screen_manager.add_widget(MapViewScreen(name="mapview"))
        self.screen_manager.add_widget(Tips_page(name="tipsview"))
        self.screen_manager.add_widget(SymbolScreen(name="symbolview"))
        self.screen_manager.current = "main"

        return self.screen_manager

    def switch_to_admin_app(self):
        self.stop()
        from admin_kivyMD import RescueAdminApp

        RescueAdminApp().run()


if __name__ == "__main__":
    RescueApp().run()
