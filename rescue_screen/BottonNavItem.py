from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.behaviors import ButtonBehavior

# Set the window size to simulate a mobile device
Window.size = (360, 640)

# KV string for custom widgets and styling
KV = """
<BottomNavItem>:
    orientation: "vertical"
    adaptive_height: True
    spacing: dp(2)
    padding: dp(5)
    
    MDIconButton:
        icon: root.icon
        pos_hint: {"center_x": .5}
        theme_icon_color: "Custom"
        icon_color: (1, 0.6, 0.1, 1) if root.selected else (0.5, 0.5, 0.5, 1)
        on_release: root.navigate()
        
    MDLabel:
        text: root.text
        halign: "center"
        theme_text_color: "Custom"
        text_color: (1, 0.6, 0.1, 1) if root.selected else (0.5, 0.5, 0.5, 1)
        font_style: "Caption"
        adaptive_height: True
"""

Builder.load_string(KV)


# คลาส BottomNavItem สำหรับปุ่มแต่ละปุ่ม
class BottomNavItem(MDBoxLayout):
    icon = StringProperty("")
    text = StringProperty("")
    selected = BooleanProperty(False)
    screen_name = StringProperty("")

    def navigate(self):
        app = MDApp.get_running_app()
        app.root.current = self.screen_name


# 🟢 คลาสใหม่: BottomNavBar ทำให้สามารถใช้ได้ทุกหน้า
class BottomNavBar(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"
        self.adaptive_height = True
        self.md_bg_color = (1, 1, 1, 1)
        self.padding = [0, dp(5), 0, dp(5)]
        self.create_ui()

    def create_ui(self):
        # Clear existing widgets (if any)
        self.clear_widgets()

        # Add navigation items
        self.add_widget(
            BottomNavItem(
                icon="compass-outline",
                text="Explore",
                selected=True,
                screen_name="main",
            )
        )
        self.add_widget(
            BottomNavItem(
                icon="file-document-outline",
                text="Reports",
                screen_name="receiver",
            )
        )
        self.add_widget(
            BottomNavItem(
                icon="account-box-multiple",
                text="Officer info",
                screen_name="officer",
            )
        )
        self.add_widget(
            BottomNavItem(
                icon="account-outline",
                text="Login",
                screen_name="login",
            )
        )
