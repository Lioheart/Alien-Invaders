"""
Wyświetla okno PyGame
"""

import pygame as pygame
from pygame.sprite import Group

import game_functions as gf
from game_stats import GameStats
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

    # Utworzenie egzemplarza przeznaczonego do przechowywania danych statystycznych dotyczących gry.
    stats = GameStats(ai_set)

    # Utworzenie statku kosmicznego, grupy pocisków oraz grupy obcych
    ship = Ship(screen, ai_set)
    aliens = Group()
    bullets = Group()

    # Utworzenie floty obcych
    gf.create_fleet(ai_set, screen, aliens, ship)

    # Rozpoczęcie pętli głównej gry
    while True:
        gf.check_events(ship, ai_set, screen, bullets)  # Sprawdzanie zdarzeń klawiatury
        if stats.game_active:
            ship.update()  # Uaktualnienie położenia statku
            gf.update_bullets(bullets, aliens, ai_set, screen, ship)  # Ustalanie liczby pocisków na ekranie
            gf.update_aliens(ai_set, aliens, ship, stats, screen, bullets)  # Uaktualnienie położenia każdego obcego
        gf.update_screen(ai_set, screen, ship, bullets, aliens)  # Odświeżanie ekranu

if __name__ == '__main__':
    run_game()
