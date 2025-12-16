import pygame
import sys
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from menuitems import MenuItem

class Screen:
    current_screen = "Menu"
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock1 = pygame.time.Clock()
    dt = 0

    def handle_event(self):
        pass

    def update(self, dt):
        pass

    def draw(self, screen):
        pass


class MenuScreen(Screen):
    titlefont = pygame.font.Font(None, 90)
    def __init__(self, menu_items, menu_location, menu_title=("", (0, 0))):
        self.__menu_length = len(menu_items)
        

        self.menu_title = MenuScreen.titlefont.render(menu_title[0], True, (255, 255, 255))
        self.title_location = menu_title[1]

        menu_spread = menu_location[1] - menu_location[0]
        item_pos = [pos for pos in range(menu_location[0] + 24, menu_location[1] - 24, menu_spread // len(menu_items))]
        self.menu_items = [MenuItem(menu_items[i], (SCREEN_WIDTH // 2, item_pos[i])) for i in range(len(menu_items))]

        self.index = 0
        self.menu_selection = 0

    def move_down(self):
        self.menu_items[self.index].unselect()
        self.index = (self.index + 1) % self.__menu_length
        self.menu_items[self.index].select()

    def move_up(self):
        self.menu_items[self.index].unselect()
        self.index = (self.index + self.__menu_length - 1) % self.__menu_length
        self.menu_items[self.index].select()

    def current_item(self):
        return self.menu_items[self.index]
    
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if self.menu_selection > 0:
                return
            else:
                if event.key == pygame.K_w:
                    self.move_up()
                elif event.key == pygame.K_s:
                    self.move_down()
                elif event.key == pygame.K_SPACE:
                    self.activate()
                self.menu_selection = MENU_SELECTION_COOLDOWN
        
        if event.type == pygame.QUIT:
                sys.exit()
        
    
    def update(self, dt):
        self.menu_selection = max(self.menu_selection - dt, 0)
        for event in pygame.event.get():
            self.handle_event(event)
    
    def draw(self, screen):
        screen.fill("black")
        screen.blit(self.menu_title, self.title_location)
        for item in self.menu_items:
            item.draw(screen)

    def play(self):

        while Screen.current_screen == "Menu":
            self.update(Screen.dt)
            self.draw(Screen.screen)
            pygame.display.flip()
            Screen.dt = Screen.clock1.tick(60) / 1000
        return

    def activate(self):
        Screen.current_screen = self.menu_items[self.index].activate()

class PlayScreen(Screen):

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return "Menu"

    def play(self):

        asteroids = pygame.sprite.Group()
        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        shots = pygame.sprite.Group()

        AsteroidField.containers = (updatable,)
        Asteroid.containers = (asteroids, updatable, drawable)
        Player.containers = (updatable, drawable)
        Shot.containers = (updatable, drawable, shots)
    
     
        field = AsteroidField()
        player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        
        while Screen.current_screen == "Play":
            log_state()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if self.handle_event(event) == "Menu":
                    Screen.current_screen = "Menu"


            updatable.update(Screen.dt)
            for object in asteroids:
                if player1.collides_with(object):
                    log_event("player_hit")
                    print("Game over!")
                    sys.exit()
        
            for asteroid in asteroids:
                for shot in shots:
                    if shot.collides_with(asteroid):
                        log_event("asteroid_shot")
                        asteroid.split()
                        shot.kill()

            Screen.screen.fill("black")
        
            for object in drawable:
                object.draw(Screen.screen)
        
            pygame.display.flip()
            Screen.dt = Screen.clock1.tick(60) / 1000
        return