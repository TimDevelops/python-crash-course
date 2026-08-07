# glossary = {
#     'dictionaries':'stores key/value pairs',
#     'strings':'text in Python',
#     'integers':'numbers in Python',
#     'if-elif-else':'if this, then this.. elif this, then this.. else this',
#     'while':'while this happens (or is true) then do this',
# }

# glossary['sets'] = "sorta like a list but has curly brackets {} and isn't ordered"
# glossary['for'] = "a type of loop that can loop through a set of data until it finishes"
# glossary['functions'] = "can be used to define something and then called on later"

# for key, value in glossary.items():
#     print(f"{key.title()} - {value}.")

# rivers = {
#     'nile river' : 'egypt',
#     'amazon river' : 'south america',
#     'yangtze river' : 'asia'
# }

# for key, value in rivers.items():
#     print(f"The {key.title()} runs through {value.title()}.")

# for river in rivers.keys():
#     print(f"\n{river.title()}")

# for country in rivers.values():
#     print(f"\n{country.title()}")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'penny': 'cobalt'
}
poll_list = ['jen','mike','joe','sarah','billy','bob','alex','penny']

for name in poll_list:
    print(f"Hi {name.title()}, we think you should take this poll on which programming language is your favorite!\n")

for name in poll_list:
    if name in favorite_languages.keys():
        print(f"{name.title()}, thank you so much for taking the poll!")
    else:
        print(f"{name.title()}, please take the poll!")
 