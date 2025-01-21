
from typing import override
import json
import os

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from sd_main_menu import SDMainScreen
from sd_scan_qr import SDQRScreen
from sd_edit_data import SDEditScreen
from sd_list_view import SDListViewScreen
from sd_show_error import SDErrorScreen
from sd_choose_file import SDChooseFileScreen
from sd_confirm_delete import SDConfirmDeleteScreen

class SDApp(App):
    def __init__(self):
        print("Init app")

        self.all_data = {}
        self.tmp_data = {}

        super(SDApp, self).__init__()

        # Load sample data from json file if available:
        if os.path.exists("sample_data.json"):
            with open("sample_data.json") as jf:
                self.all_data = json.load(jf)

    @override
    def build(self):
        print("Build app")

        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(SDMainScreen(self, "main_screen"))
        self.screen_manager.add_widget(SDQRScreen(self, "scan_screen"))
        self.screen_manager.add_widget(SDEditScreen(self, "edit_screen"))
        self.screen_manager.add_widget(SDListViewScreen(self, "list_view_screen"))
        self.screen_manager.add_widget(SDErrorScreen(self, "error_screen"))
        self.screen_manager.add_widget(SDChooseFileScreen(self, "choose_file_screen"))
        self.screen_manager.add_widget(SDConfirmDeleteScreen(self, "confirm_delete_screen"))

        self.screen_manager.current = "main_screen"

        return self.screen_manager

    def main_screen(self):
        self.screen_manager.current = "main_screen"

    def scan_screen(self):
        self.screen_manager.current = "scan_screen"

    def edit_screen(self):
        self.screen_manager.current = "edit_screen"

    def list_view_screen(self):
        self.screen_manager.current = "list_view_screen"

    def choose_file_screen(self):
        self.screen_manager.current = "choose_file_screen"

    def error_screen(self):
        if "error" in self.tmp_data:
            self.screen_manager.current = "error_screen"

    def confirm_delete_screen(self):
        self.screen_manager.current = "confirm_delete_screen"

    def save_to_file(self):
        with open("sample_data.json", "w") as jf:
            json.dump(self.all_data, jf)

    def save_data(self, qr_id, data):
        if qr_id:
            print("Save data...")
            self.all_data[qr_id] = data
            print(f"Number of sets: {len(self.all_data)}")
            self.save_to_file()

    def clean_tmp_data(self):
        self.tmp_data = {}

    def delete_item(self, qr_id: str):
        if qr_id in self.all_data:
            del self.all_data[qr_id]
            self.save_to_file()

    def quit(self):
        self.stop()


if __name__ == "__main__":
    sd_app = SDApp()
    sd_app.run()

