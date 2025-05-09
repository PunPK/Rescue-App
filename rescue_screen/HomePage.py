from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty
from kivy.core.text import LabelBase
from kivy.uix.label import Label
import gridfs
from kivy.lang import Builder
from rescue_screen import ReceiverScreen
from kivy.lang import Builder
from kivymd.icon_definitions import md_icons
from rescue_screen.db_connection import reports_collection, users_collection
from kivy.uix.behaviors import ButtonBehavior
from rescue_screen.ReportScreen import ReceiverScreen
from rescue_screen.LoginScreen import LoginScreen
from rescue_screen.RegistrationPage import RegistrationScreen

# from rescue_screen.BottonNavItem import BottomNavBar

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


class ClickableImage(ButtonBehavior, Image):

    def __init__(self, link=None, **kwargs):
        super().__init__(**kwargs)
        self.link = link

    def on_release(self):
        if self.link:
            import webbrowser

            webbrowser.open(self.link)


class CircularButton(MDBoxLayout):
    def __init__(self, icon_source, title, link=None, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.adaptive_height = True
        self.spacing = dp(8)
        self.pos_hint = {"center_x": 0.5}
        self.link = link  # Store the link for later use

        # Clickable Image (without a background)
        image = ClickableImage(
            source=icon_source,
            size_hint=(None, None),
            size=(dp(70), dp(70)),  # Adjust size as needed
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            link=link,  # Pass the link to the ClickableImage
        )

        # Title
        title_label = MDLabel(
            text=title,
            halign="center",
            theme_text_color="Secondary",
            font_style="Caption",
            adaptive_height=True,
            padding=(0, dp(4)),  # Added padding for title spacing
        )

        # Adding widgets
        self.add_widget(image)
        self.add_widget(title_label)

    def open_link(self, *args):
        if self.link:
            import webbrowser

            webbrowser.open(self.link)


class BottomNavItem(MDBoxLayout):
    icon = StringProperty("")
    text = StringProperty("")
    selected = BooleanProperty(False)
    screen_name = StringProperty("")

    def navigate(self):
        app = MDApp.get_running_app()
        app.root.current = self.screen_name


class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_ui()

    def create_ui(self):
        # Main layout
        main_layout = MDBoxLayout(orientation="vertical")

        # Create a container for scrollable content
        scroll_container = MDBoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height=dp(800),  # Set a fixed height that fits the content
        )
        # Bind the height of scroll_container to its minimum height
        scroll_container.bind(minimum_height=scroll_container.setter("height"))

        # Logo section with gradient-like effect
        logo_layout = MDBoxLayout(
            orientation="vertical",
            adaptive_height=True,
            size_hint_y=None,
            height=dp(200),
            padding=[0, dp(20), 0, dp(10)],  # Reduced bottom padding
            md_bg_color=(0, 0.4, 1, 1),
        )

        # Logo image in a white circle with shadow
        logo_box = MDBoxLayout(
            size_hint=(None, None),
            size=(dp(100), dp(100)),
            pos_hint={"center_x": 0.5},
            padding=dp(10),
        )

        logo_card = MDCard(
            size_hint=(None, None),
            size=(dp(80), dp(80)),
            radius=[dp(40)],
            md_bg_color=(1, 1, 1, 1),
            elevation=3,
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )

        logo_image = Image(
            source="Image/logo.png",
            size_hint=(None, None),
            size=(dp(100), dp(100)),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )

        logo_card.add_widget(logo_image)
        logo_box.add_widget(logo_card)
        logo_layout.add_widget(logo_box)

        # App name with improved typography
        app_name = MDLabel(
            text="Rescue App",
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_style="H5",
            bold=True,
            adaptive_height=True,
        )
        logo_layout.add_widget(app_name)

        # Creator name with improved styling
        creator_name = MDLabel(
            text="Developed By CoE36",
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 0.9),
            font_style="Caption",
            adaptive_height=True,
        )
        logo_layout.add_widget(creator_name)

        # Services section
        content_layout = MDBoxLayout(
            orientation="vertical",
            padding=[dp(15), dp(15), dp(15), dp(15)],
            spacing=dp(15),
            md_bg_color=(1, 1, 1, 1),
            size_hint_y=None,
            height=dp(500),
        )

        services_label = MDLabel(
            text="Services",
            theme_text_color="Primary",
            font_style="H6",
            adaptive_height=True,
            padding=[0, 0, 0, dp(10)],  # Add some bottom padding
        )
        content_layout.add_widget(services_label)

        # Grid for service cards (2 rows of 3 cards)
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

        # Service cards - first row
        services_grid1.add_widget(
            ServiceCard(
                icon_source="Image/map_icon.png",
                title="View Map Information",
                on_release=lambda x: self.Nav("mapview"),
            )
        )
        services_grid1.add_widget(
            ServiceCard(
                icon_source="Image/help_icon.png",
                title="Safety Tips \nBy Your Self",
                on_release=lambda x: self.Nav("tipsview"),
            )
        )
        services_grid1.add_widget(
            ServiceCard(
                icon_source="Image/rescue_icon.png",
                title="Rescue \nSymbol",
                # on_release=lambda x: self.Link(
                #     "https://santofire.co.th/safety-symbol/"
                # ),
                on_release=lambda x: self.Nav("symbolview"),
            )
        )

        # Service cards - second row
        services_grid2.add_widget(
            ServiceCard(
                icon_source="Image/SignIn.png",
                title="Sign Up\nApplication",
                on_release=lambda x: self.Nav("register"),
            )
        )
        services_grid2.add_widget(
            ServiceCard(
                icon_source="Image/app_icon.png",
                on_release=lambda x: self.Nav("applicationinfo"),
                title="Application\nInformation",
            )
        )
        services_grid2.add_widget(
            ServiceCard(
                icon_source="Image/group.png",
                on_release=lambda x: self.Nav("mydevelop"),
                title="Developer\nCoE36",
            )
        )

        content_layout.add_widget(services_grid1)
        content_layout.add_widget(services_grid2)

        # Circular buttons row
        circular_buttons = MDBoxLayout(
            adaptive_height=True,
            spacing=dp(50),
            padding=[dp(20), dp(20), dp(20), dp(20)],
            pos_hint={"center_x": 0.5},
        )

        circular_buttons.add_widget(
            CircularButton(
                icon_source="Image/coepsu.png",
                title="PSU CoE36",
                link="https://www.coe.psu.ac.th",
            )
        )
        circular_buttons.add_widget(MDBoxLayout(size_hint_x=None, width=dp(50)))
        circular_buttons.add_widget(
            CircularButton(
                icon_source="Image/sf_icon.png",
                title="Safety First",
                link="https://www.youtube.com/watch?v=8DXDmI85VUw",
            )
        )

        content_layout.add_widget(circular_buttons)

        bottom_nav = MDBoxLayout(adaptive_height=True, md_bg_color=(1, 1, 1, 1))

        bottom_nav.add_widget(
            BottomNavItem(
                icon="compass-outline",
                text="Explore",
                selected=True,
                screen_name="main",
            )
        )

        bottom_nav.add_widget(
            BottomNavItem(
                icon="file-document-outline", text="Reports", screen_name="receiver"
            )
        )

        bottom_nav.add_widget(
            BottomNavItem(
                icon="account-box-multiple", text="Officer", screen_name="officer"
            )
        )

        bottom_nav.add_widget(
            BottomNavItem(icon="account-outline", text="Login", screen_name="login")
        )

        # Add logo_layout and content_layout to scroll_container
        scroll_container.add_widget(logo_layout)
        scroll_container.add_widget(content_layout)

        # Create ScrollView and add scroll_container to it
        scroll_view = ScrollView(size_hint=(1, 1))
        scroll_view.add_widget(scroll_container)

        # Add ScrollView and bottom nav to the main layout
        main_layout.add_widget(scroll_view)
        main_layout.add_widget(bottom_nav)

        self.add_widget(main_layout)

    def Nav(self, page):
        self.manager.current = page

    def Link(self, link):
        if link:
            import webbrowser

            webbrowser.open(link)
