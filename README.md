# 🐍 Snake 贪吃蛇

![Python](https://img.shields.io/badge/Python-3.12-blue)
![pygame](https://img.shields.io/badge/pygame-2.6-informational)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Made with pygame](https://img.shields.io/badge/Made%20with-pygame-ff69b4)

一个用 Python + pygame 写的贪吃蛇小游戏。**零图片素材**，画面全是用彩色方块画出来的 —— 特别适合用来学 pygame 入门。

## 玩法

- **方向键** 控制蛇的移动
- 吃到红色方块 **+1 分**，同时身体变长
- 撞到墙或撞到自己 → 游戏结束
- 结束后按 **R** 重新开始；按 **ESC** 退出

## 运行

需要 Python 3 和 pygame：

```bash
pip install pygame
python snake.py
```

## 技术要点

- 25×25 的格子坐标系，蛇用一张坐标列表表示
- 主循环三件事：处理输入 → 移动蛇 → 画画面
- 吃到食物身体变长，没吃到则保持等长
- 用 `pygame.draw.rect` 画彩色方块当"UI"，完全不需要素材

## 文件

- `snake.py` —— 游戏主程序

## 许可

MIT License
