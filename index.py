# aliens = []

# for alien in range(30):
#     new_alien = {'color':'green','points':5,'speed':'slow'}
#     aliens.append(new_alien)

# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10

# for alien in aliens[:5]:
#     print(alien)
# print("...")

# pizza = {
#     'crust' : 'stuffed',
#     'toppings' : ['cheese','peppironni','marina sauce'],
#     'side' : 'ranch'
# }

# print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

# for topping in pizza['toppings']:
#     print(f"\t{topping}")

# favorite_languages = {
#     'jen' : ['python','ruby'],
#     'james' : ['c'],
#     'billy' : ['html','css','js'],
# }

# for name,languages in favorite_languages.items():
#     if len(languages) > 1:
#         print(f"\n{name.title()}'s favorite languages are:")
#         for language in languages:
#             print(f"\t{language.title()}")
#     else:
#         print(f"\n{name.title()}'s favorite language is:")
#         for language in languages:
#             print(f"\t{language.title()}")

users = {
    'tgreer': {
        'firstname':'timmy',
        'lastname':'greer',
        'id_number':123
    },
    'bbob': {
        'firstname':'billy',
        'lastname':'bob',
        'id_number':321
    },
}

for user,info in users.items():
    print(f"\nUsername: {user}")
    full_name = f"{info['firstname']} {info['lastname']}"
    id_number = info['id_number']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tID Number: {id_number}")