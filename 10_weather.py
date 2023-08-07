import requests
answer = requests.get("https://www.7timer.info/bin/astro.php?lon=113.2&lat=23.1&ac=0&unit=metric&output=json&tzshift=0")
weather = answer.json()
#print(weather)
print("direction\tspeed")
for d in weather.get('dataseries'):
    inner_d = d['wind10m']
    print(f"{inner_d['direction']}\t\t{inner_d['speed']}")


