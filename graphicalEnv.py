import pygame

pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

GRID_DISTANCE = 50

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

assert DISPLAY_WIDTH % GRID_DISTANCE == 0
assert DISPLAY_HEIGHT % GRID_DISTANCE == 0

car_width = 73

class Grid():
    def __init__(self, DISPLAY_WIDTH, DISPLAY_HEIGHT, GRID_DISTANCE):
        self._WIDTH = int(DISPLAY_WIDTH / GRID_DISTANCE )
        self._HEIGHT = int(DISPLAY_WIDTH / GRID_DISTANCE )

        self.grid = [[None for i in range(self._WIDTH)] for i in range(self._HEIGHT)]


class Car(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image= pygame.image.load('forklift2.png')
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

    def moveRight(self,):
        self.x += 1

    def moveLeft(self,):
        self.x -= 1

    def moveUp(self,):
        self.y += 1

    def moveDown(self,):
        self.y -= 1
        self.rect.y = self.y * GRID_DISTANCE

    def display(self, display):
        self.rect.x = self.x * GRID_DISTANCE
        self.rect.y = self.y * GRID_DISTANCE
        display.blit(self.image, (self.rect.x, self.rect.y))

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
pygame.display.set_caption('AI classes project')
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')

def car(x,y):
    gameDisplay.blit(carImg,(x,y))





carclass = Car(2, 2)

def game_loop():
    # x = (DISPLAY_WIDTH * 0.45)
    # y = (DISPLAY_HEIGHT * 0.8)
    x = 0
    y = 550

    x_change = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                    carclass.moveLeft()
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                    carclass.moveRight()
                if event.key == pygame.K_UP:
                    carclass.moveDown()
                if event.key == pygame.K_DOWN:
                    carclass.moveUp()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        print(x)

        gameDisplay.fill(WHITE)

        for i in range(0, DISPLAY_WIDTH, GRID_DISTANCE):
            pygame.draw.line(gameDisplay, BLACK, [i, 0], [i,600], 1)

        for i in range(0, DISPLAY_HEIGHT, GRID_DISTANCE):
            pygame.draw.line(gameDisplay, BLACK, [0, i], [800,i], 1)

        car(x,y)
        carclass.display(gameDisplay)

        if x > DISPLAY_WIDTH - car_width or x < 0:
            gameExit = True


        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
