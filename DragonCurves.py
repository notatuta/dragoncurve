#
# manim -pqh --disable_caching DragonCurves.py DragonCurves
#
from manim import *
import numpy as np

class DragonCurves(MovingCameraScene):
    def construct(self):
        self.add_sound("vibevoice_realtime_audio2.wav", time_offset=0) # in-Samuel_man
        self.camera.frame.save_state()
        caption = Text("Regular Dragon Curve").to_edge(UP)

        rotation_angle = -PI/2
        vertex0 = Dot(color=WHITE, fill_opacity=0.5)
        vertex1 = vertex0.copy()
        vertex1.shift(RIGHT)
        vertex1.shift(UP * 0.5)
        vertices = VGroup()
        vertices.add(vertex0)
        vertices.add(vertex1)

        karaoke = VGroup()
        karaoke.add(Text("Make a copy,", font_size=32))
        karaoke.add(Text("rotate it by 90°,", font_size=32))
        karaoke.add(Text("append,", font_size=32))
        karaoke.add(Text("repeat", font_size=32))
        karaoke.arrange(RIGHT, buff=0.2).to_edge(DOWN)

        lines = VGroup()
        lines.add(Line(vertex0.get_center(), vertex1.get_center(), color=WHITE).set_opacity(0.5))
        self.play(Write(caption), FadeIn(vertex0), FadeIn(vertex1), FadeIn(lines))
        self.add(karaoke)

        invisible_head = Dot(vertex0.get_center())
        invisible_head.set_opacity(0)
        invisible_tail = Dot(vertex1.get_center())
        invisible_tail.set_opacity(0)
        invisible_dots = VGroup()
        invisible_dots.add(invisible_head)
        invisible_dots.add(invisible_tail)

        pivot = Circle(color=RED, radius=0.2)
        pivot.move_to(vertex1.get_center())
        self.play(Create(pivot))
        reps_before_zoom = 3
        for i in range(0, 11):
            if (i <= reps_before_zoom):
                karaoke[0].set_color(YELLOW)
                karaoke[1].set_color(WHITE)
                karaoke[2].set_color(WHITE)

            new_vertices = VGroup()
            new_dots = VGroup()
            new_lines = VGroup()
            last_index = len(vertices) - 1

            for j in range(last_index - 1, -1, -1):
                new_vertices.add(vertices[j].copy())
                new_dot = invisible_dots[j].copy()
                new_dot.rotate(angle=rotation_angle, about_point=vertices[last_index].get_center())
                new_dots.add(new_dot)
                new_lines.add(Line(invisible_dots[j].get_center(), 
                                   invisible_dots[j + 1].get_center(), color=WHITE).set_opacity(0.5))
            if (i <= reps_before_zoom):
                self.play(FadeIn(new_vertices), FadeIn(new_lines))
            else:
                self.add(new_vertices, new_lines)
            for k in range(0,len(new_vertices)):
                vertices.add(new_vertices[k])
                invisible_dots.add(new_dots[k])
                lines.add(new_lines[k])
            if (i < reps_before_zoom):
                karaoke[0].set_color(WHITE)
                karaoke[1].set_color(YELLOW)
                self.play(
                    Rotate(
                        new_vertices + new_lines,
                        angle=rotation_angle,
                        about_point=vertices[last_index].get_center(),
                        rate_func=smooth
                    )
                )
                karaoke[1].set_color(WHITE)
                karaoke[2].set_color(YELLOW)
            elif (i == reps_before_zoom):
                karaoke[0].set_color(WHITE)
                karaoke[1].set_color(YELLOW)
                self.play(
                    Rotate(
                        new_vertices + new_lines,
                        angle=rotation_angle,
                        about_point=vertices[last_index].get_center(),
                        rate_func=smooth
                    ),
                    self.camera.auto_zoom(invisible_dots, margin=2, animate=True),
                    FadeOut(karaoke),
                    FadeOut(caption),
                    FadeOut(pivot)
                )
            else:
                self.play(
                    Rotate(
                        new_vertices + new_lines,
                        angle=rotation_angle,
                        about_point=vertices[last_index].get_center(),
                        rate_func=linear
                    ),
                    self.camera.auto_zoom(invisible_dots, margin=2, animate=True),
                )
            if (i < reps_before_zoom):
                self.play(pivot.animate.move_to(vertices[len(vertices) - 1].get_center()))
        lines.set_opacity(1)
        vertices.set_opacity(1)
        self.wait(2)
        self.clear()
        self.camera.frame.restore()

