from typing import override

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.image import Image

class SDListViewScreen(Screen):
    def __init__(self, main_app, name: str):
        print("Init list view screen")

        self.main_app = main_app

        super(SDListViewScreen, self).__init__(name=name)

        self.layout = BoxLayout(orientation="vertical")

        self.scroll_view = ScrollView(do_scroll_x=False)
        self.scroll_view.add_widget(self.layout)

        self.add_widget(self.scroll_view)

    @override
    def on_pre_enter(self, *args):
        self.scroll_view.clear_widgets()
        self.layout.clear_widgets()

        all_data = self.main_app.all_data
        all_data_len = len(all_data)

        if all_data_len > 0:
            for k, v in all_data.items():
                # First row
                label1 = Button(text=k, disabled=True, text_size=(200, None))
                label2 = Image(source=v["image_path"])
                row_layout = BoxLayout(orientation="horizontal")
                row_layout.add_widget(label1)
                row_layout.add_widget(label2)
                self.layout.add_widget(row_layout)

                # Second row
                label1 = Button(text=v["description"], disabled=True, text_size=(200, None))
                label2 = Button(text=v["gps_location"], disabled=True, text_size=(200, None))
                row_layout = BoxLayout(orientation="horizontal")
                row_layout.add_widget(label1)
                row_layout.add_widget(label2)
                self.layout.add_widget(row_layout)

                # Third row
                label = Button(text="", disabled=True, size_hint=(4.0, 1.0),
                    background_normal="", background_color=(0,0,0,1))
                button1 = Button(text="Edit")
                button1.bind(on_release=lambda obj, bound_id=k: self.edit_data(bound_id)) # type: ignore
                button2 = Button(text="Delete", background_color=(1,0,0,1))
                button2.bind(on_release=lambda obj, bound_id=k: self.delete_data(bound_id)) # type: ignore
                row_layout = BoxLayout(orientation="horizontal")
                row_layout.add_widget(label)
                row_layout.add_widget(button1)
                row_layout.add_widget(button2)
                self.layout.add_widget(row_layout)

                label = Button(text="", disabled=True, size_hint=(1.0, 0.2),
                    background_normal="", background_color=(0,0,0,1))
                self.layout.add_widget(label)
        else:
            label = Button(text="No data", disabled=True)
            self.layout.add_widget(label)

        back = Button(text="Back")
        back.bind(on_release=self.back_to_main) # type: ignore
        self.layout.add_widget(back)
        self.layout.size_hint_y = None
        self.layout.height = all_data_len * 300
        self.scroll_view.add_widget(self.layout)

    def delete_data(self, qr_id: str):
        self.main_app.clean_tmp_data()
        self.main_app.tmp_data["qr_id"] = qr_id
        self.main_app.confirm_delete_screen()

    def edit_data(self, qr_id: str):
        self.main_app.clean_tmp_data()
        self.main_app.tmp_data["qr_id"] = qr_id
        self.main_app.edit_screen()

    def back_to_main(self, obj):
        self.main_app.main_screen()

