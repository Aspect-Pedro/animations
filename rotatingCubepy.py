from manim import *

class RotatingCube(ThreeDScene):
    def construct(self):
        self.begin_ambient_camera_rotation(rate=0.1)
        self.set_camera_orientation(phi=40*DEGREES, theta=-45*DEGREES)
        grid = NumberPlane().set_opacity(0.2)
        self.add(grid)
        axes = ThreeDAxes().set_opacity(0.5)
        labels = axes.get_axis_labels(
            Tex("x").scale(0.7), Text("y").scale(0.45), Text("z").scale(0.45)
        )
        self.play(Write(axes))
        axes = ThreeDAxes()
        cube = Cube(fill_opacity=0, stroke_width=1, stroke_color=WHITE)
        square = Square()
        cube.generate_target()
        cube.target.shift(3 * UL)
        self.play(DrawBorderThenFill(cube))
        self.play(Rotate(cube, 45*DEGREES*10,np.array([1.0, 0.0, 1.0]), run_time=5))
        self.play(Transform(cube, square))
        self.play(Rotate(square, 90*DEGREES,np.array([0,0,0])),FadeOut(cube))
        # self.play(FadeOut(cube))
        self.wait(2)
        # self.play(MoveToTarget(cube))
