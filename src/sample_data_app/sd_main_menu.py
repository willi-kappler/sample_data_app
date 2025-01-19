from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

class SDMainScreen(Screen):
    def __init__(self, main_app, name: str):
        print("Init main screen")

        self.main_app = main_app

        super(SDMainScreen, self).__init__(name=name)

        layout = BoxLayout(orientation="vertical")

        scan_button = Button(text="Scan QR code")
        scan_button.bind(on_release=lambda obj: self.main_app.scan_screen())
        edit_button = Button(text="Edit Data")
        edit_button.bind(on_release=lambda obj: self.main_app.edit_screen())
        quit_button = Button(text="Quit")
        quit_button.bind(on_release=lambda obj: self.main_app.quit())

        layout.add_widget(scan_button)
        layout.add_widget(edit_button)
        layout.add_widget(quit_button)

        self.add_widget(layout)

