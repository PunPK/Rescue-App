from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivy.uix.screenmanager import ScreenManager

# Import our screen classes
from rescue_screen.home_admin import Home_Admin
from rescue_screen.tool_page import Tool_page
from rescue_screen.card_page import Card_page, CreateCardScreen, EditCardScreen
from rescue_screen.safty_tips_management import (
    Tips_page,
    CreateTipScreen,
    EditTipScreen,
)

# Define the KV string for the navigation structure
KV = """
BoxLayout:
    orientation: 'vertical'
    size_hint: 1, 1
    
    ScreenManager:
        id: screen_manager
        size_hint: 1, 1 
    
    MDBottomNavigation:
        panel_color: app.theme_cls.primary_color
        text_color_active: 1, 1, 1, 1
        size_hint_y: 0.1

        MDBottomNavigationItem:
            name: 'nav_main'
            text: 'Main'
            icon: 'home'
            on_tab_press: app.switch_screen('home-admin')
        
        MDBottomNavigationItem:
            name: 'nav_main'
            text: 'Mangement'
            icon: 'tools'
            on_tab_press: app.switch_screen('tool-page')
        
        # MDBottomNavigationItem:
        #     name: 'nav_main'
        #     text: 'Main'
        #     icon: 'home'
        #     on_tab_press: app.switch_screen('home-admin')

        MDBottomNavigationItem:
            name: 'nav_logout'
            text: 'logout'
            icon: 'logout-variant'
            on_tab_press: app.switch_to_user_app()
"""


class RescueAdminApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Amber"

        # Create the root widget from KV string
        self.root = Builder.load_string(KV)

        # Get reference to the screen manager
        self.screen_manager = self.root.ids.screen_manager

        self.screen_manager.add_widget(Home_Admin(name="home-admin"))
        self.screen_manager.add_widget(Tool_page(name="tool-page"))
        self.screen_manager.add_widget(Card_page(name=("card-page")))
        self.screen_manager.add_widget(CreateCardScreen(name=("create_card")))
        self.screen_manager.add_widget(EditCardScreen(name=("edit_card")))
        self.screen_manager.add_widget(Tips_page(name=("tips-page")))
        self.screen_manager.add_widget(CreateTipScreen(name=("create_tip")))
        self.screen_manager.add_widget(EditTipScreen(name=("edit_tip")))
        # Set initial screen AFTER adding screens
        self.screen_manager.current = "home-admin"

        return self.root

    def switch_screen(self, screen_name):
        self.screen_manager.current = screen_name

    def switch_to_user_app(self):
        self.stop()
        from main_kivyMD import RescueApp

        RescueApp().run()


if __name__ == "__main__":
    RescueAdminApp().run()
