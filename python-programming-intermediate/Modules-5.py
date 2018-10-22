## 1. Introduction to Modules ##

import math
root = math.sqrt(99)
flr = math.floor(89.9)

## 2. Importing Using An Alias ##

import math as m
root = m.sqrt(33)

## 3. Importing A Specific Object ##

from math import *
root = math.sqrt(1001)

## 4. Variables Within Modules ##

import math

print(math.pi)
a = math.sqrt(math.pi)
b = math.ceil(math.pi)
c = math.floor(math.pi)

## 5. The CSV Module ##

import csv
temp = csv.reader(open('nfl.csv'))
nfl = list(temp)

## 6. Counting How Many Times a Team Won ##

import csv
f = open("nfl.csv", "r")
nfl = list(csv.reader(f))
patriots_wins = 0
for row in nfl:
    if "New England Patriots" in row[2]:
        patriots_wins = patriots_wins + 1 

## 7. Making a Function that Counts Wins ##

import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

# Define your function here.
def nfl_wins(team_name, list_name):
    wins = 0
    for row in list_name:
        if team_name in row[2]:
            wins =  wins + 1
    return wins

cowboys_wins = nfl_wins("Dallas Cowboys", nfl)
falcons_wins = nfl_wins("Atlanta Falcons", nfl)