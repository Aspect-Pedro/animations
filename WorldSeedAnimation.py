from manim import *

PATH = 'C:\\Users\Pedro\Desktop\manimAnimations\images'

class Animate(Scene):
    def construct(self):
        map = ImageMobject(f"{PATH}\\MinecraftMap.png").move_to([0, -1, 0]);
        map.height = 2.5
        number = always_redraw(lambda: Text("Seed: 12432275434", font="Minecraftia").next_to(map,UP,buff=1.5));
        arrow = always_redraw(lambda: Line(start=number.get_bottom(),end=map.get_top(), buff=0.2).add_tip())
        self.play(DrawBorderThenFill(number))
        self.play(FadeIn(map))
        self.play(DrawBorderThenFill(arrow))
        self.play(number.animate.shift(LEFT*2),map.animate.shift(LEFT*2))
        map2 = ImageMobject(f"{PATH}\\MinecraftMap2.png").next_to(map,RIGHT, buff=1)
        map2.height = 2.5
        arrow2 = Line(start=number.get_bottom(), end=map2.get_top(),buff=0.5).add_tip();
        self.play(DrawBorderThenFill(arrow2),FadeIn(map2))
        icon = SVGMobject(f"{PATH}\\Red_X.svg").move_to(arrow2.get_midpoint()).scale(0.2)
        self.play(DrawBorderThenFill(icon))
        self.wait(2)
