from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.text import LabelBase

# ลงทะเบียนฟอนต์ภาษาไทย
LabelBase.register(
    name="ThaiFont",
    fn_regular="../fonts/THSarabunNew.ttf",
)


class ReportApp(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical")

        # ใช้ฟอนต์ใน TextInput
        self.location_input = TextInput(
            hint_text="สถานที่", font_name="ThaiFont", multiline=False
        )
        self.description_input = TextInput(
            hint_text="คำอธิบาย", font_name="ThaiFont", multiline=True
        )

        # ใช้ฟอนต์ใน Button
        self.submit_button = Button(text="ส่งรายงาน", font_name="ThaiFont")
        self.submit_button.bind(on_press=self.send_report)

        self.layout.add_widget(self.location_input)
        self.layout.add_widget(self.description_input)
        self.layout.add_widget(self.submit_button)

        return self.layout

    def send_report(self, instance):
        location = self.location_input.text
        description = self.description_input.text

        if location and description:
            report = {"location": location, "description": description}
            print(report)  # หรือทำการส่งรายงานต่อไป


if __name__ == "__main__":
    ReportApp().run()
