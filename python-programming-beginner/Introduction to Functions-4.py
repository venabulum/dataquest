## 1. Overview ##

data = open('movie_metadata.csv', 'r').read().split('\n')
movie_data = []
for row in data:
    movie_data.append(row.split(','))

print(movie_data[0:6])

## 3. Writing Our Own Functions ##

def first_elts(input_lst):
    movies = []
    for row in input_lst:
        movies.append(row[0])
    return movies

movie_names = first_elts(movie_data)
print(movie_names[0:6])

## 4. Functions with Multiple Return Paths ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def is_usa(movie):
    if movie[len(movie)-2] == "USA":
        return True
    else:
        return False

wonder_woman_usa = is_usa(wonder_woman)

## 5. Functions with Multiple Arguments ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def is_usa(input_lst):
    if input_lst[6] == "USA":
        return True
    else:
        return False
    
    
def index_equals_str(i_list, i_index, i_string):
    if i_list[i_index] == i_string:
        return True
    else:
        return False

index_equals_str(i_index = 4, i_string = "English", i_list = "wonder_woman")

wonder_woman_in_color = index_equals_str(wonder_woman, 2, "Color")
print(wonder_woman_in_color)

## 6. Optional Arguments ##

def index_equals_str(input_lst,index,input_str):
    if input_lst[index] == input_str:
        return True
    else:
        return False
def counter(input_lst,header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        num_elt = num_elt + 1
    return num_elt

def feature_counter(i_list, i_index, i_string, header_row = False):
    count = 0
    if header_row == True:
        i_list = i_list[1:len(i_list)]
    for row in i_list:
        if row[i_index] == i_string:
            count = count + 1
    return count

num_of_us_movies = feature_counter(movie_data, 6, "USA", header_row = True)
print(num_of_us_movies)

## 7. Calling a Function inside another Function ##

def feature_counter(input_lst,index, input_str, header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        if each[index] == input_str:
            num_elt = num_elt + 1
    return num_elt

def summary_statistics(data):
    num_japan_films = (feature_counter(movie_data, 6, "Japan", header_row = True))
    num_color_films = (feature_counter(movie_data, 2, "Color", header_row = True))
    num_films_in_english = (feature_counter(movie_data, 5, "English", header_row = True))
    sum = {}
    sum["japan_films"] = num_japan_films
    sum["color_films"] = num_color_films
    sum["films_in_english"] = num_films_in_english
    return sum
    
summary = summary_statistics(movie_data)