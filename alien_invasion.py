"""
Wyświetla okno PyGame
"""

import pygame as pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():
    """
    Inicjalizacja gry
    """
    # Utworzenie obiektu ekranu
    pygame.init()  # Inicjalizacja ustawienia tła - wymagane
    ai_set = Settings()
    screen = pygame.display.set_mode(
        (ai_set.screen_width, ai_set.screen_height))  # Ustawienia okna (w nawiasie rozmiar)
    pygame.display.set_caption("Inwazja obcych")

    # Utworzenie statku kosmicznego
    ship = Ship(screen, ai_set)

    # Utworzenie grupy przeznaczonej do przechowywania pocisków.
    bullets = Group()

    # Rozpoczęcie pętli głównej gry
    while True:
        gf.check_events(ship, ai_set, screen, bullets)  # Sprawdzanie zdarzeń klawiatury
        ship.update()  # Uaktualnienie położenia statku
        gf.update_bullets(bullets)  # Ustalanie liczby pocisków na ekranie
        gf.update_screen(ai_set, screen, ship, bullets)  # Odświeżanie ekranu


if __name__ == '__main__':
    run_game()
