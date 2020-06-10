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
        self.bg_color = (207, 181, 59)

        # Ustaweienia dotyczące statku
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Ustawienia dotyczące pocisku
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Ustawienia dotyczące obcego
        self.alien_speed_factor = 0.6
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # 1 oznacza prawo; -1 oznacza lewo
