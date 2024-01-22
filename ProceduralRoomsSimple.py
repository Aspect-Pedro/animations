from manim import *

class ManhattanDistance(Scene):
    def construct(self):
        # Set the points
        point_start = np.array([0, 0, 0])
        p1 = np.array([1,0,0])
        p2 = np.array([1,1,0])
        p3 = np.array([2,1,0])
        point_end = np.array([2, 2, 0])
        

        # Draw the grid
        self.draw_grid()

        # Draw the points
        dot_a = Dot([0,0,0], color=RED)
        dot_1 = Dot([1,0,0], color=YELLOW)
        dot_2 = Dot([1,1,0], color=YELLOW)
        dot_3 = Dot([2,1,0], color=YELLOW)
        dot_b = Dot([2,2,0], color=GREEN)

        # Draw the line connecting the points

        line1 = Line(point_start, p1, color=YELLOW)
        line2 = Line(p1, p2, color=YELLOW)
        line3 = Line(p2, p3, color=YELLOW)
        line4 = Line(p3, point_end, color=YELLOW)

        # Draw the Manhattan distance
        manhattan_distance = Tex(f"Manhattan Distance: {abs(point_end[0] - point_start[0]) + abs(point_end[1] - point_start[1])}",color=YELLOW)
        manhattan_distance.next_to(line4, UP, buff=0.2)
        coord_start = Tex("(0,0)",color=WHITE).next_to(dot_a,LEFT/2 + [0,-0.5,0]).scale(0.7)
        coord_end = Tex("(2,2)",color=WHITE).next_to(dot_b,RIGHT/2 + [0,-0.5,0]).scale(0.7)

        # Animation
        self.play(Create(dot_a), Create(coord_start),Create(coord_end), Create(dot_b),Create(dot_1),Create(dot_2),Create(dot_3))
        self.play(Create(line1))
        self.play(Create(line2))
        self.play(Create(line3))
        self.play(Create(line4))
        self.play(Write(manhattan_distance.scale(0.7)))
        self.wait(2)

    def draw_grid(self):
        # Draw a simple grid
        grid = NumberPlane(background_line_style={
                "stroke_color": WHITE,
                "stroke_width": 2,
                "stroke_opacity": 0.2
            })
        self.add(grid)

class EuclideanDistance(Scene):
    def construct(self):
        # Set the points
        point_start = np.array([0, 0, 0])
        p1 = np.array([1,1,0])
        point_end = np.array([2, 2, 0])
        
        # Draw the grid
        self.draw_grid()

        # Draw the points
        dot_a = Dot([0,0,0], color=RED)
        dot_1 = Dot([1,1,0], color=YELLOW)
        dot_b = Dot([2,2,0], color=GREEN)

        # Draw the line connecting the points

        line1 = Line(point_start, p1, color=YELLOW)
        line2 = Line(p1, point_end, color=YELLOW)

        # Draw the Manhattan distance
        euclidean_distance = Tex(f"Distância Euclidiana: {np.linalg.norm(point_end - point_start):.2f}",color=YELLOW)
        euclidean_distance.next_to(line2, UP, buff=0.2)
        coord_start = Tex("(0,0)",color=WHITE).next_to(dot_a,LEFT/2 + [0,-0.5,0]).scale(0.7)
        coord_end = Tex("(2,2)",color=WHITE).next_to(dot_b,RIGHT/2 + [0,-0.5,0]).scale(0.7)

        # Animation
        self.play(Create(dot_a), Create(coord_start),Create(coord_end), Create(dot_b),Create(dot_1))
        self.play(Create(line1))
        self.play(Create(line2))
        self.play(Write(euclidean_distance.scale(0.7)))
        self.wait(2)

    def draw_grid(self):
        # Draw a simple grid
        grid = NumberPlane(background_line_style={
                "stroke_color": WHITE,
                "stroke_width": 2,
                "stroke_opacity": 0.2
            })
        self.add(grid)
        
class BezierAnimation(Scene):
    def construct(self):
        self.draw_grid()
        # Define control points for the Bézier curve
        p0 = np.array([0, 0, 0])
        p1 = np.array([1, 3, 0])
        p2 = np.array([3, -3, 0])
        p3 = np.array([6, 3, 0])

        # Create Bézier curve
        bezier_curve = CubicBezier(
            start_anchor=p0,
            start_handle=p1,
            end_handle=p2,
            end_anchor=p3,
            color=YELLOW
        )

        # Draw the control points
        control_points = VGroup(
            Dot(p0, color=WHITE),
            Dot(p1, color=WHITE),
            Dot(p2, color=WHITE),
            Dot(p3, color=WHITE)
        )

        # Animate the Bézier curve and control points
        self.play(Create(bezier_curve), Create(control_points),run_time=3)
        self.wait(1)
    
    def draw_grid(self):
        # Draw a simple grid
        grid = NumberPlane(background_line_style={
                "stroke_color": WHITE,
                "stroke_width": 2,
                "stroke_opacity": 0.2
            })
        self.add(grid)