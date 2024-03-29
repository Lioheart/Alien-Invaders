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
        self.bg_color = (207, 181, 59)

        # Ustaweienia dotyczące statku
        self.ship_limit = 3

        # Ustawienia dotyczące pocisku
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Ustawienia dotyczące obcego
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # 1 oznacza prawo; -1 oznacza lewo

        # Łatwa zmiana szybkości gry
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """
        Inicjalizacja ustawień, które ulegają zmianie w trakcie gry.
        """
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 0.5
        self.alien_points = 50

    def increase_speed(self):
        """Zmiana ustawień dotyczących szybkości."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
