import pygame, sys
from settings import *
from level import Level

 
class Game:
    def __init__(self):
        
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('Game_v1')
        self.clock = pygame.time.Clock()

        self.level = Level()

        # sound
        main_sound = pygame.mixer.Sound('../audio/main.ogg')
        main_sound.set_volume(0.0)
        main_sound.play(loops=-1)

        # menu toggles
        self.upgrade_menu_toggle = False
        self.pause_menu_toggle = False 
 
    def run(self):
        self.screen
        while True:
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_upgrade_menu()
                    
                    if event.key == pygame.K_ESCAPE:
                        self.level.toggle_pause_menu()
            
            # update window
            self.screen.fill(WATER_COLOUR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)
 
if __name__ == '__main__':
    game = Game()
    game.run()