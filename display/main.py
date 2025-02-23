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

# ตั้งค่าฟอนต์ที่รองรับภาษาไทย
LabelBase.register(name="ThaiFont", fn_regular="../fonts/THSarabunNew.ttf")

# ใช้ฟอนต์ใน Label
label = Label(text="สวัสดี", font_name="ThaiFont")

# เชื่อมต่อกับ MongoDB
client = MongoClient("localhost", 27017)
db = client["rescue_app"]
users_collection = db["users"]
reports_collection = db["reports"]

# ตรวจสอบและสร้างข้อมูลผู้ใช้และรายงานหากไม่มี
if users_collection.count_documents({}) == 0:
    users_collection.insert_many(
        [
            {"username": "admin", "password": "admin123", "role": "admin"},
            {"username": "user", "password": "user123", "role": "user"},
        ]
    )

# ตรวจสอบว่าคอลเลกชัน reports ว่างเปล่า
if reports_collection.count_documents({}) == 0:
    # เพิ่มเอกสารเริ่มต้นหากคอลเลกชันว่าง
    reports_collection.insert_one(
        {"location": "Initial Location", "description": "Initial Description"}
    )


# หน้าจอ Login
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


# หน้าจอ Admin
class AdminScreen(Screen):
    pass


# หน้าจอ User (Sender)
class UserScreen(Screen):
    def send_report(self):
        location = self.ids.location_input.text
        description = self.ids.description_input.text

        if location and description:
            report = {"location": location, "description": description}

            # เพิ่มรายงานใหม่ใน MongoDB
            reports_collection.insert_one(report)

            # ล้างช่อง input
            self.ids.location_input.text = ""
            self.ids.description_input.text = ""

            # แสดง Popup แจ้งเตือน
            popup = Popup(
                title="Success",
                content=Label(text="Report sent successfully!"),
                size_hint=(0.8, 0.4),
            )
            popup.open()
        else:
            popup = Popup(
                title="Error",
                content=Label(text="Please fill all fields!"),
                size_hint=(0.8, 0.4),
            )
            popup.open()


# หน้าจอ Receiver
class ReceiverScreen(Screen):
    def load_reports(self):
        # อ่านรายงานจาก MongoDB
        reports = reports_collection.find()

        # ล้างรายการเก่า
        self.ids.reports_container.clear_widgets()

        # แสดงรายงานใหม่
        for report in reports:
            report_text = f"Location: {report['location']}\nDescription: {report['description']}\n"
            self.ids.reports_container.add_widget(
                Label(
                    text=report_text, font_name="ThaiFont", size_hint_y=None, height=100
                )
            )


# จัดการหน้าจอ
class RescueApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(AdminScreen(name="admin"))
        sm.add_widget(UserScreen(name="user"))
        sm.add_widget(ReceiverScreen(name="receiver"))
        return sm


if __name__ == "__main__":
    RescueApp().run()
