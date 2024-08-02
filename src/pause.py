import pygame
from settings import *
from upgrade import Item

class Pause:
    def __init__(self, player):

        # general setup
        self.display_surface = pygame.display.get_surface()
        self.player = player
        self.attribute_nmbr = 3
        self.attribute_names_1 = ['Resume', 'Options', 'Quit']
        self.attribute_names_2 = ['Video Options', 'Audio Options', 'Back']
        self.font = pygame.font.Font(UI_FONT,UI_FONT_SIZE)

        # item creation
        self.height = self.display_surface.get_size()[1] // 3
        self.width = self.display_surface.get_size()[0] * 0.2
        self.create_items()

        # selection system
        self.selection_index = 0
        self.selection_time = None
        self.can_move = True
        self.selection_cooldown_time = 200

    def input(self):
        keys = pygame.key.get_pressed()

        if self.can_move:
            if keys[pygame.K_DOWN] and self.selection_index < self.attribute_nmbr - 1:
                self.selection_index += 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
            elif keys[pygame.K_UP]and self.selection_index >= 1:
                self.selection_index -= 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()

            if keys[pygame.K_RETURN]: # <- return might not work for right enter, could change to space
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
                # Code for selection

    def create_items(self):
        self.item_list = []

        for item, index in enumerate(range(self.attribute_nmbr)):
            full_height = self.display_surface.get_size()[1] 
            increment = full_height // self.attribute_nmbr
            top = (item * increment) + (increment - self.height) // 2 

            left = self.display_surface.get_size()[0] * 0.2

            item = Item(left,top,self.width,self.height,index,self.font)
            self.item_list.append(item)

    def change_player_keybinds(self):
        pass

    def display(self):
        pass

class Button:
    def __init__(self,x,y,rect,scale):
        pass