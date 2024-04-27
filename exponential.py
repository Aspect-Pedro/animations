from manim import *

class ExponentialFunctionGraph(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 8, 1],
            y_range=[0, 50, 2],
            tips= False,
            axis_config={"color": WHITE},
        )

        exp_graph = axes.plot(lambda x: np.exp(x) - 1, color=GREEN)

        # Labels
        axes_labels = axes.get_axis_labels(x_label="Tempo", y_label="Desenvolvimento")

        # Animation
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(exp_graph), run_time=2)
        
        # Change graph color
        self.play(exp_graph.animate.set_color(RED))
        self.wait(2)

