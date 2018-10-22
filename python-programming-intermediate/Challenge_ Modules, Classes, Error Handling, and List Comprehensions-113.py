## 2. Introduction to the Data ##

import csv

f = open('nfl_suspensions_data.csv', 'r')
nfl_suspensions = list(csv.reader(f))
nfl_suspensions = nfl_suspensions[1:]
    
years = {}
for row in nfl_suspensions:
    row_year = row[5]
    if row_year in years:
        years[row_year] = years[row_year] + 1
    else:
        years[row_year] = 1

print(years)

## 3. Unique Values ##

teams = [ row[1] for row in nfl_suspensions ]
unique_teams = set(teams)
games = [ row[2] for row in nfl_suspensions ]
unique_games = set(games)
print(unique_teams)
print(unique_games)

## 4. Suspension Class ##

class Suspension:
    def __init__(self, row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        self.year = row[5]
        
third_suspension = Suspension(nfl_suspensions[2])
print(third_suspension.year)

## 5. Tweaking the Suspension Class ##

class Suspension():
    def __init__(self, row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        
        try:
            self.year = int(row[4])
        except Exception:
            self.year = 0
            
    def get_year(self):
        return self.year
        

missing_year = Suspension(nfl_suspensions[23])
twenty_third_year = missing_year.get_year()