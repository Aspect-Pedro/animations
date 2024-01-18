from manim import *

PATH = 'C:\\Users\Pedro\Desktop\manimAnimations\images'

class Animate(Scene):
    def construct(self):
         # Number of terms
        num_terms = 63

        # Original expression
        original_expression = MathTex(*[f"2 *" for _ in range(num_terms)], r"2").scale(0.3)

        # Exponential expression
        exponential_expression = MathTex("2^{64}")

        # Position the expressions
        original_expression.shift(UP)
        exponential_expression.next_to(original_expression, DOWN)

        # Display the original expression
        self.play(Write(original_expression))

        # Transform the original expression into the exponential expression
        self.play(
            Transform(original_expression, exponential_expression),
            run_time=3
        )

        self.wait()
        

class Animate2(Scene):
    def construct(self):
        value = 2**64
        # Create a grid of the expression
        expression_grid = self.create_expression_grid()
        exponential_expression = MathTex(f"2^{{64}} = {value}")

        # Display the original expression and expression grid #
        expression_grid.shift(UP*1.5)
        self.play(Write(expression_grid), run_time=4.5)
        brace = Brace(expression_grid, direction=UP)
        caption = brace.get_text("64 Bits")
        self.play(GrowFromCenter(brace), Write(caption),run_time=1.5)
        self.wait(1)
        self.play(
            brace.animate.scale(0.1).fade(1),
            caption.animate.scale(0.1).fade(1)
        )
        self.play(Transform(expression_grid, exponential_expression,run_time=1.5))
        self.wait(2)

    def create_expression_grid(self):
        num_copies = 8  # Number of rows
        expression_grid = VGroup()

        for _ in range(num_copies):
            row_expression = MathTex(*[r"2 \times" for _ in range(8)], r"2").scale(0.8)
            row_expression.next_to(expression_grid, DOWN, buff=0.1)
            expression_grid.add(row_expression)

        return expression_grid