import requests
from bs4 import BeautifulSoup
import json

def scrapuj_dane(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f'Nie udało się pobrać strony. Kod odpowiedzi: {response.status_code}')
        return None

def analizuj_strone(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    # Znajdź sekcję z postaciami
    sekcje_postaci = soup.find_all('div', class_='unit-card-grid__cell js-unit-search__result')
    
    # Inicjalizacja listy na postacie
    postacie = []
    
    # Przetwarzanie każdej postaci
    for sekcja in sekcje_postaci:
        nazwa_postaci = sekcja.find('div', class_='unit-card__name').text.strip()
        
        # Sprawdź, czy istnieje element z klasą 'relic-badge'
        poziom_reliktu_elem = sekcja.find('div', class_='relic-badge')
        poziom_reliktu = poziom_reliktu_elem.text.strip() if poziom_reliktu_elem else 'Nieokreślony'
        
        # Sprawdź, czy istnieje element z klasą 'character-portrait__zeta'
        poziom_zeta_elem = sekcja.find('div', class_='character-portrait__zeta')
        poziom_zeta = poziom_zeta_elem.text.strip() if poziom_zeta_elem else 'Nieokreślony'
        
        # Pobierz procent ukończenia, jeśli istnieje
        procent_ukonczenia_elem = sekcja.find('div', class_='progress-bar')
        procent_ukonczenia = procent_ukonczenia_elem['style'].split(':')[-1].strip('%;') if procent_ukonczenia_elem else 'Nieokreślony'
        
        # Dodawanie informacji o postaci do listy
        postacie.append({
            'nazwa': nazwa_postaci,
            'poziom_reliktu': poziom_reliktu,
            'poziom_zeta': poziom_zeta,
            'procent_ukonczenia': procent_ukonczenia
        })
    
    return postacie

if __name__ == '__main__':
    url = 'https://swgoh.gg/p/172597111/characters'
    html = scrapuj_dane(url)
    if html:
        postacie = analizuj_strone(html)
        
        # Konwertuj obiekty BeautifulSoup na standardowe typy Pythona
        postacie_jsonable = []
        for postac in postacie:
            postacie_jsonable.append({
                'nazwa': postac['nazwa'],
                'poziom_reliktu': postac['poziom_reliktu'],
                'poziom_zeta': postac['poziom_zeta'],
                'procent_ukonczenia': postac['procent_ukonczenia']
            })
        
        # Zapisz wyniki do pliku JSON
        with open('postacie.json', 'w', encoding='utf-8') as plik:
            json.dump(postacie_jsonable, plik, ensure_ascii=False, indent=4)
        
        print('Dane o postaciach zapisane do pliku postacie.json')