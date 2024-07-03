import requests
from bs4 import BeautifulSoup
import json

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f'Failed to fetch the page. Response code: {response.status_code}')
        return None

def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find the section with characters
    character_sections = soup.find_all('div', class_='unit-card-grid__cell js-unit-search__result')
    
    # Initialize list for characters
    characters = []
    
    # Process each character
    for section in character_sections:
        character_name = section.find('div', class_='unit-card__name').text.strip()
        
        # Check if 'relic-badge' element exists
        relic_level_elem = section.find('div', class_='relic-badge')
        relic_level = relic_level_elem.text.strip() if relic_level_elem else 'Undefined'
        
        # Check if 'character-portrait__zeta' element exists
        zeta_level_elem = section.find('div', class_='character-portrait__zeta')
        zeta_level = zeta_level_elem.text.strip() if zeta_level_elem else 'Undefined'
        
        # Check if level element exists
        level_elem = section.find('div', class_='character-portrait__level')
        level = level_elem.text.strip() if level_elem else 'Undefined'
        
        # Get completion percentage if available
        completion_elem = section.find('div', class_='progress-bar')
        completion_percentage = completion_elem['style'].split(':')[-1].strip('%;') if completion_elem else 'Undefined'
        
        # Get gear level if available
        gear_elem = section.find('div', class_='character-portrait__gframe')
        gear_level = gear_elem['class'][-1].split('-')[-1] if gear_elem else 'Undefined'

        # Count number of stars if available
        stars_elem = section.find_all('div', class_='rarity-range__star')
        stars_count = len(stars_elem)
        
        # Add character information to the list
        characters.append({
            'name': character_name,
            'relic_level': relic_level,
            'zeta_level': zeta_level,
            'level': level,
            'completion_percentage': completion_percentage,
            'gear_level': gear_level,
            'stars_count': stars_count
        })
    
    return characters

if __name__ == '__main__':
    url = 'https://swgoh.gg/p/172597111/characters'
    html = fetch_data(url)
    if html:
        characters = parse_page(html)
        
        # Convert BeautifulSoup objects to standard Python types
        characters_jsonable = []
        for character in characters:
            characters_jsonable.append({
                'name': character['name'],
                'relic_level': character['relic_level'],
                'zeta_level': character['zeta_level'],
                'level': character['level'],
                'completion_percentage': character['completion_percentage'],
                'gear_level': character['gear_level'],
                'stars_count': character['stars_count']
            })
        
        # Save results to JSON file
        with open('characters.json', 'w', encoding='utf-8') as file:
            json.dump(characters_jsonable, file, ensure_ascii=False, indent=4)
        
        print('Character data saved to characters.json file')