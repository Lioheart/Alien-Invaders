"""Zarządzanie całym zachowanie statku kosmicznego."""
import pygame


class Ship:
    """
    Odpowiada za właściwości statku kosmicznego.
    """

    def __init__(self, screen, ai_settings):
        """Inicjalizacja statku kosmicznego i jego położenie początkowe.
        :param screen: Ekran
        :param ai_settings: Ustawienia gry
        """
        self.screen = screen
        self.ai_set = ai_settings

        # Wczytanie obrazu statku kosmicznego i pobranie jego prostokąta
        self.image = pygame.image.load('images/space-ship.png')  # Wczytanie obrazu
        self.image = pygame.transform.scale(self.image, (70, 83))
        self.rect = self.image.get_rect()  # Ustawienie prostokąta dla obrazu
        self.screen_rect = screen.get_rect()

        # Każdy nowy statek kosmiczny pojawia się na dole ekranu
        self.rect.centerx = self.screen_rect.centerx  # Służy do obsługi gdzie znajduje się statek
        self.rect.bottom = self.screen_rect.bottom - 5

        # Punkt środkowy statku jest przechowywany w postaci liczby zmiennoprecinkowej
        self.center = float(self.rect.centerx)

        # Opcje wskazujące na poruszanie się statku
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """
        Uaktualnienie położenia statku na podstawie opcji wskazującej na jego ruch.
        """
        # Uaktualnienie wartości punktu środkowego statku, a nie jego prostokąta
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_set.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_set.ship_speed_factor

        # Uaktualnienie obiektu rect na podstawie wartosci self.center
        self.rect.centerx = self.center

    def blitme(self):
        """
        Wyswietlanie statku kosmicznego w jego aktualnym położeniu.
        """
        self.screen.blit(self.image, self.rect)
