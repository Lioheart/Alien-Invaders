"""Funkcje gry"""
import sys
from time import sleep

import pygame

from alien import Alien
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


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Reakcja na kolizję między pociskiem i obcym
    :param stats: Statystyki
    :param sb: Tablica wyników
    :param ai_settings: Ustawienia
    :param screen: Ekran
    :param ship: Statek
    :param aliens: Flota obcych (grupa)
    :param bullets: Pociski (grupa)
    """
    # Usunięcie wszystkich pocisków i obcych, między którymi doszło do kolizji
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for alien in collisions.values():
            stats.score += ai_settings.alien_points * len(alien)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # Pozbycie się istniejących pocisków, przyspieszenie gry i utworzenie nowej floty
        bullets.empty()
        ai_settings.increase_speed()

        # Inkrementacja numeru poziomu
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)


def check_high_score(stats, sb):
    """
    Sprawdzenie, czy mamy nowy najlepszy wynik osiągnięty dotąd w grze.
    :param stats: Statystyki
    :param sb: Tablica wyników
    """
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def update_bullets(bullets, aliens, ai_settings, screen, ship, stats, sb):
    """Uaktualnienie położenia pocisków i usunięcie tych niewidocznych na ekranie.
    :param stats: Statystyki
    :param sb: Tablica wyników
    :param ai_settings: Ustawienia
    :param screen: Ekran
    :param ship: Statek
    :param aliens: Flota obcych (grupa)
    :param bullets: Pociski (grupa)
    """
    bullets.update()  # Uaktualnienie położenia pocisków

    # Usunięcie pocisków, które znajdują się poza ekranem
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


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
    elif event.key == pygame.K_q:
        sys.exit()


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


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """
    Rozpoczęcie nowej gry po kliknięciu przycisku Uruchom grę przez użytkownika.
    :param sb: Tablica wyników
    :param ai_settings: Ustawienia
    :param screen: Ekran
    :param ship: Statek
    :param aliens: Flota obcych (grupa)
    :param bullets: Pociski (grupa)
    :param stats: Statystyki
    :param play_button: Przycisk Uruchom grę
    :param mouse_x: Pozycja kursora w osi X
    :param mouse_y: Pozycja kursora w osi Y
    """
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Wyzerowanie ustawień dotyczących gry
        ai_settings.initialize_dynamic_settings()

        # Ukrycie kursora myszy
        pygame.mouse.set_visible(False)

        # Wyzerowanie danych statystycznych
        stats.reset_stats()
        stats.game_active = True

        # Wyzerowanie obrazów tablicy wyników
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ship()

        # Usunięcie zawartości list aliens i bullets
        aliens.empty()
        bullets.empty()

        # Utworzenie nowej floty i wysrodkowanie statku
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """
    Reakcja na zdarzenia generowane przez klawiaturę i mysz.
    :param sb: Tablica wyników
    :param aliens: Flota obcych (grupa)
    :param stats: Statystyki
    :param play_button: Przycisk Uruchom grę
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

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def update_screen(ai_settings, screen, ship, bullets, aliens, play_button, stats, sb):
    """
    Uaktualnienie obrazów na ekranie i przejście do nowego ekranu.
    :param sb: Tablica wyników
    :param stats: Statystyki
    :param play_button: Przycisk Uruchom grę
    :param aliens: Statki obcych (grupa
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
    aliens.draw(screen)

    # Wyświetlenie informacji o punktacji
    sb.show_score()

    # Wyświetlenie przycisku tylko wtedy, gdy gra jest nieaktywna
    if not stats.game_active:
        play_button.draw_button()

    # Wyświetlanie ostatnio zmodyfikowanego ekranu
    pygame.display.flip()


def get_number_aliens_x(ai_settings, alien_width):
    """Ustalenie liczby obcych, którzy zmieszczą się w rzędzie.
    :param ai_settings: Ustawienia
    :param alien_width: Szerokość statku obcego
    :return: Ilość obcych w rzędzie - int
    """
    available_space_x = ai_settings.screen_width - 2 * alien_width  # Ilość miejsca w poziomie
    number_aliens_x = int(available_space_x / (2 * alien_width))  # Ile obcych zmieści się w rzędzie
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """Ustalenie, ile rzędów obcych zmieści się na ekranie.
    :param ai_settings: Ustawienia
    :param ship_height: Wysokość statku
    :param alien_height: Wysokość statku obcego
    :return: Ilość rzędów statków obcych - int
    """
    available_space_y = (ai_settings.screen_height - (7 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Utworzenie obcego i umieszczenie go w rzędzie
    :param ai_settings: Ustawienia
    :param screen: Ekran
    :param aliens: Flota obcych (grupa)
    :param alien_number: numer kolumny
    :param row_number: numer wiersza
    """
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width  # Szerokość obcego

    # Utworzenie obcego i umieszczenie go w rzędzie
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number + 5
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """Utworzenie pełnej floty obcych.
    :param ai_settings: Ustawienia
    :param screen: Ekran
    :param aliens: Flota obcych (grupa)
    :param ship: Statek
    """
    # Utworzenie obcego i ustalenie liczby obcych, którzy zmieszczą się w rzędzie
    # Odległość między poszczególnymi obcymi jest równa szerokości obcego
    alien = Alien(ai_settings, screen)  # Nie jest częścią floty - bierzemy wymiary
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Utworzenie pierwszego rzędu obcych
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, sb):
    """
    Sprawdzenie, czy którykolwiek obcy dotarł do dolnej krawędzi ekranu.
    :param sb: Tablica wyników
    :param ai_settings: Ustawienia
    :param stats: Statystyki
    :param screen: Ekran
    :param ship: Statek
    :param aliens: Flota obcych (grupa)
    :param bullets: Pociski (grupa)
    """
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)
            break


def update_aliens(ai_settings, aliens, ship, stats, screen, bullets, sb):
    """Sprawdzenie, czy flota znajduje się przy krawędzi ekranu, a następnie uaktualnienie położenia wszystkich
    obcych we flocie.
    :param sb: Tablica wyników
    :param stats: Statystyki
    :param screen: Ekran
    :param bullets: Pociski (grupa)
    :param ship: Statek
    :param ai_settings: Ustawienia
    :param aliens: Flota obcych (grupa)"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Wykrywanie kolizji między obcym i statkiem.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)

    # Wyszukiwanie obcych docierających do dolnej krawędzi ekranu
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, sb)


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb):
    """Reakcja na uderzenie obcego w statek.
    :param sb: Tablica wyników
    :param ai_settings: Ustawienia
    :param stats: Statystyki
    :param screen: Ekran
    :param ship: Statek
    :param aliens: Flota obcych (grupa)
    :param bullets: Pociski (grupa)
    """
    if stats.ships_left > 1:
        stats.ships_left -= 1

        # Uaktualnienie tablicy wyników
        sb.prep_ship()

        # Usunięcie zawartości list aliens i bullets
        aliens.empty()
        bullets.empty()

        # Utworzenie nowej floty i wyśrodkowanie statku
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Pauza
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def change_fleet_direction(ai_settings, aliens):
    """Przesunięcie całej floty w dół i zmiana kierunku, w którym się ona porusza.
    :param ai_settings: Ustawienia
    :param aliens: Flota obcych (grupa)
    """
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_fleet_edges(ai_settings, aliens):
    """Odpowiednia reakcja, gdy obcy dotrze do krawędzi ekranu.
    :param ai_settings: Ustawienia
    :param aliens: Flota obcych (grupa)
    """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
