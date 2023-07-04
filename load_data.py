import requests
API_KEY = "40cee4db8217f46fc5bfb315b7293e81"
city_name = "London"
url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_KEY}"

response = requests.get(url=url)

print(response.content)
