import pygame
from settings import *
from pygame.locals import KEYDOWN, K_ESCAPE

class Pause:
    def __init__(self):

        # general setup
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT,UI_FONT_SIZE)
        self.current_menu = 'main'
        
        
        # main menu options
        self.main_menu_options = ['Resume', 'Options', 'Quit']
        self.main_selection_index = 0
        self.main_menu_items = self.create_menu_items(self.main_menu_options)

        # options menu options
        self.options_menu_options = ['Video Options', 'Audio Options', 'Keybinds', 'Back']
        self.options_selection_index = 0
        self.options_menu_items = self.create_menu_items(self.options_menu_options)


        # selection system
        self.selection_time = None
        self.can_select = True
        self.selection_cooldown_time = 300

    def create_menu_items(self, options):
        items = []
        full_width = self.display_surface.get_size()[0]
        menu_height = len(options) * 50 + (len(options) - 1) * 10  # Calculate the height of the menu
        top_offset = (self.display_surface.get_size()[1] - menu_height) // 2

        for index, option in enumerate(options):
            left = full_width // 2
            top = top_offset + index * 60  # Space items vertically with 60px height
            item = Item(left, top, option, self.font)
            items.append(item)

        return items

    def input(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]

        if self.current_menu == 'main':
            items = self.main_menu_items
            selection_index = self.main_selection_index
        else:
            items = self.options_menu_items
            selection_index = self.options_selection_index

        for index, item in enumerate(items):
            if item.rect.collidepoint(mouse_pos):
                # Update the selection index for the current menu
                if self.current_menu == 'main':
                    self.main_selection_index = index
                else:
                    self.options_selection_index = index
                
                if mouse_pressed and self.can_select:
                    if self.current_menu == 'main':
                        self.handle_main_selection()
                    else:
                        self.handle_options_selection()
                    
                    self.can_select = False
                    self.selection_time = pygame.time.get_ticks()

    def handle_main_selection(self):
        match self.main_selection_index:
            case 0:
                key_press_event = pygame.event.Event(KEYDOWN, {"key": K_ESCAPE})
                pygame.event.post(key_press_event)
            case 1:
                self.current_menu = 'options'
            case 2:
                pygame.quit()

    def handle_options_selection(self):
        match self.options_selection_index:
            case 0:
                pass  # Handle video options
            case 1:
                pass  # Handle audio options
            case 2:
                pass  # Handle keybind options
            case 3:
                self.current_menu = 'main'

    def selection_cooldown(self):
        if not self.can_select:
            current_time = pygame.time.get_ticks()
            if current_time - self.selection_time >= self.selection_cooldown_time:
                self.can_select = True

    def change_player_keybinds(self):
        pass

    def display(self):
        self.input()
        self.selection_cooldown()

        if self.current_menu == "main":
            items = self.main_menu_items
            selection_index = self.main_selection_index
        else:
            items = self.options_menu_items
            selection_index = self.options_selection_index

        for index, item in enumerate(items):
            selected = (index == selection_index)
            item.display(self.display_surface, selected)

class Item:
    def __init__(self, l, t, text, font):
        self.font = font
        self.text = text
        self.text_surf = self.font.render(text, False, TEXT_COLOUR)
        self.rect = self.text_surf.get_rect(center=(l, t))

    # def display(self, surface, selected):
    #     colour = TEXT_COLOUR_SELECTED if selected else TEXT_COLOUR
    #     text_surf = self.font.render(self.text, False, colour)
    #     pygame.draw.rect(surface, UPGRADE_BG_COLOUR_SELECTED if selected else UI_BG_COLOUR, self.rect)
    #     pygame.draw.rect(surface, UI_BOARDER_COLOUR, self.rect, 4)
    #     surface.blit(text_surf, self.rect)
    def display(self, surface, selected):
        colour = TEXT_COLOUR_SELECTED if selected else TEXT_COLOUR
        bg_colour = UPGRADE_BG_COLOUR_SELECTED if selected else UI_BG_COLOUR

        # Draw background rectangle
        pygame.draw.rect(surface, bg_colour, self.rect.inflate(20, 10))  # Add padding to the rectangle

        # Draw border
        pygame.draw.rect(surface, UI_BOARDER_COLOUR, self.rect.inflate(20, 10), 4)

        # Draw text
        text_surf = self.font.render(self.text, False, colour)
        surface.blit(text_surf, text_surf.get_rect(center=self.rect.center))