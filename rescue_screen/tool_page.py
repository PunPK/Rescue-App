from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp
from kivy.core.window import Window
from kivymd.uix.card import MDCard
from kivy.uix.image import Image
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from kivy.uix.scrollview import ScrollView

Window.size = (360, 640)


class ServiceCard(MDCard):
    def __init__(self, icon_source, title, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None
        self.height = dp(120)
        self.radius = [dp(15)]
        self.elevation = 1
        self.padding = [dp(10), dp(10), dp(10), dp(10)]
        self.md_bg_color = (1, 1, 1, 1)
        self.ripple_behavior = True
        self.orientation = "vertical"

        # Create a circular background for the icon
        icon_bg = MDCard(
            size_hint=(None, None),
            size=(dp(50), dp(50)),
            radius=[dp(25)],
            md_bg_color=(0.9, 0.95, 1, 1),  # Light blue background
            elevation=0,
            pos_hint={"center_x": 0.5},
        )

        # Icon
        icon = Image(
            source=icon_source,
            size_hint=(None, None),
            size=(dp(50), dp(50)),
            pos_hint={"center_x": 0.7, "center_y": 0.5},
        )

        icon_bg.add_widget(icon)

        # Title
        title_label = MDLabel(
            text=title,
            halign="center",
            theme_text_color="Secondary",
            font_style="Caption",
            adaptive_height=True,
        )

        # Add widgets to card
        self.add_widget(MDBoxLayout(size_hint_y=None, height=dp(5)))  # Spacing
        self.add_widget(icon_bg)
        self.add_widget(MDBoxLayout(size_hint_y=None, height=dp(5)))  # Spacing
        self.add_widget(title_label)

    def on_card_click(self, *args):
        if hasattr(self, "on_release") and self.on_release:
            self.on_release(self)


class Tool_page(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "tool-page"
        self.create_ui()

    def create_ui(self):
        # Main layout
        main_layout = MDBoxLayout(orientation="vertical", size_hint=(1, 1))

        # Toolbar at the top
        toolbar = MDTopAppBar(
            title="Admin Management",
            elevation=0,
            pos_hint={"top": 2},
        )
        main_layout.add_widget(toolbar)

        # ScrollView containing the service cards
        scroll_view = ScrollView(
            size_hint=(1, 1),
        )  # Set a height for the scroll view
        content_layout = MDBoxLayout(
            adaptive_height=True,
            orientation="vertical",
            spacing=dp(10),
        )

        services_grid1 = MDBoxLayout(
            adaptive_height=True,
            spacing=dp(10),
            padding=[0, dp(5), 0, dp(5)],
            size_hint_x=1,
        )

        services_grid2 = MDBoxLayout(
            adaptive_height=True,
            spacing=dp(10),
            padding=[0, dp(5), 0, dp(5)],
            size_hint_x=1,
        )
        services_grid3 = MDBoxLayout(
            adaptive_height=True,
            spacing=dp(10),
            padding=[0, dp(5), 0, dp(5)],
            size_hint_x=1,
        )
        # Service cards - first row
        services_grid1.add_widget(
            ServiceCard(
                icon_source="Image/phone_icon.png",  # Ensure the image path is correct
                title="Phone Management",
                on_release=lambda x: MDApp.get_running_app().switch_screen("card-page"),
            )
        )

        # Service cards - second row
        services_grid2.add_widget(
            ServiceCard(
                icon_source="image/SignIn.png",  # Ensure the image path is correct
                title="Sign In\nApplication",
                on_release=self.Nav,
            )
        )

        services_grid3.add_widget(
            ServiceCard(
                icon_source="image/SignIn.png",  # Ensure the image path is correct
                title="Sign In\nApplication",
                on_release=self.Nav,
            )
        )

        # Add the grids to the content layout
        content_layout.add_widget(services_grid1)
        content_layout.add_widget(services_grid2)
        content_layout.add_widget(services_grid3)

        # Add the content layout to the scroll view
        scroll_view.add_widget(content_layout)

        # Add the scroll view to the main layout
        main_layout.add_widget(scroll_view)

        self.add_widget(main_layout)

    def Nav(self, page):
        self.manager.current = page
