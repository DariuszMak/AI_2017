#!/usr/bin/python3

import pygame

def rot_center(image, angle):
    """rotate a Surface, maintaining position."""

    loc = image.get_rect().center
    rot_sprite = pygame.transform.rotate(image, angle)
    rot_sprite.get_rect().center = loc
    return rot_sprite
