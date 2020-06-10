"""
Wyświetla okno PyGame
"""

import pygame as pygame
from pygame.sprite import Group

import game_functions as gf
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
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

    # Utworzenie przycisku Uruchom grę
    play_button = Button(ai_set, screen, 'Uruchom grę')

    # Utworzenie egzemplarza przeznaczonego do przechowywania danych statystycznych dotyczących gry oraz utworzenie
    # egzemplarza Scoreboard
    stats = GameStats(ai_set)
    sb = Scoreboard(ai_set, screen, stats)

    # Utworzenie statku kosmicznego, grupy pocisków oraz grupy obcych
    ship = Ship(screen, ai_set)
    aliens = Group()
    bullets = Group()

    # Utworzenie floty obcych
    gf.create_fleet(ai_set, screen, ship, aliens)

    # Rozpoczęcie pętli głównej gry
    while True:
        gf.check_events(ai_set, screen, stats, sb, play_button, ship, aliens, bullets)  # Sprawdzanie zdarzeń klawiatury
        if stats.game_active:
            ship.update()  # Uaktualnienie położenia statku
            gf.update_bullets(bullets, aliens, ai_set, screen, ship, stats, sb)  # Ustalanie liczby pocisków na ekranie
            gf.update_aliens(ai_set, aliens, ship, stats, screen, bullets, sb)  # Uaktualnienie położenia każdego obcego
        gf.update_screen(ai_set, screen, ship, bullets, aliens, play_button, stats, sb)  # Odświeżanie ekranu


if __name__ == '__main__':
    run_game()
