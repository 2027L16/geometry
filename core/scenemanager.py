import manim


class SceneManager:
    """Coordinate queued animations and objects within a Manim scene."""

    scene: manim.Scene

    def __init__(self, scene: manim.Scene):
        self.scene = scene
        self.transitions: list[manim.Animation] = []
        self.objects: dict[str, manim.Mobject] = {}

    def add_object(self, name: str, obj: manim.Mobject, scene_add: bool = False) -> None:
        """Register a Manim object by name and optionally add it to the scene immediately."""

        self.objects[name] = obj
        if scene_add:
            self.scene.add(obj)

    def add_transition(self, name: str, obj: manim.Mobject) -> None:
        """Queue a transform animation that morphs the stored object into ``obj``."""

        if name in self.objects:
            transform = manim.Transform(self.objects[name], obj)
            self.transitions.append(transform)
            self.objects[name] = obj

    def add_move_to(self, name: str, x: float, y: float) -> None:
        """Queue a smooth translation of the stored object to ``(x, y, 0)``."""

        if name in self.objects:
            self.transitions.append(self.objects[name].animate.move_to((x, y, 0)))  # type: ignore[attr-defined]

    def play_transitions(self) -> None:
        """Play all queued transitions and clear the buffer."""

        if self.transitions:
            self.scene.play(*self.transitions)
            self.transitions = []