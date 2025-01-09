
import numpy as np
import cv2

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera


class SDApp(App):
    cam = Camera(resolution=(320, 240))

    def build(self):
        #parent = AnchorLayout(anchor_x="center", anchor_y="top")
        parent = BoxLayout(orientation="vertical")

        self.cam.play = True

        scan_button = Button(text="Scan QR code")
        scan_button.bind(on_release=self.scan_image)

        parent.add_widget(self.cam)
        parent.add_widget(scan_button)

        return parent

    def scan_image(self, obj):
        print("Scan image...")

        # Get texture, size and pixel data
        texture = self.cam.texture
        height, width = texture.height, texture.width
        pixels = texture.pixels

        # Converto to image
        data = np.frombuffer(pixels, np.uint8)
        image = data.reshape(height, width, 4)

        # QR code detector
        detector = cv2.QRCodeDetector()
        data, vertices_array, binary_qrcode = detector.detectAndDecode(image)

        if vertices_array is not None:
            print(f"QRCode data: {data}")
            self.cam.play = False
        else:
            print("There was some error")


if __name__ == "__main__":
    sd_app = SDApp()
    sd_app.run()

