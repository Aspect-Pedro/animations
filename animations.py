from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(RED_C, opacity=0.5)  # set the color and transparency
        
        square = Square() # Create a square
        square.rotate(PI / 4) # Rotate a certain amount
        square.set_fill(BLUE, opacity=0.5)
        
        square.next_to(circle, LEFT, buff=0.1) # Set the position
        
        self.play(Create(square))  # show the circle on screen
        self.play(FadeOut(square)) # Fade out animation
        self.play(Create(circle), Create(square))
        self.play(FadeOut(square)) # Fade out animation

        