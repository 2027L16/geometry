# Dynamic Geometry Animator

Dynamic Geometry Animator is a lightweight toolkit built on top of [Manim](https://www.manim.community/) for creating interactive geometric constructions. It focuses on defining reusable geometric elements (points, lines, circles, and more) whose positions are updated dynamically as their dependencies move. The toolkit is designed for educational visuals, algorithm demonstrations, and exploratory geometry experiments.

> Looking for the original Chinese documentation? See [`README.zh-CN.md`](README.zh-CN.md).

## Features
- **Composable primitives** such as `Dot` and `BetweenDot` that propagate updates to dependent elements.
- **Scene orchestration helper** (`SceneManager`) that batches Manim animations to keep interactions smooth.
- **Manim-native objects** so the resulting scenes can be rendered with the Manim CLI without additional adapters.
- **Extensible element base class** that makes it straightforward to add new geometric constructions.

## Installation

Dynamic Geometry Animator uses [Poetry](https://python-poetry.org/) for dependency management.

```powershell
git clone https://github.com/2027L16/geometry.git
cd geometry
poetry install
```


## Quick Start

Render the included example scene to verify the setup:

```powershell
poetry run manim basic_scene.py TestScene -p
```

This command opens a preview window that shows:

1. Two points `A` and `B`.
2. A point `C` that stays on the segment `AB` while maintaining a configurable ratio.
3. Additional points created dynamically after moving `A`.

The animation demonstrates how dependent elements respond when their parents move via `Dot.move_to` or coordinate assignments.

## Package Overview

| Module | Description |
| --- | --- |
| `core/scenemanager.py` | Defines `SceneManager`, a thin wrapper around `manim.Scene` that accumulates and plays transition animations in batches. |
| `elements/base.py` | Provides the abstract `Element` base class with subscription mechanics for dependency updates. |
| `elements/dot.py` | Implements concrete point elements, including proportional points (`BetweenDot`). |
| `basic_scene.py` | Demonstrates how to assemble a scene using the provided components. |

Extend the toolkit by subclassing `Element` and implementing the `to_manim` and `update` hooks to describe how your element is rendered and refreshed.

## Development

- Run static analysis with Ruff before committing:

	```powershell
	poetry run ruff check .
	```

- Execute the automated tests:

- Execute the automated tests:

	```powershell
	poetry run pytest
	```

- Prefer fast, logic-focused tests under `tests/`. For rendering-heavy features consider isolating geometry calculations to keep the suite lightweight.

## Roadmap
- Add line and circle primitives with the same reactive update model.
- Provide higher-level construction presets (perpendicular bisectors, angle bisectors, circumcenters, etc.).
- Publish documentation with rendered GIFs of example scenes.

## Contributing
Issues and pull requests are welcome! Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) and follow the [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) before participating.

## License

Released under the [GNU GPL v3](LICENSE).
