import requests
from pprint import pprint

name_list = ['Hulk', 'Captain_America', 'Thanos']
id_list = []
intelligence_list = []
for name in name_list:
    def get_superHero_id(name_list):
        url = (f"https://superheroapi.com/api/2619421814940190/search/{name}")
        response = requests.get(url=url)
        data = dict(response.json())
        id = data['results'][0]['id']
        id_list.append(id)
        return response.json()

    get_superHero_id(name_list)


for id in id_list:
    def get_superHero_powerstats(id_list):
        url = (f"https://superheroapi.com/api/2619421814940190/{id}/powerstats")
        response = requests.get(url=url)
        data = dict(response.json())
        intell = data['intelligence']
        intelligence_list.append(intell)
        return response.json()

    get_superHero_powerstats(id_list)

superHero_intelligence = dict(zip(name_list, intelligence_list))
print(f'Самый умный супергерой - {max(superHero_intelligence)}.')
