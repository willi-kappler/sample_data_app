from typing import override

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

class SDEditScreen(Screen):
    def __init__(self, main_app, name: str):
        print("Init edit screen")

        self.main_app = main_app

        super(SDEditScreen, self).__init__(name=name)

        layout = BoxLayout(orientation="vertical")

        self.qr_label = Label(text="Empty")

        save_button = Button(text="Save")
        save_button.bind(on_release=self.save_data)

        layout.add_widget(self.qr_label)
        layout.add_widget(save_button)

        self.add_widget(layout)

    @override
    def on_enter(self, *args):
        self.qr_label.text = self.main_app.qr_data

    def save_data(self, obj):
        self.main_app.main_screen()

