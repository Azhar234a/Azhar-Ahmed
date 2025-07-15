import requests
api_key = "your_api_key"
city = "Sanaa"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)
data = response.json()

print(data['main']['temp'])