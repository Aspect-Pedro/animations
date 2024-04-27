from manim import *

class Grid(Scene):
    def construct(self):
        grid = self.generate_grid(21, 21)
        self.play(Write(grid), run_time=5)
        self.wait()

    def generate_grid(self, rows, cols, grid_spacing=0.3):
        grid = VGroup()
        for i in range(rows):
            for j in range(cols):
                square = Square(side_length=grid_spacing, fill_opacity=0, stroke_width=1).shift((RIGHT * j * grid_spacing + UP * i * grid_spacing)- (RIGHT * cols * grid_spacing / 2) - (UP * rows * grid_spacing / 2))
                grid.add(square)
        return grid

class Grid2(Scene):
    def construct(self):
        grid = self.generate_grid(4, 2)
        self.play(Write(grid), run_time=5)
        self.wait()

    def generate_grid(self, rows, cols, grid_spacing=0.3):
        grid = VGroup()
        for i in range(rows):
            for j in range(cols):
                square = Square(side_length=grid_spacing, fill_opacity=0, stroke_width=1).shift((RIGHT * j * grid_spacing + UP * i * grid_spacing)- (RIGHT * cols * grid_spacing / 2) - (UP * rows * grid_spacing / 2))
                grid.add(square)
        return grid

class Grid3(Scene):
    def construct(self):
        grid = self.generate_grid(8, 2)
        self.play(Write(grid), run_time=5)
        self.wait()

    def generate_grid(self, rows, cols, grid_spacing=0.3):
        grid = VGroup()
        for i in range(rows):
            for j in range(cols):
                square = Square(side_length=grid_spacing, fill_opacity=0, stroke_width=1).shift((RIGHT * j * grid_spacing + UP * i * grid_spacing)- (RIGHT * cols * grid_spacing / 2) - (UP * rows * grid_spacing / 2))
                grid.add(square)
        return grid

class EighthyToP(Scene):
    def construct(self):
        text = Text("80", font="Advanced Pixel-7").scale(2)
        self.play(Write(text))
        self.wait(1)
        self.play(Transform(text, Text("P", font="Advanced Pixel-7").scale(2)), run_time=3)
        self.wait(1)


# Render the scene
if __name__ == "__main__":
    config.pixel_height = 1080
    config.pixel_width = 1920
    config.frame_height = 6.0
    config.frame_width = 10.67
    config.frame_y_radius = 3.0
    config.frame_x_radius = 5.33
    config.frame_rate = 30
    config.save_last_frame = False
    config.quality = "high"
    config.renderer = "opengl"
    config.input_file = ""
    config.output_file = ""
    config.slow_factor = 1
    config.save_pngs = False
    config.save_as_gif = False
    config.media_dir = "./media"
    config.tex_dir = "./tex"
    config.verbosity = "ERROR"
    scene = Grid()
    scene.render()