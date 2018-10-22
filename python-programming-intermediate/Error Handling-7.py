## 2. Sets ##

gender = []
for row in legislators:
    gender.append(row[3])
    
gender = set(gender)
print(gender)

## 3. Exploring the Dataset ##

party = []
for row in legislators:
    party.append(row[6])

party = set(party)
print(party)
# print(legislators)

## 4. Missing Values ##

for row in legislators:
    if row[3] == '':
        row[3] = 'M'
        
print(legislators)

## 5. Parsing Birth Years ##

birth_years = []
for row in legislators:
    parts = row[2].split('-')
    birth_years.append(parts[0])
    
print(birth_years)

## 6. Try/except Blocks ##

try:
    float('hello')
except Exception:
    print('Error converting to float.')

## 7. Exception Instances ##

try:
    int('')
except Exception as err:
    print(type(err))
    print(str(err))

## 8. The Pass Keyword ##

converted_years = []

for year in birth_years:
    try:
        int_year = int(year)
        converted_years.append(int_year)
    except:
        pass

## 9. Convert Birth Years to Integers ##

for item in legislators:
    try:
        date = item[2].split('-')
        birth_year = int(date[0])
    except Exception:
        birth_year = 0
    item.append(birth_year)
    
print(legislators)


## 10. Fill in Years Without a Value ##

for row in legislators:
    if row[7] != 0:
        last_value = row[7]
    if row[7] == 0:
        row[7] = last_value
        
print(legislators)