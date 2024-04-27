from manim import *
config.background_color = BLACK

class WritingText(Scene):
    def construct(self):
        text = Text("QR", font="Advanced Pixel-7").scale(2)
        self.play(Write(text))
        self.play(Transform(text, Text("Quick Response", font="Advanced Pixel-7").scale(2)))
        self.wait(1)

class QRCode(Scene):
    def construct(self):
        qr = SVGMobject("C:\\Users\\Pedro\\Downloads\\qrcode3.svg")
        self.play(Write(qr), run_time=5)

class BarCode(Scene):
    def construct(self):
        qr = SVGMobject("C:\\Users\\Pedro\\Downloads\\barcode.svg")
        self.play(Write(qr), run_time=5)
        self.wait(1)

class BigQRCode(Scene):
    def construct(self):
        qr = SVGMobject("C:\\Users\\Pedro\\Downloads\\QR_Code_Version_25.svg").scale(4)
        self.play(Write(qr))
        # self.add(qr)
        self.wait(1)

class BigQRCode2(Scene):
    def construct(self):
        qr = SVGMobject("C:\\Users\\Pedro\\Downloads\\QR_Code_Version_25.svg").scale(4)
        self.play(Write(qr), run_time=5)
        # self.add(qr)
        self.wait(1)