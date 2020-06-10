"""Służy do monitorowania danych statystycznych dla gry."""


class GameStats:
    """Monitorowanie danych statystycznych w grze 'Inwazja obcych'."""

    def __init__(self, ai_settings):
        """Inicjalizacja danych statystycznych.
        :param ai_settings: Ustawienia
        """
        self.ai_settings = ai_settings
        # Najlepszy wynik nigdy nie powinien zostać wyzerowany
        self.high_score = 0
        self.reset_stats()

        # Uruchomienie gry "Inwazja obcych" w stanie nieaktywnym
        self.game_active = False

    def reset_stats(self):
        """Inicjalizacja danych statystycznych, które mogą zmieniać się w trakcie gry."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
