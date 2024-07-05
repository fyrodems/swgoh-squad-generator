import json
from itertools import combinations

# Funkcja wczytująca dane postaci z pliku JSON
def wczytaj_dane_z_json(nazwa_pliku):
    with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
        dane = json.load(plik)
    return dane

# Funkcja doboru najlepszego składu na podstawie zadanych kryteriów
def dobierz_najlepszy_sklad(postacie, kryteria):
    najlepszy_sklad = []
    najlepszy_wynik = 0
    
    # Generowanie wszystkich możliwych kombinacji składów o różnej długości
    for dlugosc_składu in range(1, len(postacie) + 1):
        for kombinacja in combinations(postacie, dlugosc_składu):
            if spelnia_kryteria(kombinacja, kryteria):
                wynik = ocen_sklad(kombinacja, kryteria)
                if wynik > najlepszy_wynik:
                    najlepszy_wynik = wynik
                    najlepszy_sklad = kombinacja
    
    return najlepszy_sklad, najlepszy_wynik

# Funkcja sprawdzająca czy dana kombinacja postaci spełnia zadane kryteria
def spelnia_kryteria(kombinacja, kryteria):
    # Przykładowe kryteria: minimalna liczba gwiazdek, wysoki poziom reliktów, itp.
    min_gwiazdek = kryteria.get('min_gwiazdek', 5)
    min_reliktow = kryteria.get('min_reliktow', 2)
    
    for postac in kombinacja:
        if postac['stars_count'] < min_gwiazdek or int(postac['relic_level']) < min_reliktow:
            return False
    
    return True

# Funkcja oceniająca skład na podstawie zadanych kryteriów
def ocen_sklad(kombinacja, kryteria):
    # Przykładowe ocenianie składu: sumowanie wartości zmiennych, algorytm heurystyczny, itp.
    suma_ocen = 0
    for postac in kombinacja:
        suma_ocen += postac['stars_count'] * int(postac['relic_level'])
    
    return suma_ocen

# Przykładowe użycie
if __name__ == '__main__':
    # Wczytanie danych postaci z pliku JSON
    postacie = wczytaj_dane_z_json('characters.json')
    
    # Przykładowe kryteria doboru składu
    kryteria = {'min_gwiazdek': 5, 'min_reliktow': 5}
    
    # Dobranie najlepszego składu
    najlepszy_sklad, wynik_oceny = dobierz_najlepszy_sklad(postacie, kryteria)
    
    # Wyświetlenie najlepszego składu i wyniku oceny
    print("Najlepszy skład:")
    for postac in najlepszy_sklad:
        print(f"- {postac['name']} (Gwiazdki: {postac['stars_count']}, Relikty: {postac['relic_level']})")
    print(f"Wynik oceny: {wynik_oceny}")