"""
Ustawienia gry
"""


class Settings:
    """Klasa przeznaczona do przechowywania wszystkich ustawień gry."""

    def __init__(self):
        """Inicjalizacja ustwień gry."""
        # Ustawienia ekranu
        self.screen_width = 1600
        self.screen_height = 900

        # Zdefiniowanie koloru tła
        self.bg_color = (0, 0, 70)

        # Ustaweienia dotyczące statku
        self.ship_speed_factor = 1.5

        # Ustawienia dotyczące pocisku
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 160, 160, 160
        self.bullets_allowed = 3
