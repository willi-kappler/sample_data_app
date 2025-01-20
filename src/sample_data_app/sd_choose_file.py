
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView

class SDChooseFileScreen(Screen):
    def __init__(self, main_app, name: str):
        print("Init choose file screen")

        self.main_app = main_app

        super(SDChooseFileScreen, self).__init__(name=name)

        layout = BoxLayout(orientation="vertical")

        file_chooser = FileChooserListView()
        file_chooser.bind(on_submit=self.get_file) # type: ignore

        layout.add_widget(file_chooser)

        self.add_widget(layout)

    def get_file(self, *args):
        file_name = args[1][0]
        print(f"{file_name=}")
        self.main_app.tmp_data["image_path"] = file_name
        self.main_app.edit_screen()


