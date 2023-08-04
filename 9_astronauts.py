import requests
# request the names of the astronauts from the provided url
people = requests.get("http://api.open-notify.org/astros.json")
# save the request with the name people***
people_json = people.json()
# print the names of the people in json

print("name\t|\tcraft")
for d in people_json["people"]:   
    print(f"{d['name']}\t|\t{d['craft'].upper()}")
