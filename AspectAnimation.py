from manim import *


class WriteName(Scene):
    def construct(self):
        letter = Text(
            "Aspect Pedro",
            font="Hi Jack" ,color=WHITE, font_size=100).move_to([0,0, 0]
        )
        
    
        animations = [
            FadeOut(letter[0]),
            letter[1].animate.scale(.6),
            FadeOut(letter[3]),
            FadeOut(letter[4]),
            FadeOut(letter[5]),
            FadeOut(letter[7]),
            FadeOut(letter[8]),
            FadeOut(letter[9]),
            FadeOut(letter[10]),
        ]
        
        
        self.play(DrawBorderThenFill(letter))
        self.play(AnimationGroup(*animations))
        
        self.play(letter[2].animate.shift(RIGHT*2.3),letter[6].animate.flip().shift(LEFT * 0.85), letter[1].animate.move_to([-0.15,-0.35,0]))

        # name = Text("Aspect Pedro", font_size=20, font="Hi Jack").move_to([-0.10, .9, 0])
        
        # self.play(FadeIn(name))
        

        self.wait(1.5)
        # offset = 0
        # for index,char in enumerate(CHANNEL_NAME):
        #     letter = Text(char, font="Hi Jack", color=WHITE, font_size=100).move_to([-3 + offset,0, 0])            

        #     self.play(DrawBorderThenFill(letter))
        #     offset += 1

        




class Logo(Scene):
    def construct(self):
        firstP = Text("P", font="Hi Jack", color=WHITE, font_size=100)
        secondP = Text("P", font="Hi Jack", color=WHITE, font_size=100).next_to(firstP,RIGHT,buff=-0.3).flip()
        
        self.play(DrawBorderThenFill(VGroup(firstP, secondP)))
        self.wait(3)