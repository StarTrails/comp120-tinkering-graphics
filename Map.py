import pygame
import random


pygame.init()
TileSet = {
'GrassTile' : pygame.image.load("TileGrass.png"),
'WaterTile' : pygame.image.load("TileWater.png"),
'RockTile' : pygame.image.load("TileRock.png")
}

TileList = ['GrassTile', 'WaterTile', 'RockTile']

TILESIZE = 64
MAPWIDTH = 10
MAPHEIGHT = 15
TotalX = TILESIZE*MAPWIDTH
TotalY = TILESIZE*MAPHEIGHT

MAINSCREEN = pygame.display.set_mode((TotalX,TotalY))


GameCycle = True
while GameCycle:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameCycle = False
        if event.type == pygame.KEYDOWN and pygame.K_RETURN:
            for x in range(0, TotalX, TILESIZE):
                for y in range(0, TotalY, TILESIZE):
                    key = TileList[random.randint(0, len(TileList) - 1)]
                    MAINSCREEN.blit(TileSet[key], (x, y))


            pygame.display.flip()