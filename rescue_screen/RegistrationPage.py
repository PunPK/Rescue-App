from kivy.lang import Builder
from kivy.core.window import Window
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from pymongo import MongoClient, errors


# label = Label(text="สวัสดี", font_name="ThaiFont")

# เชื่อมต่อกับ MongoDB
client = MongoClient("localhost", 27017)
db = client["rescue_app"]
users_collection = db["users"]

Window.size = (360, 640)


class RegistrationScreen(MDScreen):
    dialog = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build()

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "700"
        # return Builder.load_string(KV)

    def show_registration_success(self):
        Username = self.ids.username_input.text
        FullName = self.ids.full_name_input.text
        Email = self.ids.email_input.text
        Password = self.ids.password_input.text

        if Username and Password:
            new_user = {
                "username": Username,
                "fullname": FullName,
                "email": Email,
                "password": Password,
                "role": "user",
            }

            # เพิ่มรายงานใหม่ใน MongoDB
            users_collection.insert_one(new_user)

            # ล้างช่อง input
            self.ids.username_input.text = ""
            self.ids.full_name_input.text = ""
            self.ids.email_input.text = ""
            self.ids.password_input.text = ""

            if not self.dialog:
                self.dialog = MDDialog(
                    title="Registration Successful!",
                    text="Your account has been created successfully.",
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
        else:
            if not self.dialog:
                self.dialog = MDDialog(
                    title="Registration Error!",
                    text="Registration have a problem. Check your new username and password",
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

    def switch_to_signin(self):
        self.manager.current = "login"
