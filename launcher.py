from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# Import your apps
from main_kivyMD import RescueApp
from admin_kivyMD import RescueAdminApp

# Import your login screen
from rescue_screen.LoginScreen import LoginScreen
from rescue_screen.ReportScreen import ReceiverScreen
from rescue_screen.LoginScreen import LoginScreen
from rescue_screen.ReportList import ReportList
from rescue_screen.RegistrationPage import RegistrationScreen
from rescue_screen.HomePage import MainScreen
from rescue_screen.ruam_ber import Ruem_ber
from rescue_screen.MyDevelopPage import MyDevelop
from rescue_screen.ApplicationInfo import ApplicationInfoScreen
from rescue_screen.MapScreen import MapScreen


# shared.py
from kivymd.app import MDApp


class RescueApp(MDApp):
    def build(self):
        pass

    def switch_to_admin_app(self):
        self.stop()
        rescue_admin_app = RescueAdminApp()
        rescue_admin_app.run()


class RescueAdminApp(MDApp):
    def build(self):
        pass

    def switch_to_user_app(self):
        self.stop()
        rescue_app = RescueApp()
        rescue_app.run()
