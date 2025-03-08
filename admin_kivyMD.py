from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivy.uix.screenmanager import ScreenManager

# Import our screen classes
from rescue_screen.home_admin import Home_Admin

# Define the KV string for the navigation structure
KV = """
BoxLayout:
    orientation: 'vertical'
    
    ScreenManager:
        id: screen_manager
    
    MDBottomNavigation:
        panel_color: app.theme_cls.primary_color
        text_color_active: 1, 1, 1, 1
        
        MDBottomNavigationItem:
            name: 'nav_main'
            text: 'Main'
            icon: 'home'
            on_tab_press: app.switch_screen('home-admin')
        
        MDBottomNavigationItem:
            name: 'nav_main'
            text: 'Main'
            icon: 'home'
            on_tab_press: app.switch_screen('home-admin')
        
        MDBottomNavigationItem:
            name: 'nav_main'
            text: 'Main'
            icon: 'home'
            on_tab_press: app.switch_screen('home-admin')
            
        MDBottomNavigationItem:
            name: 'nav_reviews'
            text: 'Reviews'
            icon: 'star'
            on_tab_press: app.switch_screen('reviews')
"""


class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Amber"

        # Create the root widget from KV string
        self.root = Builder.load_string(KV)

        # Get reference to the screen manager
        self.screen_manager = self.root.ids.screen_manager

        # Create and add screens to the manager

        self.screen_manager.add_widget(Home_Admin(name="home-admin"))

        # Set initial screen AFTER adding screens
        self.screen_manager.current = "home-admin"

        return self.root

    def switch_screen(self, screen_name):
        self.screen_manager.current = screen_name


if __name__ == "__main__":
    MyApp().run()
