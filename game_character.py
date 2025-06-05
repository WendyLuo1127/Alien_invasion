# -*- coding: utf-8 -*-

import pygame
import sys

class GameCharacter:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)  # 加载图像
        self.rect = self.image.get_rect()  # 获取图像的矩形区域
        self.background_color = self.image.get_at((0, 0))  # 获取左上角像素作为背景色
    
    def draw(self, screen):
        # 获取屏幕宽高
        screen_width, screen_height = screen.get_size()
        # 计算图像绘制的位置，使其位于屏幕中央
        position = (screen_width // 2 - self.rect.width // 2, screen_height // 2 - self.rect.height // 2)
        screen.blit(self.image, position)  # 将角色绘制到屏幕
    
def main():
    pygame.init()

    # 创建一个屏幕，宽高为800x600
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Game Character Example")

    # 创建一个GameCharacter对象，传入图像文件路径
    character = GameCharacter('images/pika.png')

    # 设置背景色为角色的背景色
    screen.fill(character.background_color)

    # 主循环
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # 绘制角色
        character.draw(screen)

        # 更新屏幕
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
