from manim import *
from manim.utils.color import rgb_to_color

import numpy as np
from typing import Iterable, Tuple, Union, List
from scipy.ndimage.interpolation import zoom


def arr_to_dots(arr: Iterable, color: Union[str, List], opacity: float) -> VGroup:

    dots = [Dot(i) for i in arr]
    if isinstance(color, str):
        dots = [i.set_fill(color, opacity=opacity) for i in dots]
    else:
        assert len(dots) == len(color)
        dots = [i.set_fill(j, opacity=opacity) for i, j in zip(dots, color)]

    group = VGroup(*dots)

    return group


def gen_rand_dots(n: int, color: Union[str, List], opacity: float = 1) -> VGroup:
    rand = np.random.multivariate_normal(np.zeros(2), np.eye(2), size=n)
    rand = np.hstack((rand, np.zeros((n, 1))))

    return arr_to_dots(rand, color, opacity)


def rand_color_grid(gridsize: Tuple[int, int]) -> np.ndarray:
    colors = (np.random.rand(2, 2, 3)).astype(float)
    return zoom(colors, (gridsize[0] / 2, gridsize[1] / 2, 1), order=1)


def rand_color_arr(n: int) -> Iterable:
    colors = (np.random.rand(3, 3)).astype(float)
    colors = zoom(colors, (n / 3, 1), order=1)
    c = []
    for i in colors:
        c.append(rgb_to_color(i))

    return c


def gen_grid(
    xrange: Tuple[float, float], yrange: Tuple[float, float], xn: int, yn: int
) -> VGroup:
    x = np.linspace(*xrange, num=xn)
    y = np.linspace(*yrange, num=yn)

    colorgrid = rand_color_grid((xn, yn))

    dots = []
    colors = []

    # go top left to bottom right
    for j, jv in enumerate(y[::-1]):
        for i, iv in enumerate(x):
            color = rgb_to_color(colorgrid[i, j, :])
            dots.append(Dot((iv, jv, 0)).set_fill(color))
            colors.append(color)

    return VGroup(*dots), colors


class Start(Scene):
    def construct(self):

        n = 100

        (grid, colors) = gen_grid((-2, 2), (-2, 2), 10, 10)

        group1 = gen_rand_dots(n, colors)
        group2 = gen_rand_dots(n, colors)
        group3 = gen_rand_dots(n, colors)

        text1 = Text("Here are some transformations.")
        text2 = Text("A grid of points").to_corner(UL)
        text3 = Text("First random transformation").to_corner(UL)
        text4 = Text("Second random transformation").to_corner(UL)
        text5 = Text("Third random transformation").to_corner(UL)

        self.play(Write(text1))
        self.wait()
        self.play(
            ReplacementTransform(text1, text2), LaggedStart(Create(grid), run_time=3)
        )
        self.wait()
        self.play(
            ReplacementTransform(grid, group1), ReplacementTransform(text2, text3)
        )
        self.wait()
        self.play(
            ReplacementTransform(group1, group2), ReplacementTransform(text3, text4)
        )
        self.wait()
        self.play(
            ReplacementTransform(group2, group3), ReplacementTransform(text4, text5)
        )
        self.wait()
        self.play(Uncreate(group3), Unwrite(text5))
        self.wait()
