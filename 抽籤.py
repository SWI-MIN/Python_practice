import random
import time

people = ['a','b','c','d','e','f','g','h','i']

for i in range(2):
    lucky = random.sample(people,9)
    random.shuffle(people)
    if i < 1:
        print('按造順序1~9份',lucky)
    else:
        print('恭喜你多做一份',people[0])