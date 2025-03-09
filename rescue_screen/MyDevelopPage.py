from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager

Window.size = (360, 640)

KV = """
<MyDevelop>:
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1  # White background
            Rectangle:
                pos: self.pos
                size: self.size
        
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
                text: 'ทีมผู้พัฒนา'
                font_name: 'ThaiFont'
                font_size: '20sp'
                color: 1, 1, 1, 1  # White text
                halign: 'left'
                text_size: self.size
                valign: 'center'
                padding_x: 10
        
        # Develop By section
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: dp(140)
            padding: dp(20)
            spacing: dp(10)
            canvas.before:
                Color:
                    rgba: utils.get_color_from_hex('#f5f5f5')  # Light gray background
                Rectangle:
                    pos: self.pos
                    size: self.size
            
            MDLabel:
                text: "Develop By"
                theme_text_color: "Custom"
                text_color: utils.get_color_from_hex('#023282')  # Dark blue text
                font_size: dp(24)
                bold: True
                halign: "center"
            
            # CoE PSU Logo
            AsyncImage:
                source: 'Image/coepsu.png'
                size_hint: None, None
                size: dp(100), dp(60)
                pos_hint: {'center_x': 0.5}
                allow_stretch: True
                keep_ratio: True
        
        # Scrollable content
        ScrollView:
            do_scroll_x: False
            
            BoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                padding: dp(10)
                spacing: dp(10)
                
                # Entry 1
                MDCard:
                    size_hint_y: None
                    height: dp(100)
                    padding: dp(10)
                    spacing: dp(10)
                    elevation: 1
                    radius: [15, 15, 15, 15]
                    md_bg_color: utils.get_color_from_hex('#ffffff')  # White background
                    
                    # Landscape icon
                    AsyncImage:
                        size_hint_x: 0.3
                        source: 'Image/6710110005.png'
                        size: dp(80), dp(80)
                        allow_stretch: True
                        keep_ratio: True
                        radius: [40, 40, 40, 40]
                    
                    # Text information
                    BoxLayout:
                        orientation: 'vertical'
                        size_hint_x: 0.7
                        
                        MDLabel:
                            text: "นายกรธัช สุขสวัสดิ์"
                            font_name: 'ThaiFont'
                            theme_text_color: "Custom"
                            text_color: utils.get_color_from_hex('#023282')  # Dark blue text
                            font_size: dp(16)
                            bold: True
                        
                        MDLabel:
                            text: "6710110005"
                            theme_text_color: "Custom"
                            text_color: utils.get_color_from_hex('#023282')  # Dark blue text
                            font_size: dp(16)
                
                # Entry 2
                MDCard:
                    size_hint_y: None
                    height: dp(100)
                    padding: dp(10)
                    spacing: dp(10)
                    elevation: 1
                    radius: [15, 15, 15, 15]
                    md_bg_color: utils.get_color_from_hex('#ffffff')  # White background
                    
                    # Landscape icon
                    AsyncImage:
                        size_hint_x: 0.3
                        source: 'Image/6710110270.png'
                        size: dp(80), dp(80)
                        allow_stretch: True
                        keep_ratio: True
                        radius: [40, 40, 40, 40]
                    
                    # Text information
                    BoxLayout:
                        orientation: 'vertical'
                        size_hint_x: 0.7
                        
                        MDLabel:
                            text: "นายปุรัสกร เกียรติ์นนทพัทธ์"
                            font_name: 'ThaiFont'
                            theme_text_color: "Custom"
                            text_color: utils.get_color_from_hex('#023282')  # Dark blue text
                            font_size: dp(16)
                            bold: True
                        
                        MDLabel:
                            text: "6710110270"
                            theme_text_color: "Custom"
                            text_color: utils.get_color_from_hex('#023282')  # Dark blue text
                            font_size: dp(16)
                
                # Entry 3
                MDCard:
                    size_hint_y: None
                    height: dp(100)
                    padding: dp(10)
                    spacing: dp(10)
                    elevation: 1
                    radius: [15, 15, 15, 15]
                    md_bg_color: utils.get_color_from_hex('#ffffff')  # White background
                    
                    # Landscape icon
                    AsyncImage:
                        size_hint_x: 0.3
                        source: 'Image/6710110280.png'
                        size: dp(80), dp(80)
                        allow_stretch: True
                        keep_ratio: True
                        radius: [40, 40, 40, 40]
                    
                    # Text information
                    BoxLayout:
                        orientation: 'vertical'
                        size_hint_x: 0.7
                        
                        MDLabel:
                            text: "นายพัฒนชัย พันธุ์เกตุ"
                            font_name: 'ThaiFont'
                            theme_text_color: "Custom"
                            text_color: utils.get_color_from_hex('#023282')  # Dark blue text
                            font_size: dp(16)
                            bold: True
                        
                        MDLabel:
                            text: "6710110280"
                            theme_text_color: "Custom"
                            text_color: utils.get_color_from_hex('#023282')  # Dark blue text
                            font_size: dp(16)

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


class MyDevelop(MDScreen):
    pass


class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "700"

        # Create a screen manager
        self.screen_manager = MDScreenManager()

        # Add MyDevelopScreen to the screen manager
        self.screen_manager.add_widget(MyDevelop(name="mydevelop"))

        return self.screen_manager


if __name__ == "__main__":
    MyApp().run()
