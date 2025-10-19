from __future__ import annotations

from abc import ABC, abstractmethod

import manim

from core import SceneManager


class Element(ABC):
    """Base class for reactive geometric elements."""

    _subscribers: list[Element]
    scenemanager: SceneManager
    obj: manim.VMobject
    name: str

    @abstractmethod
    def to_manim(self) -> manim.VMobject:
        """Produce a Manim object that represents the element."""

    @abstractmethod
    def __init__(self, name: str, scenemanager: SceneManager):
        self._subscribers = []
        self.scenemanager = scenemanager
        self.name = name

    def subscribe(self, subscriber: Element) -> None:
        """Register a dependent element that should receive updates."""

        self._subscribers.append(subscriber)

    def _notify_subscribers(self) -> None:
        """Invoke ``update`` on all registered dependents."""

        for sub in self._subscribers:
            sub.update()

    @abstractmethod
    def update(self) -> None:
        """Refresh the element's internal state and animations."""

        pass