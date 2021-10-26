import json
import hashlib


# 1
class Myrange:
    def __init__(self, path):
        self.file = path
        with open(self.file) as f:
            self.countries_list = json.load(f)
        self.x = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.x == len(self.countries_list):
            raise StopIteration
        self.country_name = self.countries_list[self.x]['name']['official']
        self.x += 1
        return self.country_name


country = Myrange('countries.json')

with open('country_link.txt', 'w', encoding='utf-8') as f:
    for item in country:
        data = f'{item} - https://en.wikipedia.org/wiki/{item.replace(" ", "_")}\n'
        f.write(data)


# 2
with open('country_link.txt') as f:
    x = [hashlib.md5(item.encode()).hexdigest() for item in f]
    print(x)
