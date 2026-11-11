#TODO: MUST RETURN BACK TO INITIAL CITY

from math import sqrt
import random

class City():
    name = None
    X = 0
    Y = 0

    def __init__(self, name, _x, _y):
        self.name = name
        self.X = _x
        self.Y = _y

class Pairing():
    city_one = None
    city_two = None
    distance = None

    def __init__(self, city_one: City, city_two: City):
        self.change_cities(city_one, city_two)

    def change_cities(self, city_one: City, city_two: City):
        self.city_one = city_one
        self.city_two = city_two

        self.distance = sqrt((city_two.X - city_one.X) ** 2 + (city_two.Y - city_one.Y) ** 2)


def mutate(cities, _pairings):

    i, j = random.sample(range(len(cities)), 2)  # two different indices
    cities[i], cities[j] = cities[j], cities[i]

    _pairings.clear()
    for x in range(len(cities) - 1):
        pairings.append(Pairing(cities[x], cities[x+1]))

bristol = City("Bristol", 30, 60)
london = City("London", 40, 80)
bath = City("Bath", -30, 0)
cardiff = City("Cardiff", 45, 60)
brum = City("Birmingham", 22, 90)


all_cities =  [bristol, london, bath, cardiff, brum]

pairings = []

for x in range(len(all_cities) - 1):
    pairings.append(Pairing(all_cities[x], all_cities[x+1]))


best_total_distance = float('inf')

worst_total_distance = float('-inf')

counter = 10000
while counter > 0:
    current_distance = 0
    for x in pairings:
        current_distance += x.distance

    best_total_distance = min(best_total_distance, current_distance)
    worst_total_distance = max(worst_total_distance, current_distance)

    mutate(all_cities, pairings)
    counter -= 1

print(best_total_distance)
print("-")
print(worst_total_distance)