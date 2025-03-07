from kivy.lang import Builder
from kivy.core.window import Window
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen

# Set window size to simulate a smartphone
Window.size = (360, 640)

KV = """
MDScreen:
    md_bg_color: 1, 1, 1, 1
    
    MDBoxLayout:
        orientation: 'vertical'
        padding: 0
        spacing: 0
        
        # Top blue wave section
        MDRelativeLayout:
            size_hint_y: 0.3
            
            # Blue background
            MDFloatLayout:
                md_bg_color: 0.1, 0.4, 0.9, 1
                size_hint: 1, 1
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
            
            # Wave shape (white)
            Image:
                source: "wave.png"
                size_hint: 1, 1
                pos_hint: {"center_x": 0.5, "center_y": 0}
                allow_stretch: True
                keep_ratio: False
            
            # Status bar elements
            MDLabel:
                text: "12:00"
                pos_hint: {"center_y": 0.85, "center_x": 0.1}
                font_style: "Caption"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                
            # Sign up / Sign in tabs
            MDBoxLayout:
                adaptive_height: True
                spacing: dp(20)
                pos_hint: {"center_x": 0.6, "center_y": 0.3}
                
                MDLabel:
                    text: "Sign up"
                    theme_text_color: "Custom"
                    text_color: 0.1, 0.4, 0.9, 1
                    font_style: "H6"
                    bold: True
                    
                MDLabel:
                    text: "Sign in"
                    theme_text_color: "Custom"
                    text_color: 0.5, 0.7, 1, 1
                    font_style: "H6"
        
        # Form section
        MDBoxLayout:
            orientation: 'vertical'
            padding: dp(20)
            spacing: dp(15)
            size_hint_y: 0.7
            md_bg_color: 0.95, 0.98, 1, 1
            
            MDTextField:
                hint_text: "Username"
                mode: "line"
                line_color_normal: 0.1, 0.4, 0.9, 1
                
            MDTextField:
                hint_text: "Full name"
                mode: "line"
                line_color_normal: 0.1, 0.4, 0.9, 1
                
            MDTextField:
                hint_text: "E-mail"
                mode: "line"
                line_color_normal: 0.1, 0.4, 0.9, 1
                
            MDTextField:
                hint_text: "Password"
                mode: "line"
                password: True
                line_color_normal: 0.1, 0.4, 0.9, 1
            
            MDBoxLayout:
                adaptive_height: True
                spacing: dp(10)
                
                MDCheckbox:
                    size_hint: None, None
                    size: dp(48), dp(48)
                    active: True
                    selected_color: 0.1, 0.4, 0.9, 1
                    
                MDLabel:
                    text: "Agree with [color=0066CC]Terms & Conditions[/color]"
                    markup: True
                    theme_text_color: "Secondary"
            
            Widget:
                size_hint_y: 0.1
                
            MDFillRoundFlatButton:
                text: "Sign up"
                md_bg_color: 0.1, 0.4, 0.9, 1
                text_color: 1, 1, 1, 1
                size_hint_x: 0.5
                pos_hint: {"center_x": 0.5}
                on_release: app.show_registration_success()
                
            MDTextButton:
                text: "I'm already a member"
                theme_text_color: "Custom"
                text_color: 0.3, 0.3, 0.3, 1
                pos_hint: {"center_x": 0.5}
                on_release: app.switch_to_signin()
"""

# Builder.load_string(KV)


class RegistrationScreen(MDScreen):
    dialog = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build()

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "700"
        return Builder.load_string(KV)

    def show_registration_success(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Registration Successful!",
                text="Your account has been created successfully.",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x: self.dialog.dismiss(),
                    )
                ],
            )
        self.dialog.open()

    def switch_to_signin(self):
        self.manager.current = "login"
