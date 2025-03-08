from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.label import MDLabel
from kivymd.icon_definitions import md_icons
from kivy.core.window import Window

# Set window size to mobile dimensions (360x640)
Window.size = (360, 640)


class BottomNavScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create the bottom navigation bar
        bottom_navigation = MDBottomNavigation(
            panel_color=self.theme_cls.primary_color,
            selected_color_background=self.theme_cls.accent_color,
            text_color_active=self.theme_cls.primary_dark,
        )

        # Home tab
        home_tab = MDBottomNavigationItem(name="home", text="Home", icon="home")
        home_tab.add_widget(MDLabel(text="Welcome to the Home Screen", halign="center"))

        # Search tab
        search_tab = MDBottomNavigationItem(
            name="search", text="Search", icon="magnify"
        )
        search_tab.add_widget(MDLabel(text="Search Screen", halign="center"))

        # Profile tab
        profile_tab = MDBottomNavigationItem(
            name="profile", text="Profile", icon="account"
        )
        profile_tab.add_widget(MDLabel(text="User Profile Screen", halign="center"))

        # Settings tab
        settings_tab = MDBottomNavigationItem(
            name="settings", text="Settings", icon="cog"
        )
        settings_tab.add_widget(MDLabel(text="Settings Screen", halign="center"))

        # Add all tabs to the bottom navigation
        bottom_navigation.add_widget(home_tab)
        bottom_navigation.add_widget(search_tab)
        bottom_navigation.add_widget(profile_tab)
        bottom_navigation.add_widget(settings_tab)

        # Add the bottom navigation to the screen
        self.add_widget(bottom_navigation)


class BottomNavApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.theme_style = "Light"
        return BottomNavScreen()


if __name__ == "__main__":
    BottomNavApp().run()
