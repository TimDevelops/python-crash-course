csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = ['Exercise: fill me with names']
print(friends_list)
# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise

# == Leaving this here to show how far I've come lol ==
# print(csv)
# csv = (csv.split(','))
# print(csv)
# csv = ",".join(csv)
# print(csv)
# csv = (csv.split(':'))
# print(csv)
# csv = ','.join(csv)
# print(csv)
# csv = (csv.split(';'))
# print(csv)
# csv = ','.join(csv)
# print(csv)
# csv = ''.join(csv)
# csv = csv.split(',')
# print(csv)

csv = ','.join(csv.split(':'))
csv = ','.join(csv.split(';'))
csv = csv.split(',')

friends_list = csv
print(friends_list)