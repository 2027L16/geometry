"""Unit tests for dynamic geometry elements with stubbed Manim objects."""

from __future__ import annotations

from typing import Any, cast

import manim
import pytest

from core import SceneManager
from elements import BetweenDot, Dot


class _StubAnimation:
    def __init__(self, coords: tuple[float, float, float]) -> None:
        self.coords = coords


class _StubAnimator:
    def __init__(self, dot: "_StubDot") -> None:
        self._dot = dot

    def move_to(self, coords: tuple[float, float, float]) -> _StubAnimation:
        self._dot.coords = coords
        return _StubAnimation(coords)


class _StubDot:
    def __init__(self, coords: tuple[float, float, float]) -> None:
        self.coords = coords

    @property
    def animate(self) -> _StubAnimator:
        return _StubAnimator(self)

    def move_to(self, coords: tuple[float, float, float]) -> "_StubDot":
        self.coords = coords
        return self


class _DummyScene:
    def __init__(self) -> None:
        self.added: list[Any] = []
        self.play_calls: list[tuple[Any, ...]] = []

    def add(self, obj: Any) -> None:
        self.added.append(obj)

    def play(self, *animations: Any) -> None:
        self.play_calls.append(animations)


@pytest.fixture(autouse=True)
def _stub_manim(monkeypatch: pytest.MonkeyPatch) -> None:
    """Replace Manim objects with light-weight stand-ins so tests stay fast."""

    from elements import dot as dot_module

    monkeypatch.setattr(dot_module.manim, "Dot", _StubDot, raising=False)


def test_between_dot_initialises_at_ratio() -> None:
    scene = _DummyScene()
    manager = SceneManager(cast(manim.Scene, scene))

    dot_a = Dot("A", 0.0, 0.0, manager)
    dot_b = Dot("B", 3.0, 3.0, manager)
    between = BetweenDot("C", dot_a, dot_b, 2.0, manager)

    expected_x = (dot_a.x + 2.0 * dot_b.x) / 3.0
    expected_y = (dot_a.y + 2.0 * dot_b.y) / 3.0

    assert between.x == pytest.approx(expected_x, rel=1e-9)
    assert between.y == pytest.approx(expected_y, rel=1e-9)
    assert scene.added  # Dot objects should be added to the scene


def test_between_dot_updates_when_parent_moves() -> None:
    scene = _DummyScene()
    manager = SceneManager(cast(manim.Scene, scene))

    dot_a = Dot("A", -2.0, 1.0, manager)
    dot_b = Dot("B", 4.0, -1.0, manager)
    between = BetweenDot("C", dot_a, dot_b, 1.0, manager)

    dot_a.move_to(2.0, 3.0)

    expected_x = (dot_a.x + dot_b.x) / 2.0
    expected_y = (dot_a.y + dot_b.y) / 2.0

    assert between.x == pytest.approx(expected_x, rel=1e-9)
    assert between.y == pytest.approx(expected_y, rel=1e-9)
    assert len(scene.play_calls) == 1