from csv import reader
from os import walk
import pygame
import re

def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map,delimiter=',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map
    
def import_folder(path):
    surface_list = []
    for _,__,img_files in walk(path):
        img_files.sort()
        img_files.sort()
        for image in img_files:           
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            # print(full_path)
            surface_list.append(image_surf)
    
    return surface_list