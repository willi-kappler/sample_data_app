from kivy.app import App
#from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout

import plyer

class SDApp(App):
    def build(self):
        parent = AnchorLayout(anchor_x="center", anchor_y="top")

        scan_button = Button(text="Scan QR code")
        scan_button.bind(on_release=self.scan_image)

        parent.add_widget(scan_button)

        return parent

    def scan_image(self, obj):
        print("Scan image...")
        try:
            plyer.camera.take_picture("qr_code", self.scan_qr_code)
        except NotImplementedError:
            print("Camera not available...")

    def scan_qr_code(self):
        pass

if __name__ == "__main__":
    sd_app = SDApp()
    sd_app.run()

