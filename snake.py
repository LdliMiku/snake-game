# -*- coding: utf-8 -*-
"""贪吃蛇 Snake —— 用 pygame 画彩色方块做的小游戏，零素材，只有代码。"""

import sys
import random
import pygame

# ---------- 1. 基础设置 ----------
CELL = 20                  # 每个格子的边长（像素）
GRID_W, GRID_H = 25, 25    # 横向、纵向各多少个格子
WIDTH, HEIGHT = CELL * GRID_W, CELL * GRID_H   # 窗口尺寸
FPS = 10                   # 速度：每秒蛇移动几格子

# 颜色（R, G, B）
BLACK  = (18, 18, 18)      # 背景
GREEN  = (0, 200, 83)      # 蛇
RED    = (231, 76, 60)     # 食物
WHITE  = (240, 240, 240)   # 文字


def random_food(snake):
    """在空白格子里随机生成一个食物的坐标 (x, y)"""
    while True:
        x = random.randint(0, GRID_W - 1)
        y = random.randint(0, GRID_H - 1)
        if (x, y) not in snake:      # 食物不能长在蛇身上
            return (x, y)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake 贪吃蛇")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("consolas", 24)
    big_font = pygame.font.SysFont("consolas", 44)

    def reset():
        """开始或重开一局，返回 (蛇身, 方向, 得分, 食物)"""
        snake = [(GRID_W // 2, GRID_H // 2 + 1),
                 (GRID_W // 2, GRID_H // 2),
                 (GRID_W // 2, GRID_H // 2 - 1)]   # 3 段身体，竖着摆
        direction = (1, 0)                          # 初始向右
        score = 0
        food = random_food(snake)
        return snake, direction, score, food

    snake, direction, score, food = reset()

    running = True
    game_over = False

    # ---------- 2. 游戏主循环 ----------
    while running:
        # 2.1 处理事件（键盘按键）
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if game_over:
                    if event.key == pygame.K_r:      # 结束后按 R 重开
                        snake, direction, score, food = reset()
                        game_over = False
                else:
                    # 方向键控制；禁止 180 度掉头
                    if event.key == pygame.K_UP and direction != (0, 1):
                        direction = (0, -1)
                    elif event.key == pygame.K_DOWN and direction != (0, -1):
                        direction = (0, 1)
                    elif event.key == pygame.K_LEFT and direction != (1, 0):
                        direction = (-1, 0)
                    elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                        direction = (1, 0)

        # 2.2 移动蛇（没结束才动）
        if not game_over:
            head_x, head_y = snake[0]
            new_head = (head_x + direction[0], head_y + direction[1])

            # 撞墙 or 撞到自己 → 游戏结束
            hit_wall = (new_head[0] < 0 or new_head[0] >= GRID_W or
                        new_head[1] < 0 or new_head[1] >= GRID_H)
            hit_self = new_head in snake
            if hit_wall or hit_self:
                game_over = True
            else:
                snake.insert(0, new_head)          # 头前进一格，插到最前
                if new_head == food:
                    score += 1                     # 吃到食物：加分且身体变长
                    food = random_food(snake)
                else:
                    snake.pop()                    # 没吃到：尾巴去掉，等长

        # ---------- 3. 画画面 ----------
        screen.fill(BLACK)
        for seg in snake:                          # 画蛇（绿色方块）
            pygame.draw.rect(screen, GREEN,
                             (seg[0] * CELL, seg[1] * CELL, CELL, CELL))
        pygame.draw.rect(screen, RED,              # 画食物（红色方块）
                         (food[0] * CELL, food[1] * CELL, CELL, CELL))
        screen.blit(font.render(f"Score: {score}", True, WHITE), (10, 10))

        if game_over:                              # 结束后显示提示
            over_text = big_font.render("GAME OVER", True, RED)
            hint_text = font.render("Press R to restart, ESC to quit", True, WHITE)
            screen.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2,
                                    HEIGHT // 2 - 40))
            screen.blit(hint_text, (WIDTH // 2 - hint_text.get_width() // 2,
                                    HEIGHT // 2 + 10))

        pygame.display.flip()                      # 把刚才画的东西显示出来
        clock.tick(FPS)                            # 控制速度

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
