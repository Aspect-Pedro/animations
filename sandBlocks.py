from manim import *

PATH = 'C:\\Users\Pedro\Desktop\manimAnimations\images'

class Animate(Scene):
    def construct(self):
        sand = ImageMobject(f"{PATH}\\SandNew.png").move_to([-0.7, 0, 0]);
        sand.height = 0.7
        number = always_redraw(lambda: Text("7", font="Fira Code").next_to(sand,RIGHT));
        self.play(DrawBorderThenFill(number), FadeIn(sand));
        self.play(sand.animate.move_to([-5, 0, 0]), run_time=2)
        zeros = Text("000 000 000 000 000 000",font="Fira Code").next_to(number,RIGHT,buff=0.4)
        self.play(DrawBorderThenFill(zeros))
        self.wait()