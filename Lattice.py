from manim import *

class DotMap(Scene):
    def construct(self):
        for x in range(0, 8):
            for y in range(0, 5):
                self.play(Create(Dot(np.array([x - 4, y - 2, 0]), color=WHITE)), duration=0.1)

class Plane(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=0*DEGREES, theta=90*DEGREES)
        plane = NumberPlane().set_opacity(0.2)
        # axis = ThreeDAxes()
        self.play(Create(plane), run_time=2)
        self.wait(2)
        phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers()
        
        for x in range(-5, 6):
            for y in range(0, 7):
                self.play(Create(Dot(np.array([x, y - 3, 0])), color=WHITE), run_time=0.1)

        # Vector 1
        vector1 = Arrow(start=np.array([0, 0, 0]), end=np.array([1, 0, 0]), color=RED, buff=0)
        self.play(Create(vector1))

        # Vector 2
        vector2 = Arrow(start=np.array([0, 0, 0]), end=np.array([0, -1, 0]), color=BLUE, buff=0)
        self.play(Create(vector2))
        
        self.play(phi.animate.set_value(45*DEGREES))
        self.play(theta.animate.set_value(135*DEGREES))
        self.wait(2)
        
        # Vector 3
        vector3 = Arrow(start=np.array([0, 0, 0]), end=np.array([0, 0, 1]), color=GREEN, buff=0)
        self.play(Create(vector3))
        
        self.wait(1)
        
        for x in range(-5, 6):
            for y in range(0, 7):
                self.play(Create(Dot(np.array([x, y - 3, 1])), color=WHITE), run_time=0.01)
        
        self.play(phi.animate.set_value(-45*DEGREES))
        self.wait(2)
        
                

class Plane2(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=0*DEGREES, theta=90*DEGREES)
        plane = NumberPlane().set_opacity(0.2)
        # axis = ThreeDAxes()
        self.play(Create(plane), run_time=2)
        self.wait(2)
        phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers()
        
        self.play(Create(Dot(np.array([2, -2, 0])), color=RED), run_time=0.1)

        # Vector 1
        vector1 = Arrow(start=np.array([0, 0, 0]), end=np.array([1, 0, 0]), color=RED, buff=0)
        self.play(Create(vector1))

        # Vector 2
        # vector2 = Arrow(start=np.array([0, 0, 0]), end=np.array([0, -1, 0]), color=BLUE, buff=0)
        # self.play(Create(vector2))
        
        vector2 = Arrow(start=np.array([1, 0, 0]), end=np.array([2, 0, 0]), color=RED, buff=0)
        self.play(Create(vector2))

        vector3 = Arrow(start=np.array([2, 0, 0]), end=np.array([2, -1, 0]), color=BLUE, buff=0)
        self.play(Create(vector3))
        vector4 = Arrow(start=np.array([2, -1, 0]), end=np.array([2, -2, 0]), color=BLUE, buff=0)
        self.play(Create(vector4))
        
        self.play(phi.animate.set_value(45*DEGREES))
        self.play(theta.animate.set_value(135*DEGREES))
        self.wait(2)
        
                

class Plane3(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=0*DEGREES, theta=90*DEGREES)
        plane = NumberPlane().set_opacity(0.2)
        # axis = ThreeDAxes()
        self.play(Create(plane), run_time=2)
        self.wait(2)
        phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers()
        
        self.play(Create(Dot(np.array([2, -2, 0])), color=RED), run_time=0.1)

        # Vector 1
        offset = 0
        for x in range(0, 10):
            vector1 = Arrow(start=np.array([-x, offset, 0]), end=np.array([-1 - x, 0.3 + offset, 0]), color=RED, buff=0)
            self.play(Create(vector1), run_time=0.1)
            offset += 0.3
        
        
        offset = 3
        for y in range(10, -4, -1):
            vector2 = Arrow(start=np.array([-2 - y, -0.7 + offset, 0]), end=np.array([-1 - y,-1 + offset, 0]), color=BLUE, buff=0)
            self.play(Create(vector2), run_time=0.1)
            offset -= 0.3
            
        
        # vector1 = Arrow(start=np.array([0, 0, 0]), end=np.array([-1.5, 0.3, 0]), color=RED, buff=0)
        # self.play(Create(vector1))
        
        # vector2 = Arrow(start=np.array([0, 0, 0]), end=np.array([-2, 0.5, 0]), color=BLUE, buff=0)
        # self.play(Create(vector2))
        
        
        self.wait(2)
        
                