from random import randint
from operator import itemgetter
from time import sleep
plays = {}
print('Rolling the Dice:')
for j in range(1, 5):
    plays[f'jogador{j}'] = randint(1, 6)
for k, v in plays.items():
    sleep(1)
    print(f'   O {k} got {v}')
podio = sorted(plays.items(), key=itemgetter(1), reverse=True)
print("Players' Ranking:")
for i, v in enumerate(podio):
    sleep(1)
    print(f'   {i+1}º place: {v[0]} got {v[1]}')