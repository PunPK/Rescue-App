# from kivy.core.text import LabelBase

# LabelBase.register(name="ThaiFont", fn_regular="correct/path/to/THSarabunNew.ttf")

# import os
# from kivy.lang import Builder

# kv_path = os.path.join(os.path.dirname(__file__), "screen", "ReportScreen.kv")
# Builder.load_file(kv_path)

from .ReportScreen import ReceiverScreen
from .db_connection import *
from .card_page import *
from .LoginScreen import LoginScreen
from .RegistrationPage import RegistrationScreen
from .HomePage import MainScreen
from .ruam_ber import Ruem_ber
from .MyDevelopPage import MyDevelop
from .ApplicationInfo import ApplicationInfoScreen
from .home_admin import Home_Admin
from .tool_page import Tool_page
from .MapScreen import MapViewScreen
from .card_page import Card_page, EditCardScreen, CreateCardScreen
from .safty_tips_management import Tips_page, EditTipScreen, CreateTipScreen
from .salfty_tips import Tips_page
from .SymbolPage import SymbolScreen

# from .BottonNavItem import BottomNavBar