#############################################################

        caption = Text("Hex Dragon Curve").to_edge(UP)

        karaoke = VGroup()
        karaoke.add(Text("Make a copy,", font_size=32))
        karaoke.add(Text("rotate it by 120°,", font_size=32))
        karaoke.add(Text("append,", font_size=32))
        karaoke.add(Text("repeat", font_size=32))
        karaoke.arrange(RIGHT, buff=0.2).to_edge(DOWN)
 
        rotation_angle = -2*PI/3
        hex0 = RegularPolygon(n=6, radius=0.5)
        hex0.set_fill(YELLOW, opacity=0.5)
        hex0.set_stroke(WHITE, width=2)
        hex1 = hex0.copy()
        hex1.shift(DOWN)
        self.play(Write(caption),DrawBorderThenFill(hex0),DrawBorderThenFill(hex1))
        self.add(karaoke)

        hexes = VGroup()
        hexes.add(hex0)
        hexes.add(hex1)

        invisible_head = Dot(hex0.get_center())
        invisible_head.set_opacity(0)
        invisible_tail = Dot(hex1.get_center())
        invisible_tail.set_opacity(0)
        invisible_dots = VGroup()
        invisible_dots.add(invisible_head)
        invisible_dots.add(invisible_tail)

        pivot = Circle(color=RED, radius=0.2, fill_opacity=1)
        pivot.move_to(hex1.get_center())
        self.play(Create(pivot))
        reps_before_zoom = 3
        for i in range(0, 9):
            if (i <= reps_before_zoom):
                karaoke[0].set_color(YELLOW)
                karaoke[1].set_color(WHITE)
                karaoke[2].set_color(WHITE)
                
            new_hexes = VGroup()
            new_dots = VGroup()
            last_index = len(hexes) - 1

            for j in range(last_index - 1, -1, -1):
                new_hexes.add(hexes[j].copy())
                new_dot = invisible_dots[j].copy()
                new_dot.rotate(angle=rotation_angle, about_point=hexes[last_index].get_center())
                new_dots.add(new_dot)
            if (i <= reps_before_zoom):
                self.play(DrawBorderThenFill(new_hexes))
            else:
                self.add(new_hexes)
            for k in range(0,len(new_hexes)):
                hexes.add(new_hexes[k])
                invisible_dots.add(new_dots[k])

            if (i < reps_before_zoom):
                karaoke[0].set_color(WHITE)
                karaoke[1].set_color(YELLOW)
                self.play(
                    Rotate(
                        new_hexes,
                        angle=rotation_angle,
                        about_point=hexes[last_index].get_center(),
                        rate_func=smooth
                    )
                )
                karaoke[1].set_color(WHITE)
                karaoke[2].set_color(YELLOW)
            elif (i == reps_before_zoom):
                karaoke[0].set_color(WHITE)
                karaoke[1].set_color(YELLOW)
                self.play(
                    Rotate(
                        new_hexes,
                        angle=rotation_angle,
                        about_point=hexes[last_index].get_center(),
                        rate_func=smooth
                    ),
                    self.camera.auto_zoom(invisible_dots, margin=1, animate=True),
                    FadeOut(karaoke),
                    FadeOut(caption),
                    FadeOut(pivot)
                )
            else:
                self.play(
                    Rotate(
                        new_hexes,
                        angle=rotation_angle,
                        about_point=hexes[last_index].get_center(),
                        rate_func=linear
                    ),
                    self.camera.auto_zoom(invisible_dots, margin=1, animate=True)
                )
            if (i < reps_before_zoom):
                self.bring_to_front(pivot)
                self.play(pivot.animate.move_to(hexes[len(hexes) - 1].get_center()))
        hexes.set_opacity(1)
        self.wait(2)
