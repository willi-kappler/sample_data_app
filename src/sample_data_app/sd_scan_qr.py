from typing import override
import numpy as np
import cv2

from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.screenmanager import Screen


class SDQRScreen(Screen):

    def __init__(self, main_app, name: str):
        print("Init scan screen")

        self.main_app = main_app
        self.cam = Camera(resolution=(640, 480), size_hint=(1.0, 3.0))
        self.cam.play = False

        super(SDQRScreen, self).__init__(name=name)

        layout = BoxLayout(orientation="vertical")

        scan_button = Button(text="Scan QR code")
        scan_button.bind(on_release=self.scan_image)
        cancel_button = Button(text="Cancel")
        cancel_button.bind(on_release=self.cancel_scan)

        layout.add_widget(self.cam)
        layout.add_widget(scan_button)
        layout.add_widget(cancel_button)

        self.add_widget(layout)

    @override
    def on_enter(self, *args):
        self.cam.play = True

    @override
    def on_leave(self, *args):
        self.cam.play = False

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
            self.main_app.store_data(data)
            self.main_app.edit_screen()
        else:
            print("There was some error")
            self.main_app.error = "Unknown QR code"
            self.main_app.error_screen()

    def cancel_scan(self, obj):
        print("Go back to main menu...")
        self.main_app.main_screen()

