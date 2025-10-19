# 动态几何动画器

基于 [Manim](https://www.manim.community/) 的轻量级几何作图工具，用于演示几何元素的动态构造与联动。通过点、线、圆等基础元素的组合，可以创建教育可视化、算法演示以及探索性几何实验。

## 特性
- **可组合的几何元素**：提供 `Dot`、`BetweenDot` 等基础元素，并支持依赖更新的传播。
- **场景管理器**：`SceneManager` 封装了 `manim.Scene`，用于批量播放动画，保持交互顺畅。
- **原生 Manim 对象**：所有元素都直接对应 Manim 对象，无需额外适配即可用 Manim CLI 渲染。
- **易于扩展的基类**：通过继承 `Element` 并实现 `to_manim`、`update` 方法即可新增自定义几何构造。

## 安装
本项目使用 [Poetry](https://python-poetry.org/) 管理依赖：

```powershell
git clone https://github.com/2027L16/geometry.git
cd geometry
poetry install
```


## 快速上手

使用内置示例场景验证环境：

```powershell
poetry run manim basic_scene.py TestScene -p
```

运行后会打开预览窗口，展示以下内容：

1. 初始的两个点 `A` 和 `B`；
2. 依赖于 `A`、`B` 的点 `C`，保持给定比例位于线段 `AB` 上；
3. 移动 `A` 点后新增的点以及更新后的动画效果。

该示例展示了 `Dot.move_to` 与坐标赋值如何触发依赖元素的同步更新。

## 模块概览

| 模块 | 说明 |
| --- | --- |
| `core/scenemanager.py` | `SceneManager`：Manim 场景的轻量封装，负责收集并批量播放动画。 |
| `elements/base.py` | `Element` 抽象基类，实现订阅机制以支持依赖更新。 |
| `elements/dot.py` | 点元素的具体实现，包括比例点 `BetweenDot`。 |
| `basic_scene.py` | 示例场景，演示如何组合各个组件。 |

通过继承 `Element` 并实现 `to_manim` 与 `update`，即可扩展新的几何构造。

## 开发
- 提交前请运行 Ruff 进行静态检查：

	```powershell
	poetry run ruff check .
	```

- 运行自动化测试：

	```powershell
	poetry run pytest
	```

- 在 `tests/` 目录中编写新的快速测试；如需渲染，请尽量拆分纯几何逻辑以保持测试速度。

## 规划
- 增加线段、圆等更多几何元素，并保持同样的响应式更新模型。
- 提供常见的辅助构造（如垂直平分线、角平分线、外接圆心等）。
- 发布带有示例动图的文档页面。

## 贡献
欢迎提交 Issue 与 Pull Request！开始之前请阅读 [`CONTRIBUTING.md`](CONTRIBUTING.md) 并遵守 [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md)。

## 许可协议

本项目以 [GNU GPL v3](LICENSE) 授权发布。
