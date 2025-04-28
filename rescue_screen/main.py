from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from rescue_screen.ReportList import ReceiveReportScreen


class RescueApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ReceiveReportScreen(name="receive_report_screen"))
        return sm


if __name__ == "__main__":
    RescueApp().run()
