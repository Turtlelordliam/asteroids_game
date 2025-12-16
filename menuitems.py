import pygame
pygame.init()
pygame.font.init()


class MenuItem:
    selected_font = pygame.font.Font(None, 55)
    font = pygame.font.Font(None, 48)
    
    def __init__(self, text, position):
        self.__text = text
        self.selected = False
        self.new_screen = text
        self.text_surface = MenuItem.font.render(self.__text, True, (255, 255, 255))
        self.position = position
    
    def select(self):
        self.selected = True
        self.text_surface = MenuItem.selected_font.render(self.__text, True, (0, 0, 255))
    
    def unselect(self):
        self.selected = False
        self.text_surface = MenuItem.font.render(self.__text, True, (255, 255, 255))

    def draw(self, screen):
        screen.blit(self.text_surface, self.position)

    def activate(self):
        return self.__text