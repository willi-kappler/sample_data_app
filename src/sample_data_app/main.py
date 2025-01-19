
from typing import override

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from sd_main_menu import SDMainScreen
from sd_scan_qr import SDQRScreen
from sd_edit_data import SDEditScreen
from sd_show_error import SDErrorScreen

class SDApp(App):
    def __init__(self):
        print("Init app")

        self.error = ""
        self.qr_data = ""

        super(SDApp, self).__init__()

    @override
    def build(self):
        print("Build app")

        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(SDMainScreen(self, "main_screen"))
        self.screen_manager.add_widget(SDQRScreen(self, "scan_screen"))
        self.screen_manager.add_widget(SDEditScreen(self, "edit_screen"))
        self.screen_manager.add_widget(SDErrorScreen(self, "error_screen"))

        self.screen_manager.current = "main_screen"

        return self.screen_manager

    def main_screen(self):
        self.screen_manager.current = "main_screen"

    def scan_screen(self):
        self.screen_manager.current = "scan_screen"

    def edit_screen(self):
        self.screen_manager.current = "edit_screen"

    def error_screen(self):
        if self.error != "":
            self.screen_manager.current = "error_screen"

    def store_data(self, qr_data):
        self.qr_data = qr_data

    def set_error(self, error):
        self.error = error

    def quit(self):
        self.stop()


if __name__ == "__main__":
    sd_app = SDApp()
    sd_app.run()

