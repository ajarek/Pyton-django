Podsumowanie projektu: Finance Tracker (MVP)
Aplikacja Finance Tracker została stworzona i skonfigurowrowana. Zawiera wszystkie funkcjonalności, o które prosiłeś w fazie MVP, używając frameworka Django, Tailwind CSS (za pomocą CDN do szybkiego startu i pięknego wyglądu), oraz bazy SQLite. Wykresy są generowane przy użyciu Chart.js.

Co zostało zrobione:
1. Rejestracja i autoryzacja (users app)
Skonfigurowano CustomUser (co pozwala w przyszłości na łatwą modyfikację i rozbudowę profilu użytkownika).
Przygotowano piękne, ostylowane Tailwindem formularze logowania i rejestracji.
2. Śledzenie Finansów (tracker app)
Modele bazy danych:
Category (z polem określającym typ: Przychód / Wydatek).
Transaction (przypisane do konkretnej Kategorii i Użytkownika, z kwotą, datą i opisem).
Dashboard:
Automatycznie oblicza i wyświetla łączny przychód, łączne wydatki oraz obecny bilans.
Generuje piękny interaktywny wykres kołowy (Doughnut Chart) prezentujący rozkład wydatków na różne kategorie.
Tabela z najnowszymi 5 transakcjami.
Dodawanie Wydatków / Przychodów:
Dostępny jest dynamiczny formularz umożliwiający dodanie nowej transakcji wraz z odpowiednią kategorią i wyborem daty.
Jak zacząć testowanie?
Serwer Django został właśnie uruchomiony w tle!

Otwórz w przeglądarce adres: http://127.0.0.1:8000/
Zostaniesz automatycznie przekierowany do formularza logowania.
Ponieważ nie masz jeszcze konta, kliknij w "Zarejestruj się".
Po pomyślnej rejestracji, zostaniesz automatycznie zalogowany i powita Cię Dashboard.
(Opcjonalnie) Możesz wejść do Panelu Admina pod adresem http://127.0.0.1:8000/admin/ (najpierw musisz utworzyć superużytkownika w terminalu poleceniem python manage.py createsuperuser, ale nie jest to wymagane do podstawowego testowania jako zwykły użytkownik).
TIP

Zanim zaczniesz dodawać transakcje w aplikacji, system poprosi Cię o przypisanie im Kategorii. Aby je mieć, najprościej wejść w Panel Admina i dodać kilka kategorii (np. "Jedzenie" jako Wydatek, "Wypłata" jako Przychód), lub dodać je z poziomu kodu konsoli (ponieważ w MVP jeszcze nie zaimplementowaliśmy formularza dodawania kategorii na frontendzie, a jedynie transakcji z istniejących kategorii).
Aby samodzielnie uruchomić aplikację w przyszłości, wykonaj następujące kroki w terminalu (będąc w głównym folderze projektu D:\Python\Pyton-django):

  1. Aktywuj środowisko wirtualne (Virtual Environment)
  W systemie Windows użyj polecenia:
   1 .\venv\Scripts\activate

  2. Uruchom serwer deweloperski
  Gdy środowisko jest aktywne, wpisz:

   1 python manage.py runserver

  3. Otwórz przeglądarkę
  Aplikacja będzie dostępna pod adresem:
  http://127.0.0.1:8000/ (http://127.0.0.1:8000/)

  ---

  Dodatkowe przydatne polecenia:
   * Tworzenie konta administratora: Jeśli chcesz wejść do panelu /admin, musisz najpierw stworzyć superużytkownika:

   1     python manage.py createsuperuser
   * Zamykanie serwera: W terminalu, w którym działa serwer, naciśnij Ctrl + C.
   * Aktualizacja bazy danych: Jeśli zmienisz coś w modelach, uruchom:

   1     python manage.py makemigrations
   2     python manage.py migrate


