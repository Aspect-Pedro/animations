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

class RotatingCube2(ThreeDScene):
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
        self.play(Rotate(cube, 45*DEGREES,np.array([1.0, 0.0, 1.0]), run_time=0.5))
        self.play(Transform(cube, square))
        self.play(Rotate(square, 90*DEGREES,np.array([0,0,0])),FadeOut(cube))
        # self.play(FadeOut(cube))
        self.wait(2)
        # self.play(MoveToTarget(cube))

class CameraAnimation(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=0*DEGREES, theta=90*DEGREES)

        square = Square(fill_opacity=0,stroke_color=WHITE)
        squareEdgeMidLeft = ValueTracker(square.get_edge_center(LEFT)[0])
        squareEdgeMidRight = ValueTracker(square.get_edge_center(RIGHT)[0])
    

        camera = Dot3D(color=WHITE).next_to(square,OUT * 4)

        grid = NumberPlane().set_opacity(0.3)

        lineR = always_redraw(lambda: Line3D(camera.get_center(),RIGHT * squareEdgeMidLeft.get_value(),color=YELLOW))
        lineL = always_redraw(lambda: Line3D(camera.get_center(),RIGHT * squareEdgeMidRight.get_value(),color=YELLOW))
        cameraText = always_redraw(lambda: Tex("camera area").next_to(square,UL).rotate(PI))

        self.play(Write(grid))
        self.play(Create(square))
        self.play(FadeIn(camera))
        self.play(FadeIn(lineL,lineR))
        self.play(Write(cameraText))

        phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers()

        self.play(phi.animate.set_value(45*DEGREES))
        self.play(theta.animate.set_value(90*DEGREES))       
        self.play(square.animate.scale(3),squareEdgeMidLeft.animate.set_value(-3),squareEdgeMidRight.animate.set_value(3),camera.animate.shift(OUT * 2),run_time=3)
        self.wait(1)


        # # # self.play(distance_to_origin.animate.set_value(2))
        # # # self.play(focal_distance.animate.set_value(25))

        self.wait(1)
                
        self.play(phi.animate.set_value(90*DEGREES))

        self.wait(2)
