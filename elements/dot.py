from __future__ import annotations

import manim

from core import SceneManager
from elements.base import Element


class Dot(Element):
    """A point element that can notify dependents when it moves."""

    _x: float
    _y: float

    def __init__(self, name: str, x: float, y: float, scene_manager: SceneManager):
        self._x = x
        self._y = y
        super().__init__(name, scene_manager)
        self.scenemanager.add_object(name, self.to_manim(), True)

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value: float) -> None:
        self.move_to(value, self._y)

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value: float) -> None:
        self.move_to(self._x, value)

    def to_manim(self) -> manim.VMobject:
        self.obj = manim.Dot((self.x, self.y, 0))
        return self.obj

    def update(self) -> None:
        self.scenemanager.add_move_to(self.name, self.x, self.y)

    def move_to(self, newx: float, newy: float) -> None:
        """Update coordinates, propagate the change, and play queued animations."""

        self._x = newx
        self._y = newy
        self.update()
        self._notify_subscribers()
        self.scenemanager.play_transitions()


class BetweenDot(Dot):
    """A point that keeps a distance ratio between two parent points."""

    dot1: Dot
    dot2: Dot
    lamb: float

    def __init__(self, name: str, dot1: Dot, dot2: Dot, lamb: float, scene_manager: SceneManager):
        self.dot1 = dot1
        self.dot2 = dot2
        self.lamb = lamb
        self.dot1.subscribe(self)
        self.dot2.subscribe(self)
        super().__init__(
            name,
            (self.dot1.x + self.lamb * self.dot2.x) / (1 + self.lamb),
            (self.dot1.y + self.lamb * self.dot2.y) / (1 + self.lamb),
            scene_manager,
        )

    def update(self) -> None:
        self._x, self._y = (
            (self.dot1.x + self.lamb * self.dot2.x) / (1 + self.lamb),
            (self.dot1.y + self.lamb * self.dot2.y) / (1 + self.lamb),
        )
        self.scenemanager.add_move_to(self.name, self.x, self.y)