from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# Import your apps
from main_kivyMD import RescueApp
from admin_kivyMD import MyApp

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


class LauncherApp(MDApp):
    def build(self):
        # Create a screen manager
        self.screen_manager = ScreenManager()

        main_screen = MainScreen(name="main")
        self.screen_manager.add_widget(main_screen)
        self.screen_manager.add_widget(ReceiverScreen(name="receiver"))
        self.screen_manager.add_widget(LoginScreen(name="login"))
        self.screen_manager.add_widget(RegistrationScreen(name="register"))
        self.screen_manager.add_widget(LoginScreen(name="login"))

        self.screen_manager.current = "main"
        return self.screen_manager

    def switch_to_admin_app(self):
        self.stop()
        MyApp().run()

    def switch_to_user_app(self):
        self.stop()
        RescueApp().run()


if __name__ == "__main__":
    LauncherApp().run()
