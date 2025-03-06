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
