"""Służy do monitorowania danych statystycznych dla gry."""


class GameStats:
    """Monitorowanie danych statystycznych w grze 'Inwazja obcych'."""

    def __init__(self, ai_settings):
        """Inicjalizacja danych statystycznych."""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Uruchomienie gry "Inwazja obcych" w stanie aktywnym
        self.game_active = True

    def reset_stats(self):
        """Inicjalizacja danych statystycznych, które mogą zmieniać się w trakcie gry."""
        self.ships_left = self.ai_settings.ship_limit
