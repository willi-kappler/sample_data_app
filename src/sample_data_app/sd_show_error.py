from typing import override

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

class SDErrorScreen(Screen):
    def __init__(self, main_app, name: str):
        print("Init error screen")

        self.main_app = main_app

        super(SDErrorScreen, self).__init__(name=name)

        layout = BoxLayout(orientation="vertical")

        self.error_label = Label()

        ok_button = Button(text="OK")
        ok_button.bind(on_release=lambda obj: self.main_app.main_screen())

        layout.add_widget(self.error_label)
        layout.add_widget(ok_button)

        self.add_widget(layout)

    @override
    def on_enter(self, *args):
        self.error_label.text = self.main_app.error

