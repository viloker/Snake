import pygame
import os
import random

os.environ['SDL_VIDEO_CENTERED'] = "1"


class Food:
    def __init__(self):
        self.x = random.randrange(10, 770, 2) * 1.0
        self.y = random.randrange(10, 670, 2) * 1.0
        self.x2 = self.x + 20
        self.y2 = self.y + 20
        self.color = (255, 41, 41)


class Snake:
    def __init__(self):
        """ window """
        pygame.init()
        self.WINDOW = pygame.display.set_mode((800, 700))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 25)

        """ snake """
        self.x, self.y = 800 // 2, 700 // 2
        self.x2, self.y2 = self.x + 20, self.y + 20
        self.running = True
        self.move_x, self.move_y = 0, 0
        self.snake_block = 20
        self.snake_color = (67, 254, 240)
        self.snake_body = [[self.x, self.y]]
        self.snake_length = 1

        self.score = 0
        self.food = Food()

    def processInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:

                match event.key:
                    case pygame.K_RIGHT:
                        self.move_x = 2
                        self.move_y = 0
                    case pygame.K_LEFT:
                        self.move_x = -2
                        self.move_y = 0
                    case pygame.K_UP:
                        self.move_x = 0
                        self.move_y = -2
                    case pygame.K_DOWN:
                        self.move_x = 0
                        self.move_y = 2
                # if event.key == pygame.K_RIGHT:
                #     self.move_x = 2
                #     self.move_y = 0
                # elif event.key == pygame.K_LEFT:
                #     self.move_x = -2
                #     self.move_y = 0
                # elif event.key == pygame.K_UP:
                #     self.move_x = 0
                #     self.move_y = -2
                # elif event.key == pygame.K_DOWN:
                #     self.move_x = 0
                #     self.move_y = 2

        if self.x >= 780 or self.x < 0 or self.y >= 680 or self.y < 0:
            self.running = False
            self.move_x, self.move_y = 0, 0

    def update(self):
        self.x += self.move_x
        self.y += self.move_y
        self.x2 = self.x + self.snake_block
        self.y2 = self.y + self.snake_block

        if self.food.x <= self.x <= self.food.x2 and \
                self.food.y <= self.y <= self.food.y2 or \
                self.food.x <= self.x2 <= self.food.x2 and \
                self.food.y <= self.y2 <= self.food.y2:
            self.food = Food()
            self.snake_length += 5
            self.score += 1

        self.snake_body.append([self.x, self.y])
        if len(self.snake_body) > self.snake_length:
            del self.snake_body[0]


    def render(self):

        def draw_score(text):
            label = self.font.render(text, True, (255,255,255))
            self.WINDOW.blit(label, (650, 20))

        def draw_snake(snake_body):
            for item in snake_body:
                pygame.draw.rect(self.WINDOW, self.snake_color, (item[0], item[1], self.snake_block, self.snake_block))

        self.WINDOW.fill((225, 138, 248))
        draw_snake(self.snake_body)

        pygame.draw.rect(self.WINDOW, self.food.color, (self.food.x, self.food.y, self.snake_block, self.snake_block))
        draw_score(f"Score: {self.score}")
        pygame.display.update()

    def run(self):
        while self.running:
            self.processInput()
            self.update()
            self.render()
            self.clock.tick(120)


game = Snake()
game.run()
pygame.quit()
quit()
