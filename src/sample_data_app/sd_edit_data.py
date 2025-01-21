from typing import override

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.utils import platform

from plyer import gps

class SDEditScreen(Screen):
    def __init__(self, main_app, name: str):
        print("Init edit screen")

        self.main_app = main_app

        super(SDEditScreen, self).__init__(name=name)

        # Try to setup GPS:
        self.has_gps = False
        try:
            gps.configure(on_location=self.process_gps_location) # type: ignore

            if platform == "android":
                self.request_android_permissions()

            self.has_gps = True
        except NotImplementedError:
            print("GPS is not available")

        layout = BoxLayout(orientation="vertical")

        # First row
        label = Button(text="QR ID:", disabled=True)
        self.qr_label = Button(text="", disabled=True, text_size=(200, None))
        row_layout = BoxLayout(orientation="horizontal")
        row_layout.add_widget(label)
        row_layout.add_widget(self.qr_label)
        layout.add_widget(row_layout)

        # Second row
        label = Button(text="Description:", disabled=True)
        self.description = TextInput(multiline=False)
        row_layout = BoxLayout(orientation="horizontal")
        row_layout.add_widget(label)
        row_layout.add_widget(self.description)
        layout.add_widget(row_layout)

        # Third row
        label = Button(text="GPS location:", disabled=True)
        self.gps_location = TextInput(multiline=False)
        row_layout = BoxLayout(orientation="horizontal")
        row_layout.add_widget(label)
        row_layout.add_widget(self.gps_location)
        layout.add_widget(row_layout)

        if self.has_gps:
            button_start = Button(text="Start GPS")
            button_start.bind(on_release=lambda obj: gps.start()) # type: ignore
            button_stop = Button(text="Stop GPS")
            button_stop.bind(on_release=lambda obj: gps.stop()) # type: ignore
            row_layout = BoxLayout(orientation="horizontal")
            row_layout.add_widget(button_start)
            row_layout.add_widget(button_stop)
            layout.add_widget(row_layout)

        # Fourth row
        button = Button(text="Select a photo")
        button.bind(on_release=self.select_photo) # type: ignore
        self.image = Image()
        row_layout = BoxLayout(orientation="horizontal")
        row_layout.add_widget(button)
        row_layout.add_widget(self.image)
        layout.add_widget(row_layout)

        # Last row
        save_button = Button(text="Save")
        save_button.bind(on_release=self.save_data) # type: ignore
        cancel_button = Button(text="Cancel")
        cancel_button.bind(on_release=self.cancel_edit) # type: ignore
        row_layout = BoxLayout(orientation="horizontal")
        row_layout.add_widget(save_button)
        row_layout.add_widget(cancel_button)
        layout.add_widget(row_layout)

        scroll_view = ScrollView(do_scroll_x=False)
        scroll_view.add_widget(layout)

        self.add_widget(scroll_view)

    @override
    def on_pre_enter(self, *args):
        tmp_data = self.main_app.tmp_data

        if "qr_id" in tmp_data:
            qr_id = tmp_data["qr_id"]
            self.qr_label.text = qr_id

            if qr_id in self.main_app.all_data:
                current_data = self.main_app.all_data[qr_id]
                self.description.text = current_data["description"]
                self.gps_location.text = current_data["gps_location"]
                self.image.source = current_data["image_path"]
                return
        else:
            self.qr_label.text = ""

        if "description" in tmp_data:
            self.description.text = tmp_data["description"]
        else:
            self.description.text = ""

        if "gps_location" in tmp_data:
            self.gps_location.text = tmp_data["gps_location"]
        else:
            self.gps_location.text = ""

        if "image_path" in tmp_data:
            self.image.source = tmp_data["image_path"]
        else:
            self.image.source = ""

    def save_data(self, obj):
        data = {
                 "description": self.description.text,
                 "gps_location": self.gps_location.text,
                 "image_path": self.image.source
               }
        self.main_app.save_data(self.qr_label.text, data)
        self.main_app.clean_tmp_data()
        self.main_app.main_screen()

    def cancel_edit(self, obj):
        self.main_app.clean_tmp_data()
        self.main_app.main_screen()

    def select_photo(self, obj):
        tmp_data = self.main_app.tmp_data
        tmp_data["description"] = self.description.text
        tmp_data["gps_location"] = self.gps_location.text
        self.main_app.choose_file_screen()

    def process_gps_location(self, **kwargs):
        lat = kwargs["lat"]
        lon = kwargs["lon"]

        self.gps_location.text = f"{lat=}, {lon=}"

    def request_android_permissions(self):
        # From the GPS example:
        # https://github.com/kivy/plyer/blob/master/examples/gps/main.py

        from android.permissions import request_permissions, Permission # type: ignore

        request_permissions([Permission.ACCESS_COARSE_LOCATION, Permission.ACCESS_FINE_LOCATION])

