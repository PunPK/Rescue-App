from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior

KV = """
<SymbolScreen>:
    BoxLayout:
        orientation: 'vertical'
        
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
                text: 'สัญลักษณ์ความปลอดภัย'
                font_name: 'ThaiFont'
                font_size: '20sp'
                color: 1, 1, 1, 1
                halign: 'left'
                text_size: self.size
                valign: 'center'
                padding_x: 10
        
        ScrollView:
            do_scroll_x: False
            
            
            BoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                padding: dp(15)
                spacing: dp(20)

                Button:
                    text: 'ป้ายความปลอดภัยทั้งหมด'
                    font_name: 'ThaiFont'  
                    font_size: '28sp'    
                    color: 1, 1, 1, 1      
                    size_hint_y: None     
                    height: dp(50)        
                    background_color: 0.1, 0.4, 0.9, 1 
                    on_press: root.Link("https://santofire.co.th/safety-symbol/") 
                
                MDLabel:
                    text: "ป้ายเตือนภัยสีแดง"
                    font_name: 'ThaiFont'
                    font_size: sp(30)
                    bold: True
                    size_hint_y: None
                    height: self.texture_size[1]
                    halign: "center"
                    valign: "middle" 
                
                MDLabel:
                    text: "ความหมาย : หยุด หรือ ห้าม"
                    font_name: 'ThaiFont'
                    font_size: sp(20)
                    size_hint_y: None
                    height: self.texture_size[1]
                    padding_y: dp(5)
                    halign: "center"
                    valign: "middle" 
                
                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_y: None
                    height: dp(150)
                    spacing: dp(10)
                    
                    # Sign 1
                    WarningCard:
                        orientation: 'vertical'
                        elevation: 1
                        md_bg_color: 1, 0, 0, 1
                        radius: [15,]
                        
                        Image:
                            source: "Image/signs/r1.png" 
                            size_hint_y: 0.7
                        
                        MDLabel:
                            text: "ห้ามสูบบุหรี่\\nNO SMOKING"
                            font_name: 'ThaiFont'
                            halign: "center"
                            font_size: sp(10)
                            size_hint_y: 0.3
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                    
                    # Sign 2
                    WarningCard:
                        orientation: 'vertical'
                        elevation: 1
                        md_bg_color: 1, 0, 0, 1
                        radius: [15,]
                        
                        Image:
                            source: "Image/signs/r2.png" 
                            size_hint_y: 0.7
                        
                        MDLabel:
                            text: "ห้ามจุดไฟ\\nNO FIRE IGNITION"
                            font_name: 'ThaiFont'
                            halign: "center"
                            font_size: sp(10)
                            size_hint_y: 0.3
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                    
                    # Sign 3
                    WarningCard:
                        orientation: 'vertical'
                        elevation: 1
                        md_bg_color: 1, 0, 0, 1
                        radius: [15,]
                        
                        Image:
                            source: "Image/signs/r3.png" 
                            size_hint_y: 0.7
                        
                        MDLabel:
                            text: "ห้ามเข้าใกล้เครื่องจักร\\nKEEP AWAY FROM MACHINERY"
                            font_name: 'ThaiFont'
                            halign: "center"
                            font_size: sp(10)
                            size_hint_y: 0.3
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                
                MDLabel:
                    text: "ป้ายเตือนภัยสีเหลือง"
                    font_name: 'ThaiFont'
                    font_size: sp(30)
                    bold: True
                    size_hint_y: None
                    height: self.texture_size[1]
                    padding_y: dp(10)
                    halign: "center"
                    valign: "middle" 
                
                MDLabel:
                    text: "ความหมาย : ระวังมีอันตราย"
                    font_name: 'ThaiFont'
                    font_size: sp(20)
                    size_hint_y: None
                    height: self.texture_size[1]
                    padding_y: dp(5)
                    halign: "center"
                    valign: "middle" 

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_y: None
                    height: dp(150)
                    spacing: dp(10)
                    
                    # Sign 1
                    WarningCard:
                        orientation: 'vertical'
                        elevation: 1
                        md_bg_color: 1, 0.8, 0, 1
                        radius: [15,]
                        
                        Image:
                            source: "Image/signs/y1.png" 
                            size_hint_y: 0.7
                        
                        MDLabel:
                            text: "ระวังอันตราย\\nBEWARE DANGER"
                            font_name: 'ThaiFont'
                            halign: "center"
                            font_size: sp(10)
                            size_hint_y: 0.3
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                    
                    # Sign 2
                    WarningCard:
                        orientation: 'vertical'
                        elevation: 1
                        md_bg_color: 1, 0.8, 0, 1
                        radius: [15,]
                        
                        Image:
                            source: "Image/signs/y2.png" 
                            size_hint_y: 0.7
                        
                        MDLabel:
                            text: "ระวังไฟฟ้าแรงสูง\\nBEWARE HIGH VOLTAG"
                            font_name: 'ThaiFont'
                            halign: "center"
                            font_size: sp(10)
                            size_hint_y: 0.3
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                    
                    # Sign 3
                    WarningCard:
                        orientation: 'vertical'
                        elevation: 1
                        md_bg_color: 1, 0.8, 0, 1
                        radius: [15,]
                        
                        Image:
                            source: "Image/signs/y3.png" 
                            size_hint_y: 0.7
                        
                        MDLabel:
                            text: "ระวังวัตถุไวไฟ\\nBEWARE FLAMMABLE LIQUID"
                            font_name: 'ThaiFont'
                            halign: "center"
                            font_size: sp(10)
                            size_hint_y: 0.3
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1

                MDLabel:
                    text: "ป้ายเตือนภัยสีน้ำเงิน"
                    font_name: 'ThaiFont'
                    font_size: sp(30)
                    bold: True
                    size_hint_y: None
                    height: self.texture_size[1]
                    padding_y: dp(10)
                    halign: "center"
                    valign: "middle" 

                MDLabel:
                    text: "ความหมาย : ต้องทำ/บังคับ/ให้ปฏิบัติ"
                    font_name: 'ThaiFont'
                    font_size: sp(20)
                    size_hint_y: None
                    height: self.texture_size[1]
                    padding_y: dp(5)
                    halign: "center"
                    valign: "middle" 

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_y: None
                    height: dp(150)
                    spacing: dp(10)
                    
                    # Sign 1
                    WarningCard:
                        orientation: 'vertical'
                        elevation: 1
                        md_bg_color: 0, 0, 1, 1 
                        radius: [15,]
                        
                        Image:
                            source: "Image/signs/b1.png" 
                            size_hint_y: 0.7
                        
                        MDLabel:
                            text: "สวมหมวกนิรภัย\\nWEAR HEAD PROTECTION"
                            font_name: 'ThaiFont'
                            halign: "center"
                            font_size: sp(10)
                            size_hint_y: 0.3
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1 
                    
                    # Sign 2
                    WarningCard:
                        orientation: 'vertical'
                        elevation: 1
                        md_bg_color: 0, 0, 1, 1 
                        radius: [15,]
                        
                        Image:
                            source: "Image/signs/b2.png" 
                            size_hint_y: 0.7
                        
                        MDLabel:
                            text: "สวมหน้ากากกันสารเคมี\\nWEAR RESPOIRATOR"
                            font_name: 'ThaiFont'
                            halign: "center"
                            font_size: sp(10)
                            size_hint_y: 0.3
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1 
                    
                    # Sign 3
                    WarningCard:
                        orientation: 'vertical'
                        elevation: 1
                        md_bg_color: 0, 0, 1, 1  
                        radius: [15,]
                        
                        Image:
                            source: "Image/signs/b3.png" 
                            size_hint_y: 0.7
                        
                        MDLabel:
                            text: "สวมแว่นตานิรภัย\\nWEAR GOGGLE"
                            font_name: 'ThaiFont'
                            halign: "center"
                            font_size: sp(10)
                            size_hint_y: 0.3
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1 

                MDLabel:
                    text: "ป้ายเตือนภัยสีเขียว"
                    font_name: 'ThaiFont'
                    font_size: sp(30)
                    bold: True
                    size_hint_y: None
                    height: self.texture_size[1]
                    padding_y: dp(10)
                    halign: "center"
                    valign: "middle" 

                MDLabel:
                    text: "ความหมาย : บอกถึงการไปสู่ความปลอดภัย"
                    font_name: 'ThaiFont'
                    font_size: sp(20)
                    size_hint_y: None
                    height: self.texture_size[1]
                    padding_y: dp(5)
                    halign: "center"
                    valign: "middle" 

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_y: None
                    height: dp(150)
                    spacing: dp(10)
                    
                    # Sign 1
                    WarningCard:
                        orientation: 'vertical'
                        elevation: 1
                        md_bg_color: 0, 1, 0, 1 
                        radius: [15,]
                        
                        Image:
                            source: "Image/signs/g1.png" 
                            size_hint_y: 0.7
                        
                        MDLabel:
                            text: "ทางหนีไฟ\\nFIRT EXIT"
                            font_name: 'ThaiFont'
                            halign: "center"
                            font_size: sp(10)
                            size_hint_y: 0.3
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  
                    
                    # Sign 2
                    WarningCard:
                        orientation: 'vertical'
                        elevation: 1
                        md_bg_color: 0, 1, 0, 1 
                        radius: [15,]
                        
                        Image:
                            source: "Image/signs/g2.png" 
                            size_hint_y: 0.7
                        
                        MDLabel:
                            text: "จุดปฐมพยาบาล\\nFIRST AID"
                            font_name: 'ThaiFont'
                            halign: "center"
                            font_size: sp(10)
                            size_hint_y: 0.3
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  
                    
                    # Sign 3
                    WarningCard:
                        orientation: 'vertical'
                        elevation: 1
                        md_bg_color: 0, 1, 0, 1  
                        radius: [15,]
                        
                        Image:
                            source: "Image/signs/g3.png" 
                            size_hint_y: 0.7
                        
                        MDLabel:
                            text: "ชำระล้างฉุกเฉิน\\nEMERGENCY SHOWER"
                            font_name: 'ThaiFont'
                            halign: "center"
                            font_size: sp(10)
                            size_hint_y: 0.3
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1 

                

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


class WarningCard(MDCard, RoundedRectangularElevationBehavior):
    pass


class SymbolScreen(MDScreen):
    def Link(self, link):
        if link:
            import webbrowser

            webbrowser.open(link)


class SymbolApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


if __name__ == "__main__":
    SymbolApp().run()
