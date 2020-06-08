"""Funkcje gry"""
import sys

import pygame

from bullet import Bullet


def fire_bullet(ai_settings, screen, ship, bullets):
    """Wystrzelenie pocisku, jeśli nie przekroczono ustalonego limitu.
    :param ai_settings: Ustawienia
    :param screen: Ekran
    :param ship: Statek
    :param bullets: Pociski (grupa)
    """
    # Utworzenie nowego pocisku i dodanie go do grupy pocisków
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_bullets(bullets):
    """Uaktualnienie położenia pocisków i usunięcie tych niewidocznych na ekranie.
    :param bullets: Pociski (grupa)
    """
    bullets.update()  # Uaktualnienie położenia pocisków

    # Usunięcie pocisków, które znajdują się poza ekranem
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def check_keydown_events(event, ship, ai_settings, screen, bullets):
    """
    Reakcja na naciśnięcie klawisza.
    :param ai_settings: Ustawienia
    :param screen: Ekran
    :param bullets: Pociski (grupa)
    :param event: Zdarzenie
    :param ship: Statek
    """
    if event.key == pygame.K_RIGHT:
        # Przesunięcie statku w prawą stronę
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    """
    Reakcja na zwolnienie klawisza
    :param event: Zdarzenie
    :param ship: Statek
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship, ai_settings, screen, bullets):
    """
    Reakcja na zdarzenia generowane przez klawiaturę i mysz.
    :param ai_settings: Ustawienia
    :param screen: Ekran
    :param bullets: Pociski (grupa)
    :param ship: Statek
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, ai_settings, screen, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """
    Uaktualnienie obrazów na ekranie i przejście do nowego ekranu.
    :param bullets: Pociski (grupa)
    :param ai_settings: Ustawienia gry
    :param screen: Ekran
    :param ship: Statek
    """
    # Odświeżanie ekranu w trakcjie każdej iteracji pętli
    screen.fill(ai_settings.bg_color)

    # Ponowne wyświetlenie wszystkich pocisków pod warstwami statku kosmicznego i obcych
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    # Wyświetlanie ostatnio zmodyfikowanego ekranu
    pygame.display.flip()
