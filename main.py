import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from menuitems import MenuItem
import screen1

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    pygame.font.init()

    game = screen1.PlayScreen()
    menu = screen1.MenuScreen(["Play", "Exit"],[SCREEN_HEIGHT // 2, SCREEN_HEIGHT], menu_title=("Asteroid Destroyer", (SCREEN_WIDTH // 3, 50)))
    while True:
        if screen1.Screen.current_screen == "Menu":
            menu.play()
        if screen1.Screen.current_screen == "Play":
            game.play()
        if screen1.Screen.current_screen == "Exit":
            sys.exit()
            return


if __name__ == "__main__":
    main()
