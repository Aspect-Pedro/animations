from manim import *

svgPath = "C:\\Users\Pedro\Desktop\manimAnimations\images"


class FPS(Scene):
    def construct(self):
        fps_tracker = ValueTracker(60)  # Initial value set to 60 fps
        arrow = always_redraw(lambda: Arrow(ORIGIN, UP,color= GREEN if fps_tracker.get_value() > 30 else YELLOW if fps_tracker.get_value() == 30 else RED  ).rotate((fps_tracker.get_value() * TAU / 120) - (TAU / 2)).scale(1.5).move_to(LEFT * 3))
        num = always_redraw(lambda: DecimalNumber().set_value(fps_tracker.get_value()).next_to(arrow, RIGHT, buff=0.25).set_color(GREEN if fps_tracker.get_value() > 30 else YELLOW if fps_tracker.get_value() == 30 else RED))
        fps_text = always_redraw(lambda: Text(" FPS",font="Fira Code", font_size=30).next_to(num, RIGHT, buff=0.25).set_color(GREEN if fps_tracker.get_value() > 30 else YELLOW if fps_tracker.get_value() == 30 else RED))
        
        arrow2 = always_redraw(lambda: Arrow(ORIGIN, UP,color= GREEN if fps_tracker.get_value() > 30 else YELLOW if fps_tracker.get_value() == 30 else YELLOW if fps_tracker.get_value() == 30 else RED ).rotate((fps_tracker.get_value() * TAU / 120)).scale(1.5).move_to(RIGHT))

        lag_text = always_redraw(lambda: Text(" Travamentos (LAG)",font="Fira Code", font_size=30).next_to(arrow2, RIGHT, buff=0.25).set_color(GREEN if fps_tracker.get_value() > 30 else YELLOW if fps_tracker.get_value() == 30 else RED))
        


        # Animation to change FPS values
        self.play(FadeIn(num, fps_text,arrow, arrow2,lag_text), run_time=2)
        self.play(fps_tracker.animate.set_value(0), run_time=2)
        self.wait(1)

        self.play(fps_tracker.animate.set_value(60), run_time=2)
        self.wait(1)

        self.play(fps_tracker.animate.set_value(30), run_time=2)
        self.wait(1)

        # You can continue adding more FPS values and animations as needed

        # Stop the arrow updater
        arrow.clear_updaters()

class TimePerFrame(Scene):
    def construct(self):
        frame1 = Square(color=WHITE, fill_opacity=.8).move_to(LEFT * 5)
        text_frame1 = Text("Frame 1", font="Fira Code", font_size=15).next_to(frame1, DOWN, buff=0.25).set_color(WHITE)

        frame2 = Square(color=WHITE, fill_opacity=.8).move_to(LEFT * 2)
        text_frame2 = Text("Frame 2", font="Fira Code", font_size=15).next_to(frame2, DOWN, buff=0.25).set_color(WHITE)

        frame3 = Square(color=WHITE, fill_opacity=.8).move_to(RIGHT * 1)
        text_frame3 = Text("Frame 3", font="Fira Code", font_size=15).next_to(frame3, DOWN, buff=0.25).set_color(WHITE)

        frame4 = Square(color=WHITE, fill_opacity=.8).move_to(RIGHT * 4)
        text_frame4 = Text("Frame 4", font="Fira Code", font_size=15).next_to(frame4, DOWN, buff=0.25).set_color(WHITE)
        
        brace = Brace(frame1, DOWN).scale(0.4).shift(RIGHT * 1.5).set_color(WHITE)
        brace2 = Brace(frame2, DOWN).scale(0.4).shift(RIGHT * 1.5).set_color(WHITE)
        brace3 = Brace(frame3, DOWN).scale(0.4).shift(RIGHT * 1.5).set_color(WHITE)
        
        timePerFrame = Text("Tempo por frame", font="Fira Code", font_size=24).shift(DOWN * 3).set_color(WHITE)
        
        arrow1fromBraceToTime = Arrow(brace2.get_center(), timePerFrame.get_center(), color=WHITE, buff=0.5)
        

        self.play(Create(VGroup(frame1, frame2, frame3, frame4)))
        self.play(Write(VGroup(text_frame1, text_frame2, text_frame3, text_frame4)))
        self.play(GrowFromCenter(brace))
        self.play(GrowFromCenter(brace2))
        self.play(GrowFromCenter(brace3))
        self.play(Write(timePerFrame))
        self.play(GrowArrow(arrow1fromBraceToTime))

        self.wait(1)
        self.play(FadeOut(frame1, frame2, frame3, frame4, brace, brace2, brace3, text_frame1, text_frame2, text_frame3, text_frame4, arrow1fromBraceToTime, timePerFrame))



class GPUMonitor(Scene):
    def construct(self):
        fps_tracker_gpu = ValueTracker(90)  # Initial value set to 60 fps
        fps_tracker_monitor = ValueTracker(60)  # Initial value set to 60 fps

        svgIcon = SVGMobject(f"{svgPath}/gpu-icon.svg").scale(0.5).move_to(LEFT * 2).set_color(WHITE)
        svgIcon2 = SVGMobject(f"{svgPath}/screen-icon.svg").scale(0.5).move_to(RIGHT * 2).set_color(WHITE)


        self.play(DrawBorderThenFill(VGroup(svgIcon, svgIcon2)), run_time=2)

        fps_text_gpu = always_redraw(lambda: Text(" FPS",font="Fira Code", font_size=30).next_to(svgIcon, LEFT, buff=0.25))
        numGPU = always_redraw(lambda: DecimalNumber().set_value(fps_tracker_gpu.get_value()).next_to(fps_text_gpu, LEFT, buff=0.25))
        

        
        
        numMonitor = always_redraw(lambda: DecimalNumber().set_value(fps_tracker_monitor.get_value()).next_to(svgIcon2, RIGHT, buff=0.25))
        fps_text_monitor = always_redraw(lambda: Text(" FPS",font="Fira Code", font_size=30).next_to(numMonitor, RIGHT, buff=0.25))        


        # Animation to change FPS values
        self.play(Write(VGroup(numGPU, fps_text_gpu, numMonitor, fps_text_monitor)), run_time=2)

        vsyncOff = Text("V-Sync OFF", font="Fira Code", font_size=30).set_color(RED).shift(UP * 2)

        self.play(Write(vsyncOff), run_time=2)

        self.wait(2)
        
        vsyncOn = Text("V-Sync ON", font="Fira Code", font_size=30).set_color(GREEN).shift(UP * 2)

        self.play(Transform(vsyncOff, vsyncOn), run_time=2)

        self.play(fps_tracker_gpu.animate.set_value(60), run_time=2)

        self.wait(2)
