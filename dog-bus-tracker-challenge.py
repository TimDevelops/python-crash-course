# 🐾 Dog Bus Tracker — Challenge Steps
#
# 1. Start with a bus dictionary holding current passengers.
#    - Each seat number (1, 2, 3, ...) is a key
#    - Each value is another dictionary with each pet's:
#        • name
#        • breed
#        • pickup time
#        • dropoff time

bus = {
    "1": {
        "name" : "rufus",
        "breed" : "pitbull",
        "pickup" : "9am",
        "dropoff" : "11am",
    },
    "2": {
            "name" : "dudley",
            "breed" : "chiuauah",
            "pickup" : "9am",
            "dropoff" : "3pm",
        },
    "3": {
            "name" : "tommy",
            "breed" : "german shephard",
            "pickup" : "9am",
            "dropoff" : "3pm",
        }
}
#
# 2. Print a starting roster showing each pet’s seat, name, and pickup time.
print(f"======== STARTING SEAT ROSTER ========")

for seat,pet in bus.items():
    name = pet['name']
    breed = pet['breed']
    pickup = pet['pickup']
    dropoff = pet['dropoff']
    print(f"\nSeat #{seat}\n\tName: {name.title()}\n\tBreed: {breed.title()}\n\tPickup Time: {pickup}")
#
# 3. Add one new pet if there’s room on the bus.  
#    - Use MAX_SEATS to limit capacity.  
#    - Dynamically assign the next seat number.  
#    - Print the updated roster showing all pets after pickup.  
#
# if len(bus) < 4:

#     dog_name = input("What is your dog's name? ")
#     breed = input("What is your dog's breed? ")
#     pickup = 900
#     dropoff = int((input("What time do they need to be dropped off? (military time): ")))
#     bus.update({'4': {
#         'name':{dog_name},'breed':{breed},'pickup':{pickup},'dropoff':{dropoff} }
#         })

# else:
#     print(f"The bus is full at {len(bus)} seats")

# for key,value in bus.items():
#     print(f"Seat #{key} {value}")

# 4. Ask which pet leaves early.  
#    - Remove that pet from the bus.  
#    - Print a message saying they’ve headed home.  
#
# early_dog = input("What is the seat of the dog that leaves early? ")
# del bus['1']
# print(f"{early_dog} has left early")

# 5. Print a final roster listing the remaining pets and their dropoff times.  

# for key,value in bus.items():
#     print(f"Seat #{key} {value}")