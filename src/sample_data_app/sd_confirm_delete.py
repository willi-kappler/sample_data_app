from typing import override

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image


class SDConfirmDeleteScreen(Screen):
    def __init__(self, main_app, name: str):
        print("Init confirm delete screen")

        self.main_app = main_app

        super(SDConfirmDeleteScreen, self).__init__(name=name)

        self.qr_id = ""

        layout = BoxLayout(orientation="vertical")

        # First row
        self.description = Button(text="", disabled=True)
        self.image = Image()
        row_layout = BoxLayout(orientation="horizontal")
        row_layout.add_widget(self.description)
        row_layout.add_widget(self.image)
        layout.add_widget(row_layout)

        # Second row
        label = Button(text="Delete this item ?", disabled=True)
        layout.add_widget(label)

        # Third row
        button1 = Button(text="Yes, delete", background_color=(1, 0, 0, 1))
        button1.bind(on_release=self.delete_item) # type: ignore
        button2 = Button(text="Cancel")
        button2.bind(on_release=lambda obj: self.main_app.list_view_screen()) # type: ignore
        row_layout = BoxLayout(orientation="horizontal")
        row_layout.add_widget(button1)
        row_layout.add_widget(button2)
        layout.add_widget(row_layout)

        self.add_widget(layout)

    @override
    def on_pre_enter(self, *args):
        self.qr_id = self.main_app.tmp_data["qr_id"]
        self.main_app.clean_tmp_data()

        all_data = self.main_app.all_data
        if self.qr_id in all_data:
            data = all_data[self.qr_id]
            self.description.text = data["description"]
            self.image.source = data["image_path"]

    def delete_item(self, obj):
        self.main_app.delete_item(self.qr_id)
        self.main_app.list_view_screen()


