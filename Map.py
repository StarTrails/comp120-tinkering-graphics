"""Imports needed modules for code to function"""
import pygame
import random

pygame.init()

"""Specifies what images to use and defines their name"""
TileSet = {
'GrassTile' : pygame.image.load("TileGrass.png"),
'WaterTile' : pygame.image.load("TileWater.png"),
'RockTile' : pygame.image.load("TileRock.png")
}

"""Creates a list of all images defined"""
TileList = ['GrassTile', 'WaterTile', 'RockTile']

"""Sets the screen width and hieghts and also defines tilesize"""
TILESIZE = 64
MAPWIDTH = 10
MAPHEIGHT = 10
TotalX = TILESIZE*MAPWIDTH
TotalY = TILESIZE*MAPHEIGHT

"""Sets the name of the monitor that is used and the size"""
MAINSCREEN = pygame.display.set_mode((TotalX,TotalY))


TileList = ['GrassTile', 'WaterTile', 'RockTile']

TILESIZE = 64
MAPWIDTH = 10
MAPHEIGHT = 15
TotalX = TILESIZE*MAPWIDTH
TotalY = TILESIZE*MAPHEIGHT

MAINSCREEN = pygame.display.set_mode((TotalX,TotalY))



"""Creates the forloop that generates random terrain"""
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