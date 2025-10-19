"""Example Manim scene demonstrating dynamic geometry elements."""

import manim

from core import SceneManager
from elements import BetweenDot, Dot


class TestScene(manim.Scene):
    """Showcase how dependent points respond to updates."""

    scenemanager: SceneManager

    def construct(self) -> None:
        number_plane = manim.NumberPlane()
        self.add(number_plane)

        self.scenemanager = SceneManager(self)

        dot1 = Dot("A", -2, 1, self.scenemanager)
        dot2 = Dot("B", 1, -3, self.scenemanager)
        BetweenDot("C", dot1, dot2, 1, self.scenemanager)

        self.wait(2)

        dot1.x = 3
        self.wait(2)

        dot1.y = -2
        self.wait(2)

        dot3 = Dot("D", -1, 0, self.scenemanager)
        BetweenDot("E", dot1, dot3, 2, self.scenemanager)

        self.wait(2)
        dot1.move_to(1, 3)
        self.wait(2)
