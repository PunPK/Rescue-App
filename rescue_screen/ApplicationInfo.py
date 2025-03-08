from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivymd.uix.screen import MDScreen

# Register the Thai font (ThaiFont)
# Note: You would need to have this font file in your assets folder
# LabelBase.register(name="THSarabunNew", fn_regular="THSarabunNew.ttf")

# Set window size to simulate a mobile device
Window.size = (360, 640)

KV = """
<ApplicationInfoScreen>:
    MDBoxLayout:
        orientation: "vertical"
        spacing: "10dp"

        # Header
        BoxLayout:
            size_hint_y: None
            height: '60dp'
            padding: [10, 0]
            canvas.before:
                Color:
                    rgba: utils.get_color_from_hex('#023282')  # Dark blue header
                Rectangle:
                    pos: self.pos
                    size: self.size

            Image:
                source: 'Image/logo.png'
                size_hint: (None, None)
                size: (50, 50)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            Label:
                text: 'ข้อมูลที่เกี่ยวข้องกับแอปพิเคชั่น'
                font_name: 'ThaiFont'
                font_size: '20sp'
                color: 1, 1, 1, 1
                halign: 'left'
                text_size: self.size
                valign: 'center'
                padding_x: 10
        
        # Main content
        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                padding: "16dp"
                spacing: "20dp"
                size_hint_y: None
                height: self.minimum_height
                
                # Title
                MDLabel:
                    text: "Tools For Develop"
                    font_size: "24sp"
                    bold: True
                    size_hint_y: None
                    height: self.texture_size[1]
                    halign: "center"
                
                # KivyMD section
                MDBoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: "80dp"
                    spacing: "4dp"
                    padding: [0, "16dp", 0, "16dp"]
                    
                    FitImage:
                        source: "Image/kivymd.png"
                        size_hint: None, None
                        size: "80dp", "80dp"
                        pos_hint: {"center_x": .5, "center_y": .5}
                        radius: [40, 40, 40, 40]
                    
                    MDLabel:
                        text: "kivymd\\n1.2.0"
                        font_size: "16sp"
                        size_hint_x: 0.6
                        halign: "center"
                
                # Python section
                MDBoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: "80dp"
                    spacing: "4dp"
                    padding: [0, "16dp", 0, "16dp"]
                    
                    FitImage:
                        source: "Image/python.png"
                        size_hint: None, None
                        size: "80dp", "80dp"
                        pos_hint: {"center_x": .5, "center_y": .5}
                        radius: [40, 40, 40, 40]
                    
                    MDLabel:
                        text: "Python\\n3.12.3"
                        font_size: "16sp"
                        size_hint_x: 0.6
                        halign: "center"
                
                # Database section
                MDBoxLayout:
                    orientation: "vertical"
                    size_hint_y: None
                    height: "120dp"
                    spacing: "6dp"
                    
                    MDLabel:
                        text: "DataBase"
                        font_size: "18sp"
                        bold: True
                        size_hint_y: None
                        height: self.texture_size[1]
                        halign: "center"
                    
                    MDCard:
                        size_hint_y: None
                        height: "80dp"
                        md_bg_color: 0, 0.6, 0.2, 1  # Green color for MongoDB
                        radius: [4, 4, 4, 4]
                        
                        FitImage:
                            source: "Image/mongodb.png"
                            size_hint: None, None
                            size: "330dp", "80dp"
                            # pos_hint: {"center_x": .5, "center_y": .5}
                            # halign: "center"
                
                # Other Tools section
                MDBoxLayout:
                    orientation: "vertical"
                    size_hint_y: None
                    height: "100dp"
                    spacing: "3dp"
                    
                    MDLabel:
                        text: "Other Tools"
                        font_size: "18sp"
                        bold: True
                        size_hint_y: None
                        height: self.texture_size[1]
                        halign: "center"
                    
                    MDLabel:
                        text: "Font : ThaiFont"
                        font_size: "16sp"
                        size_hint_y: None
                        height: self.texture_size[1]
                        halign: "center"
                    
                    MDLabel:
                        text: "CAM : OpenCV2"
                        font_size: "16sp"
                        size_hint_y: None
                        height: self.texture_size[1]
                        halign: "center"

        # Bottom navigation
        MDBoxLayout:
            adaptive_height: True
            md_bg_color: (1, 1, 1, 1)
            padding: [0, dp(5), 0, dp(5)]
            spacing: dp(10)

            BottomNavItem:
                icon: "compass-outline"
                text: "Explore"
                screen_name: "main"

            BottomNavItem:
                icon: "file-document-outline"
                text: "Reports"
                screen_name: "receiver"

            BottomNavItem:
                icon: "account-box-multiple"
                text: "Officer"
                screen_name: "officer"

            BottomNavItem:
                icon: "account-outline"
                text: "Login"
                screen_name: "login"
"""

Builder.load_string(KV)


class ApplicationInfoScreen(MDScreen):
    pass


class ToolsForDevelopApp(MDApp):
    def build(self):
        Builder.load_string(KV)
        self.theme_cls.primary_palette = "Blue"
        return ApplicationInfoScreen()


if __name__ == "__main__":
    ToolsForDevelopApp().run()
