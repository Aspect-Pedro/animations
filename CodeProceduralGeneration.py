from manim import *

    # SetConfigFlags(FLAG_VSYNC_HINT | FLAG_MSAA_4X_HINT | FLAG_WINDOW_RESIZABLE);


class CodeFromString(Scene):
    def construct(self):
        code = '''
typedef struct axis {
    int x;
    int y;
} Vector2;
        
typedef struct room {
    Vector2 position;
    int width; int height;
    Vector2 center;
} Room;
'''

        code2 = '''
newRoom.center = { 
    newRoom.position.x + (newRoom.width / 2),
    newRoom.position.y + (newRoom.height / 2) };
}
'''

        rendered_code = Code(code=code, tab_width=4,background_stroke_color=BLACK, 
        insert_line_no=False,
        style="monokai",
        language="cpp", 
        font="Fira Code")
        
        rendered_code2 = Code(code=code2, tab_width=4,background_stroke_color=BLACK, 
        insert_line_no=False,
        style="monokai",
        language="cpp", 
        font="Fira Code").to_edge(DOWN, buff=1)
        
        self.play(Write(rendered_code), run_time=3)
        self.play(rendered_code.animate.shift(UP))
        self.play(Write(rendered_code2), run_time=3)
        self.wait(2)


class CodeVsync(Scene):
    def construct(self):
        code = '''
SetConfigFlags(FLAG_VSYNC_HINT | FLAG_MSAA_4X_HINT | FLAG_WINDOW_RESIZABLE);
'''

        rendered_code = Code(code=code, tab_width=4,background_stroke_color=BLACK, 
        insert_line_no=False,
        style="monokai",
        language="python", 
        font="Fira Code").scale(0.7)
                
        self.play(Write(rendered_code), run_time=3)
        self.wait(2)