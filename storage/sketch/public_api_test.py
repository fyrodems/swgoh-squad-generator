import requests

# URL publicznego API
url = "https://swgoh.gg/api/player/172597111"

# Parametry zapytania
params = {
    'parametr': 'wartość'
}

# Wykonanie zapytania GET
response = requests.get(url)

# Sprawdzenie odpowiedzi
if response.status_code == 200:
    print("Zapytanie działa. Odpowiedź:")
    print(response.json())  # Jeśli odpowiedź jest w formacie JSON
else:
    print(f"Zapytanie nie działa. Kod odpowiedzi: {response.status_code}")