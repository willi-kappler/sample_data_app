from typing import override

from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class SDErrorScreen(Screen):
    def __init__(self, main_app, name: str):
        print("Init error screen")

        self.main_app = main_app

        super(SDErrorScreen, self).__init__(name=name)

        layout = BoxLayout(orientation="vertical")

        self.error_label = Button(text="Empty", disabled=True)

        ok_button = Button(text="OK")
        ok_button.bind(on_release=lambda obj: self.main_app.main_screen()) # type: ignore

        layout.add_widget(self.error_label)
        layout.add_widget(ok_button)

        self.add_widget(layout)

    @override
    def on_pre_enter(self, *args):
        tmp_data = self.main_app.tmp_data
        if "error" in tmp_data:
            self.error_label.text = self.main_app.tmp_data["error"]

