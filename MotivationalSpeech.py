from manim import *

PATH = 'C:\\Users\Pedro\Desktop\manimAnimations\images'

class RockySpeech(Scene):
    def construct(self):
        
        rocky = ImageMobject(f"{PATH}\\RockyBalboa.png").shift(LEFT * 4.5)

        quote1 = Text('"Não importa como você bate e sim',font="Fira Code",font_size=24).next_to(rocky,RIGHT,buff=1.6)
        quote2 = Text('o quanto aguenta apanhar e continuar lutando."',font="Fira Code",font_size=24).next_to(quote1,DOWN)

        self.play(FadeIn(rocky),Write(quote1))
        self.play(Write(quote2))

        owner = Text('~Rocky, Balboa',font="Fira Code",font_size=16).next_to(quote2,DR).shift(LEFT * 3)
        self.play(Write(owner))

        self.wait(2)

class DogSpeech(Scene):
    def construct(self):
        
        rocky = ImageMobject(f"{PATH}\\Cachorrinho.jpg").shift(LEFT * 4).scale(0.8)

        quote1 = Text('"Seja a pessoa que o seu cachorro',font="Fira Code",font_size=24).next_to(rocky,RIGHT,buff=1)
        quote2 = Text('acredita que você é."',font="Fira Code",font_size=24).next_to(quote1,DOWN)

        self.play(FadeIn(rocky),Write(quote1))
        self.play(Write(quote2))

        owner = Text('~Desconhecido',font="Fira Code",font_size=16).next_to(quote2,DR).shift(LEFT )
        self.play(Write(owner))

        self.wait(2)