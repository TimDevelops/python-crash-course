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
print(f"\n\n======== STARTING SEAT ROSTER ========")

def roster():
    for seat,pet in bus.items():
        name = pet['name']
        breed = pet['breed']
        pickup = pet['pickup']
        dropoff = pet['dropoff']
        print(f"\nSeat #{seat}\n\tName: {name.title()}\n\tBreed: {breed.title()}\n\tPickup Time: {pickup}\n\tDropoff Time: {dropoff}")

roster()

#
# 3. Add one new pet if there’s room on the bus.  
#    - Use MAX_SEATS to limit capacity.  
#    - Dynamically assign the next seat number.  
#    - Print the updated roster showing all pets after pickup.  
#

MAX_SEATS = 5
i = 4
while len(bus) < MAX_SEATS:
    new_name = input(f"\nWhat's your pet's name?\n").lower()
    new_breed = input(f"\nWhat breed is your pet?\n").lower()
    pickup_time = input(f"\nAre you good with 9am pick? (yes or no)\n").lower()

    if pickup_time == "no":
        new_pickup = input(f"\nWhat pickup time would you like? (must be like '9am')\n").lower()
    else:
        new_pickup = "9am"

    new_dropoff = input(f"\nWhat drop off time would you like? (must be like '3pm')\n").lower()

    seat_number = str(i)

    bus.update({
        seat_number: {
            'name':new_name,
            'breed':new_breed,
            'pickup':new_pickup,
            'dropoff':new_dropoff,
        }
    })

    i += 1

if len(bus) > 5:
    print(f"\nWe're sorry, the bus is currently full!")

print(f"\n\n======== UPDATED SEAT ROSTER ========")


roster()
print(f"\n")


# 4. Ask which pet leaves early.  
#    - Remove that pet from the bus.  
#    - Print a message saying they’ve headed home.  
#
# early_dog = input("What is the seat of the dog that leaves early? ")
# del bus['1']
# print(f"{early_dog} has left early")

early_dropoff = []

for seat,pet in bus.items():
    if pet['dropoff'] != "3pm":
        print(f"\nSeat #{seat} is leaving at {pet['dropoff']}!")
        early_dropoff.append(seat)


for seat in early_dropoff:
    pet_leaving = bus.pop(seat)
    print(f"\n{pet_leaving['name'].title()} from Seat #{seat} has headed home!")


# 5. Print a final roster listing the remaining pets and their dropoff times.  

print(f"\n\n======== REMAINING AND FINAL SEAT ROSTER ========")


roster()