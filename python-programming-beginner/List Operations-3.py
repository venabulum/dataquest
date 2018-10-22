## 2. Parsing the File ##

weather_data = []
rows = open('la_weather.csv', 'r').read().split('\n')
for r in rows:
    weather_data.append(r.split(','))
print(weather_data)

## 3. Getting a Single Column From the Data ##

# weather_data has already been read in automatically to make things easier.
weather = []

for row in weather_data:
    weather.append(row[1])

## 4. Counting the Items in a List ##

count = 0

for row in weather:
    count = count + 1

## 5. Removing the Header ##

new_weather = weather[1:366]

## 6. The In Statement ##

animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]

cat_found = "cat" in animals
space_monster_found = "space_monster" in animals

## 7. Weather Types ##

weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
weather_type_found = []

for item in weather_types:
    weather_type_found.append(item in new_weather)