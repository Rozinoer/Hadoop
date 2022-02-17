#!/usr/bin/python3

import random as r

with open("creditData.txt", 'w') as file:
    for i in range(0,100,1):
        file.write(f'user{r.randint(0,100)},{r.randint(1000, 100000)},{r.randint(1,12)},bank{r.randint(1,10)}\n')

with open("customerData.txt", 'w') as file:
    gender = [
        "male",
        "female"
    ]
    for i in range(0,100,1):
        file.write(f'user{i},{r.choice(gender)},{r.randint(18,60)},{r.choice(["married","not married"])}\n')

with open("bankData.txt", 'w') as file:
    for i in range(0,10,1):
        file.write(f'bank{i},street{r.randint(0, 1000)}\n')
