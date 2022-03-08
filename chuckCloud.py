import requests

response = requests.get(f"http://api.icndb.com/jokes/random")
unparsedChuck = response.json()
print(unparsedChuck)
joke = unparsedChuck["value"]["joke"]
joke = joke.replace('&quot;', '"')
print(joke)
