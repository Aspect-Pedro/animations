from manim import *
import random

class PerlinNoise(Scene):
    def construct(self):
        grid = NumberPlane(
            x_range=(-4, 4, 1),
            y_range=(-3, 3, 1),
            axis_config={"color": GRAY},
            background_line_style={"stroke_width": 1, "stroke_color": WHITE,"stroke_opacity": 1},
        ).scale(2)
        
        self.play(Write(grid));
        self.wait(5)
        
        randomDotsArray = VGroup()
        randomX = 0
        randomY = 0
        
        for x in range(-1,2,2):
            for y in range(-1,2,2):
                if x is -1:
                    randomX = random.uniform(x, x+1)
                
                if x is 1:
                    randomX = random.uniform(x-1,x)

                if y is -1:
                    randomY = random.uniform(y, y+1)
                
                if y is 1:
                    randomY = random.uniform(y-1,y)

                randomDot = Dot(point=grid.c2p(randomX,randomY),color=YELLOW)
                randomDotsArray.add(randomDot)

                if x is 1 and y is 1:
                    line1 = Line(randomDot,Dot(point=grid.c2p(x,y)))
                    line2 = Line(randomDot,Dot(point=grid.c2p(x-1,y-1)))
                    line3 = Line(randomDot,Dot(point=grid.c2p(x-1,y)))
                    line4 = Line(randomDot,Dot(point=grid.c2p(x,y-1)))

                    randomDotsArray.add(line1,line2,line3,line4)
                    
                if x is -1 and y is 1:
                    line1 = Line(randomDot,Dot(point=grid.c2p(x,y)))
                    line2 = Line(randomDot,Dot(point=grid.c2p(x+1,y-1)))
                    line3 = Line(randomDot,Dot(point=grid.c2p(x+1,y)))
                    line4 = Line(randomDot,Dot(point=grid.c2p(x,y-1)))

                    randomDotsArray.add(line1,line2,line3,line4)
                    
                if x is 1 and y is -1:
                    line1 = Line(randomDot,Dot(point=grid.c2p(x,y)))
                    line2 = Line(randomDot,Dot(point=grid.c2p(x-1,y+1)))
                    line3 = Line(randomDot,Dot(point=grid.c2p(x-1,y)))
                    line4 = Line(randomDot,Dot(point=grid.c2p(x,y+1)))

                    randomDotsArray.add(line1,line2,line3,line4)

                if x is -1 and y is -1:
                    line1 = Line(randomDot,Dot(point=grid.c2p(x,y)))
                    line2 = Line(randomDot,Dot(point=grid.c2p(x+1,y+1)))
                    line3 = Line(randomDot,Dot(point=grid.c2p(x+1,y)))
                    line4 = Line(randomDot,Dot(point=grid.c2p(x,y+1)))

                    randomDotsArray.add(line1,line2,line3,line4)
                    

                    

        
        # self.play(DrawBorderThenFill(randomDotsArray))
        
        dotsArray = VGroup()
        for i in range(3):
            for j in range(3):
                edge = Dot(point=grid.c2p(i-1,j-1),color=RED)
                dotsArray.add(edge)
                randomx = random.choice([-0.5,0.5])
                randomy = random.choice([-0.5,0.5])


                random_vector = Line(
                    grid.c2p(i-1, j-1),
                    grid.c2p((i - 1) + randomx, (j - 1) + randomy),
                    buff=0,
                    color=RED
                )
                
                dotsArray.add(random_vector)
                
        self.play(DrawBorderThenFill(VGroup(*dotsArray)))
        
        self.wait(4)
        
        self.play(DrawBorderThenFill(randomDotsArray))
        
        self.wait(6)
        
        self.play(grid.animate.shift(7 * LEFT),dotsArray.animate.shift(3*LEFT),randomDotsArray.animate.shift(3*LEFT))

        self.wait(2)
        
        dotProductText = Text("Produto Escalar",font="Fira Code",font_size=24).next_to(grid,RIGHT * 2,buff=0.6).shift(UP)
        self.play(Write(dotProductText))
        
        dotProductFormula = MathTex(
            r"\mathbf{a} \cdot \mathbf{b} = |\mathbf{a}| \cdot |\mathbf{b}| \cdot \cos(\theta)",
        ).next_to(dotProductText,DOWN).scale(0.8)
        
        self.play(Write(dotProductFormula))

        cubicInterpolationText = Text("Interpolação Cúbica",font="Fira Code",font_size=24).next_to(dotProductFormula,DOWN,buff=0.6)
        
        self.play(Write(cubicInterpolationText))

        cubicInterpolationFormula = MathTex(
            "f(t) = (1 - t)^3 \\cdot P_0 + 3(1 - t)^2 \\cdot t \\cdot P_1",
            "+ 3(1 - t) \\cdot t^2 \\cdot P_2 + t^3 \\cdot P_3"
        ).scale(0.5).next_to(cubicInterpolationText,DOWN).shift(LEFT*0.5)
        
        self.play(Write(cubicInterpolationFormula))

        self.wait(2)

class PerlinNoiseFormula(Scene):
    def construct(self):
        dotProductText = Text("Produto Escalar",font="Fira Code",font_size=24).shift(UP * 2)
        self.play(Write(dotProductText))
        
        dotProductFormula = MathTex(
            r"\mathbf{a} \cdot \mathbf{b} = |\mathbf{a}| \cdot |\mathbf{b}| \cdot \cos(\theta)",
        ).next_to(dotProductText,DOWN).scale(0.8)
        
        self.play(Write(dotProductFormula))

        cubicInterpolationText = Text("Interpolação Cúbica",font="Fira Code",font_size=24).next_to(dotProductFormula,DOWN,buff=0.6)
        
        self.play(Write(cubicInterpolationText))

        cubicInterpolationFormula = MathTex(
            "f(t) = (1 - t)^3 \\cdot P_0 + 3(1 - t)^2 \\cdot t \\cdot P_1",
            "+ 3(1 - t) \\cdot t^2 \\cdot P_2 + t^3 \\cdot P_3"
        ).scale(0.5).next_to(cubicInterpolationText,DOWN)
        
        self.play(Write(cubicInterpolationFormula))

        self.wait(2)
