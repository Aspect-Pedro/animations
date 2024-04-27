from manim import *

PATH = "C:\\Users\Pedro\Desktop\manimAnimations\images"

class DeltaMouse(Scene):
    def construct(self):
        cursor = ImageMobject(PATH + "\\defaultCursor.png").scale(0.1).move_to([0,0,0])
        
        dot = Dot().move_to([-3.17,2.25,0])
        
        
        # Create a mouse
        self.play(FadeIn(cursor))
        self.play(cursor.animate.move_to([-3,2,0]))

        line = always_redraw(lambda: Line(start=cursor.get_corner(UL),end=dot.get_center(),buff=0.2))

        # deltaNumberTrackerX = ValueTracker(0)
        # deltaNumberTrackerY = ValueTracker(0)

        deltaNumber = always_redraw(lambda: Text(f"Δx: {-round(dot.get_center()[0]-cursor.get_center()[0], 2)}\nΔy: {round(dot.get_center()[1]-cursor.get_center()[1],2)}").move_to([1,1,0]).scale(0.5));
        
        
        self.play(DrawBorderThenFill(dot))
        self.play(FadeIn(line))
        
        self.add(deltaNumber)
        self.play(cursor.animate.move_to([0,0,0]))
        
        
        
        self.wait(2)

class pointsWay(Scene):
    def construct(self):
        cursor = ImageMobject(PATH + "\\defaultCursor.png").scale(0.1).move_to([0,0,0])

        self.play(FadeIn(cursor))
        self.play(cursor.animate.move_to([-3,2,0]))

        dot = Dot().move_to([-3.17,2.25,0])
        self.play(DrawBorderThenFill(dot))
        
        second_dot = Dot().move_to([-3.17,2.25,0])
        self.play(FadeIn(second_dot))
        self.play(cursor.animate.move_to([0,0,0]), second_dot.animate.move_to([-0.17,0.25,0]))
        
        # create a line and get the distance
        line = always_redraw(lambda: Line(start=dot.get_center(),end=second_dot.get_center(),buff=0.2))

        third_dot = Dot(color=YELLOW).move_to([-0.17,2.25,0]).set_opacity(0.5)
        second_line = Line(start=dot.get_center(),end=third_dot.get_center(),buff=0.2).set_opacity(0.5)
        third_line = Line(start=second_dot.get_center(),end=third_dot.get_center(),buff=0.2).set_opacity(0.5)
        
        self.play(FadeIn(line))
        self.play(FadeIn(third_dot), FadeIn(second_line), FadeIn(third_line))

        width = Text(f"width: {round(second_dot.get_center()[0]-dot.get_center()[0], 2)}").move_to([1,2,0]).scale(0.5).next_to(second_line, UP)
        height = Text(f"height: {abs(round(second_dot.get_center()[1]-dot.get_center()[1], 2))}").next_to(width, DOWN).scale(0.5).next_to(third_line, RIGHT)

        self.play(Write(width), Write(height))

        self.wait(2)


