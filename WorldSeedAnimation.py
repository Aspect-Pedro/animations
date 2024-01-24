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


class WorldSize(Scene):
    def construct(self):
        earth = ImageMobject(f"{PATH}\\Earth.png").scale(0.3).to_edge(LEFT,buff=2.5)
        self.play(FadeIn(earth))

        earthName = Text("Terra", font="Minecraftia",font_size=24).next_to(earth,DOWN)
        earthSurfaceArea = Text("Área: 510,064,000km²",font="Minecraftia",font_size=24).next_to(earth,UP)
        earthRadius = Text("Raio: 6,371km",font="Minecraftia",font_size=24).next_to(earthSurfaceArea,UP)
        self.play(Write(VGroup(earthName,earthSurfaceArea, earthRadius)))
        
        minecraftMap = ImageMobject(f"{PATH}\\MinecraftWorldSingle.png").to_edge(RIGHT, buff=2.5)
        minecraftName = Text("Minecraft Map", font="Minecraftia",font_size=24).next_to(minecraftMap,DOWN)
        minecraftSurfaceArea = Text("Área: 3,600,000,000km²",font="Minecraftia",font_size=24).next_to(minecraftMap,UP)
        minecraftRadius = Text("Raio: 16,925km",font="Minecraftia",font_size=24).next_to(minecraftSurfaceArea,UP)

        self.play(FadeIn(minecraftMap))
        self.play(Write(VGroup(minecraftName,minecraftSurfaceArea,minecraftRadius)))
        
        self.wait(2)
        



class PerlinNoise(Scene):
    def construct(self):
        noiseImg = ImageMobject(f"{PATH}\\PerlinNoise.png").scale(2)
        self.play(FadeIn(noiseImg))
        perlin = Text("Perlin noise",font="Minecraftia",font_size=30).next_to(noiseImg,DOWN)
        self.play(Write(perlin))
        self.wait(4)

class WhiteNoise(Scene):
    def construct(self):
        noiseImg = ImageMobject(f"{PATH}\\WhiteNoise.jpeg").scale(2)
        self.play(FadeIn(noiseImg))
        perlin = Text("White noise",font="Minecraftia",font_size=30).next_to(noiseImg,DOWN)
        self.play(Write(perlin))
        self.wait(4)