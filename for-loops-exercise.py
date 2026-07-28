names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']

# Party invitation
# print out invitations for each friend using for loop
# Add 2 extra names to the list using input boxes when running code
# print out 1 invitation to each friend per line
# names should be properly capitalized
# hint: may need 2 for loops to solve this exercise

# 1st attempt: SUCCESSFUL, but could be better
# input1 = input("Enter a name: ")
# input2 = input("Enter another name: ")
# names.append(input1)
# names1.append(input2)

# all_names = names + names1

# for name in all_names:
#     print(f"{name.title()}! You are invited to the party on Saturday!")


msg = 'You are invited to the party on Saturday!'
names.extend(names1)

for index in range(2):
    names.append(input('Enter a name name: '))

for name in names:
    print(f'{name.title()}! {msg}')