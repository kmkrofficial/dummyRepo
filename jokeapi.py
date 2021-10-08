import requests


r = requests.get("https://v2.jokeapi.dev/joke/Programming")
print(r.json()['setup'], r.json()['delivery'])