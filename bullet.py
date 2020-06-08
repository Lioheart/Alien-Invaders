"""Ustawienia przycisku"""
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Klasa przeznaczona do zarządzania pociskami wystrzeliwanymi przez statek."""

    def __init__(self, ai_settings, screen, ship):
        """Utworzenie obiektu pocisku w aktualnym położeniu statku.
        :param ai_settings: Ustawienia
        :param screen: Ekran
        :param ship: Statek
        """
        # super(Bullet, self).__init__()    - python 2.7
        # super().__init__()                - python 3
        super().__init__()  # Konieczne, aby zapewnić prawidłowe dziedziczenie
        self.screen = screen

        # Utworzenie prostokąta pocisku w punkcjie (0,0), a następnie zdefiniowanie dla niego odpowiedniego położenia
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Położenie pocisku jest zdefiniowanie za pomocą wartości zmiennoprzecinkowej.
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Poruszanie pociskiem po ekranie."""
        # Uaktualnienie położenia pocisku
        self.y -= self.speed_factor

        # Uaktualnienie położenia prostokąta pocisku
        self.rect.y = self.y

    def draw_bullet(self):
        """Wyświetlenie pocisku na ekranie."""
        pygame.draw.rect(self.screen, self.color, self.rect)
