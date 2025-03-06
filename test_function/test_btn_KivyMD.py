from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog


class MyMDApp(MDApp):
    def build(self):
        layout = MDBoxLayout()
        btn = MDRaisedButton(text="Click Me", pos_hint={"center_x": 0.5})
        btn.bind(on_release=self.open_dialog)
        layout.add_widget(btn)
        return layout

    def open_dialog(self, instance):
        self.dialog = MDDialog(
            title="Pop already show up",
            type="simple",
        )
        self.dialog.open()


MyMDApp().run()
