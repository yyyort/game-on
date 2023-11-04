import pygame as pg 
from os import walk

def import_folder(path):
    surface_list = []
    
    for _,_, image_files in walk(path):
        for image in image_files:
            full_path = path + '/' + image
            image_surface = pg.image.load(full_path).convert_alpha()
            surface_list.append(image_surface)
            
        return surface_list