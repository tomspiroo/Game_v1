import pygame
from settings import *

class Upgrade:
    def __init__(self,player):
        
        # general setup
        self.display_surface = pygame.display.get_surface()
        self.player = player
        self.attribute_nmbr = len(player.stats)
        self.attribute_names = list(player.stats.keys())
        self.max_values = list(player.max_stats.values())
        self.font = pygame.font.Font(UI_FONT,UI_FONT_SIZE)

        # item creation
        self.height = self.display_surface.get_size()[1] * 0.8
        self.width = self.display_surface.get_size()[0] // 6
        self.create_items()

        # selection system
        self.selection_index = 0
        self.selection_time = None
        self.can_upgrade = True
        self.selection_cooldown_time = 300
    
    def input(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]

        for index, item in enumerate(self.item_list):
            if item.rect.collidepoint(mouse_pos):
                self.selection_index = index
                if mouse_pressed and self.can_upgrade:  
                    item.trigger(self.player)
                    self.can_upgrade = False
                    self.selection_time = pygame.time.get_ticks()

    def selection_cooldown(self):
        if not self.can_upgrade:
            current_time = pygame.time.get_ticks()
            if current_time - self.selection_time >= self.selection_cooldown_time:
                self.can_upgrade = True

    def create_items(self):
        self.item_list = []

        for item, index in enumerate(range(self.attribute_nmbr)):
            full_width = self.display_surface.get_size()[0] 
            increment = full_width // self.attribute_nmbr
            left = (item * increment) + (increment - self.width) // 2 

            top = self.display_surface.get_size()[1] * 0.1

            item = Item(left,top,self.width,self.height,index,self.font)
            self.item_list.append(item)

    def display(self):
        self.input()
        self.selection_cooldown()

        for index, item in enumerate(self.item_list):

            # get attributes
            name = self.attribute_names[index]
            value = self.player.get_value_by_index(index)
            max_value = self.max_values[index]
            cost = self.player.get_cost_by_index(index)
            item.display(self.display_surface,self.selection_index,name,value,max_value,cost)

class Item:
    def __init__(self,l,t,w,h,index,font):
        self.rect = pygame.Rect(l,t,w,h)
        self.index = index
        self.font = font
    
    def display_names(self,surface,name,cost,selected):
        colour = TEXT_COLOUR_SELECTED if selected else TEXT_COLOUR
        # title
        title_surf = self.font.render(name,False,colour)
        title_rect = title_surf.get_rect(midtop = self.rect.midtop + pygame.math.Vector2(0,20))
        
        # cost 
        cost_surf = self.font.render(f'Cost:{int(cost)}',False,colour)
        cost_rect = cost_surf.get_rect(midbottom = self.rect.midbottom - pygame.math.Vector2(0,20))

        # draw
        surface.blit(title_surf,title_rect)
        surface.blit(cost_surf,cost_rect)

    def display_bar(self,surface,value,max_value,selected):

        # drawing setup
        top = self.rect.midtop + pygame.math.Vector2(0,60)
        bottom = self.rect.midbottom - pygame.math.Vector2(0,60)
        colour = BAR_COLOUR_SELECTED if selected else BAR_COLOUR

        # bar setup
        full_height = bottom[1] - top[1]
        relative_number = (value/max_value) * full_height
        value_rect = pygame.Rect(top[0] - 15,bottom[1] - relative_number,30,10)

        # draw elements
        pygame.draw.line(surface,colour,top,bottom,5)
        pygame.draw.rect(surface,colour,value_rect)

    def trigger(self,player):
        upgrade_attribute = list(player.stats.keys())[self.index]
        
        if player.exp >= player.upgrade_cost[upgrade_attribute] and player.stats[upgrade_attribute] < player.max_stats[upgrade_attribute]:
            player.exp -= player.upgrade_cost[upgrade_attribute]
            player.stats[upgrade_attribute] *= 1.2
            player.upgrade_cost[upgrade_attribute] *= 1.4

        if player.stats[upgrade_attribute] > player.max_stats[upgrade_attribute]:
            player.stats[upgrade_attribute] = player.max_stats[upgrade_attribute]

    def display(self,surface,selection_num,name,value,max_value,cost):
        if self.index == selection_num:
            pygame.draw.rect(surface,UPGRADE_BG_COLOUR_SELECTED,self.rect)
            pygame.draw.rect(surface,UI_BOARDER_COLOUR,self.rect,4)
        else:
            pygame.draw.rect(surface,UI_BG_COLOUR,self.rect)
            pygame.draw.rect(surface,UI_BOARDER_COLOUR,self.rect,4)

        self.display_names(surface,name,cost,self.index == selection_num)
        self.display_bar(surface,value,max_value,self.index == selection_num)