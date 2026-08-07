person_1 = {
    'first name':'Tana',
    'last name':'Greer',
    'age':28,
    'city':'Conroe'
}
for key,value in person_1.items():
    print(key.title(), value)


favorite_numbers = {
    'Tom':5,
    'Jim':4,
    'Bro':7,
    'Bob':10,
    'Billy':12,
}

print(favorite_numbers['Tom'])
print(favorite_numbers['Jim'])
print(favorite_numbers['Bro'])
print(favorite_numbers['Bob'])
print(favorite_numbers['Billy'])

glossary = {
    'dictionaries':'stores key/value pairs',
    'strings':'text in Python',
    'integers':'numbers in Python',
    'if-elif-else':'if this, then this.. elif this, then this.. else this',
    'while':'while this happens (or is true) then do this',
}

print(f"Dictionaries:\n{glossary['dictionaries']}\n")
print(f"Strings:\n{glossary['strings']}\n")
print(f"Integers:\n{glossary['integers']}\n")
print(f"If-Elif-Else:\n{glossary['if-elif-else']}\n")
print(f"While:\n{glossary['while']}\n")
