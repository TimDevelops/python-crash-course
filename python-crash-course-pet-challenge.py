# Make several dictionaries, where each dictionary represents a different pet. 
# In each dictionary, include the kind of animal and the owner’s name.
# Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.

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

print(f"\n\n============= CURRENT PET ROSTER =============")

def roster():
    i = 0
    for pet in pets:
        i += 1
        animal = pet['animal']
        name = pet['name']
        owner = pet['owner']
        gender = pet['gender']
        print(f"\nPet #{i}:\nName: {name.title()}\nAnimal: {animal}\nOwner: {owner.title()}\nGender: {gender}")

roster()

print(f"\n**Please answer the following questions**")

while True:
    new_owner = input(f"\nWhat's your name? (type 'done' to quit)\n").lower()

    if new_owner == 'done':
        break

    new_animal = input(f"\nWhat kinda of animal do you have?\n").lower()
    new_gender = input(f"\nWhat gender are they? (male/female)\n").lower()

    if new_gender == 'male':
        new_name = input(f"\nWhat's his name?\n").lower()
    else:
        new_name = input(f"\nWhat's her name?\n").lower()

    new_pet = {
        'animal':new_animal,
        'name':new_name,
        'owner':new_owner,
        'gender':new_gender,
    }

    pets.append(new_pet)

print(f"\n\n============= NEW PET ROSTER =============")


roster()

print(f"\n=============================================")

def animal_owner():
    i = 0
    for pet in pets:
        animal = pet['animal']
        name = pet['name']
        owner = pet['owner']
        gender = pet['gender']
        i += 1
        if pet['gender'] == 'male':
            print(f"\n{i}. {name.title()} is a {gender} {animal}.\n\tHis owner is {owner.title()}.")
        else:
            print(f"\n{i}. {name.title()} is a {gender} {animal}.\n\tHer owner is {owner.title()}.")

animal_owner()

print(f"\n=====================END========================\n\n")
