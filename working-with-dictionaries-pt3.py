############# 6-7. People 

person_1 = {
    'first name':'Jill',
    'last name':'Mani',
    'age':25,
    'city':'Miami'
}
person_2 = {
    'first name':'Trey',
    'last name':'Liz',
    'age':15,
    'city':'Manhattan'
}
person_3 = {
    'first name':'Billy',
    'last name':'Bob',
    'age':43,
    'city':'Austin'
}

people=[person_1, person_2, person_3]

person_4 = {
    'first name':'Jeff',
    'last name':'Bing',
    'age':60,
    'city':'Melbourne'
}
people.append(person_4)

for person in people:
    name = f"{person['first name']} {person['last name']}"
    age = person['age']
    city = person['city']
    print(f"{name} is {age} years old and lives in {city}")


############ 6-8. Pets

pet1 = {
    'animal':'dog',
    'name':'bruce',
    'owner':'billy bob',
    'gender':'male',
}
pet2 = {
    'animal':'cat',
    'name':'minnie',
    'owner':'henry cavil',
    'gender':'female',
}
pet3 = {
    'animal':'monkey',
    'name':'george',
    'owner':'yellow hat guy',
    'gender':'male',
}

pets = [pet1, pet2, pet3]

new_animal = input(f"\nWhat kinda of animal do you have? ").lower()
new_gender = input(f"\nWhat gender are they? (male/female) ").lower()

if new_gender == 'male':
    new_name = input(f"\nWhat's his name? ").lower()
else:
    new_name = input(f"\nWhat's her name? ").lower()

new_owner = input(f"\nWhat's your name? ").lower()

pet4 = {
    'animal':new_animal,
    'name':new_name,
    'owner':new_owner,
    'gender':new_gender,
}

pets.append(pet4)

i = 0
for pet in pets:
    animal = pet['animal']
    name = pet['name']
    owner = pet['owner']
    i += 1
    if pet['gender'] == 'male':
        print(f"\n{i}. {name.title()} is a {animal}.\n\tHis owner is {owner.title()}.")
    else:
        print(f"\n{i}. {name.title()} is a {animal}.\n\tHer owner is {owner.title()}.")


############ 6-9. Favorite Places

# favorite_places = {
#     'bob':['colorado','hawaii','new york','florida'],
#     'tina':['disney','mckinney','breckenridge'],
#     'bobbat':['home','gigi\'s house'],
# }

# for name,places in favorite_places.items():
#     print(f"\n{name.title()}'s favorite places are:")
#     for place in places:
#         print(f"\t\u2022 {place.title()}")

############ 6-10. Favorite Numbers

# favorite_numbers = {
#     'Tom':[5,10],
#     'Jim':[4,6,8],
#     'Bro':[27],
#     'Bob':[10,50],
#     'Billy':[12],
# }

# for name,numbers in favorite_numbers.items():
#     if len(numbers) > 1:
#         print(f"\n{name.title()}'s favorite numbers are: ")
#     else:
#         print(f"\n{name.title()}'s favorite number is: ")

#     for number in numbers:
#         print(f"\t{number}")

############ 6-11. Cities

# cities = {
#     'houston':{
#         'country':'the united states',
#         'population':'2.4 million',
#         'fact':'is the most ethinically diverse city in the USA'
#     },
#     'zürich':{
#         'country':'switzerland',
#         'population':'436,551',
#         'fact':'has over 1,200 public fountains'
#     },
#     'melbourne':{
#         'country':'australia',
#         'population':'5.5 million',
#         'fact':'was originally named Batmania after being founded by John Batman'
#     }
# }

# for city,info in cities.items():
#     country = info['country']
#     population = info['population']
#     fact = info['fact']
#     print(f"\nThe city of {city.title()} is located in {country.title()} with a population of {population}.\n\tFun fact: {city.title()} {fact}!")


############ 6-12. Extensions

