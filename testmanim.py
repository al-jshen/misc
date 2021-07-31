from manim import *


def test():
    scene = Render()
    scene.render()


class Render(Scene):
    def construct(self):
        text = Text("test")
        self.play(Write(text))


if __name__ == "__main__":
    test()
