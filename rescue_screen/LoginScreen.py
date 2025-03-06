from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from pymongo import MongoClient, errors
from kivy.core.text import LabelBase
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
import gridfs
from kivy_garden.mapview import MapView, MapMarker
from kivy.lang import Builder

from kivy.core.window import Window

Window.size = (430, 740)

LabelBase.register(name="ThaiFont", fn_regular="fonts/THSarabunNew.ttf")


# label = Label(text="สวัสดี", font_name="ThaiFont")

# เชื่อมต่อกับ MongoDB
client = MongoClient("localhost", 27017)
db = client["rescue_app"]
users_collection = db["users"]
reports_collection = db["reports"]
fs = gridfs.GridFS(db)

# ตรวจสอบและสร้างข้อมูลผู้ใช้และรายงานหากไม่มี
if users_collection.count_documents({}) == 0:
    users_collection.insert_many(
        [
            {"username": "admin", "password": "admin123", "role": "admin"},
            {"username": "user", "password": "user123", "role": "user"},
        ]
    )

if reports_collection.count_documents({}) == 0:
    # เพิ่มเอกสารเริ่มต้นหากคอลเลกชันว่าง
    reports_collection.insert_one(
        {"location": "Initial Location", "description": "Initial Description"}
    )


class LoginScreen(Screen):
    def login(self):
        username = self.ids.username_input.text
        password = self.ids.password_input.text

        user = users_collection.find_one({"username": username})

        if user and user["password"] == password:
            role = user["role"]
            if role == "admin":
                self.manager.current = "admin"
            elif role == "user":
                self.manager.current = "user"
        else:
            popup = Popup(
                title="Error",
                content=Label(text="Invalid username or password!"),
                size_hint=(0.8, 0.4),
            )
            popup.open()
