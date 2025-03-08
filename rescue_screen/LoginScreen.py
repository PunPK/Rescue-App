from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.core.text import LabelBase
import gridfs
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from pymongo import MongoClient, errors
from kivy.core.window import Window
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivymd.uix.button import MDFlatButton

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


class LoginScreen(MDScreen):
    def login(self):
        username = self.ids.username_input.text
        password = self.ids.password_input.text

        user = users_collection.find_one({"username": username})

        if user and user["password"] == password:
            role = user["role"]
            if role == "admin":
                self.manager.current = "main"
            elif role == "user":
                self.manager.current = "main"

        else:
            self.dialog = MDDialog(
                title="Invalid username or password!",
                text="Please try again or register new account.",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x: self.dialog.dismiss(),
                    )
                ],
            )
            self.dialog.open()

        self.ids.username_input.text = ""
        self.ids.password_input.text = ""

    def register(self):
        self.manager.current = "registration"
