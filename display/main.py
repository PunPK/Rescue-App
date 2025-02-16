from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
import json
import os

# ตรวจสอบและสร้างไฟล์ข้อมูลผู้ใช้และรายงานหากไม่มี
if not os.path.exists("data/users.json"):
    os.makedirs("data", exist_ok=True)
    with open("data/users.json", "w") as f:
        json.dump(
            {
                "admin": {"password": "admin123", "role": "admin"},
                "user": {"password": "user123", "role": "user"},
            },
            f,
        )

if not os.path.exists("data/reports.json"):
    with open("data/reports.json", "w") as f:
        json.dump([], f)


# หน้าจอ Login
class LoginScreen(Screen):
    def login(self):
        username = self.ids.username_input.text
        password = self.ids.password_input.text

        with open("data/users.json", "r") as f:
            users = json.load(f)

        if username in users and users[username]["password"] == password:
            role = users[username]["role"]
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

            # อ่านข้อมูลเดิมและเพิ่มรายงานใหม่
            with open("data/reports.json", "r") as f:
                reports = json.load(f)
            reports.append(report)

            # บันทึกรายงานใหม่
            with open("data/reports.json", "w") as f:
                json.dump(reports, f)

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
        # อ่านรายงานจากไฟล์
        with open("data/reports.json", "r") as f:
            reports = json.load(f)

        # ล้างรายการเก่า
        self.ids.reports_container.clear_widgets()

        # แสดงรายงานใหม่
        for report in reports:
            report_text = f"Location: {report['location']}\nDescription: {report['description']}\n"
            self.ids.reports_container.add_widget(
                Label(text=report_text, size_hint_y=None, height=100)
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
