# -*- coding: utf-8 -*-

import pygame
import sys

class GameCharacter:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)  # ����ͼ��
        self.rect = self.image.get_rect()  # ��ȡͼ��ľ�������
        self.background_color = self.image.get_at((0, 0))  # ��ȡ���Ͻ�������Ϊ����ɫ
    
    def draw(self, screen):
        # ��ȡ��Ļ���
        screen_width, screen_height = screen.get_size()
        # ����ͼ����Ƶ�λ�ã�ʹ��λ����Ļ����
        position = (screen_width // 2 - self.rect.width // 2, screen_height // 2 - self.rect.height // 2)
        screen.blit(self.image, position)  # ����ɫ���Ƶ���Ļ
    
def main():
    pygame.init()

    # ����һ����Ļ�����Ϊ800x600
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Game Character Example")

    # ����һ��GameCharacter���󣬴���ͼ���ļ�·��
    character = GameCharacter('images/pika.png')

    # ���ñ���ɫΪ��ɫ�ı���ɫ
    screen.fill(character.background_color)

    # ��ѭ��
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # ���ƽ�ɫ
        character.draw(screen)

        # ������Ļ
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
