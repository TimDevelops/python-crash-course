guest_list = ['Jensen', 'Jared', 'Tom', 'Henry']
guest_tom = guest_list.pop(2)
guest_list.insert(2, 'Michael')

print(f"=========== BEGINNING OF CODE ===========")

print(f"\nDear {guest_tom},\nWe are sorry you cannot make the dinner.")

guest_list_str = f"{', '.join(guest_list[:-1])}, & {guest_list[-1]}"

print(f"\n\nDear {guest_list_str},\n\nWe have just found out that we will be hosting even more guests!\n\nWe are excited about this change and hope you are looking forward to our dinner, as well.\n\nThank you!")

guest_list.insert(0, 'Bob')
guest_list.append('Tom')
guest_list.insert(3, 'Jerry')

print(f"\nHello {guest_list[0]}!\nPlease join me for a nice dinner, this evening @ 7pm.")
print(f"\nHello {guest_list[1]}\nPlease join me for a nice dinner, this evening @ 7pm.")
print(f"\nHello {guest_list[2]}\nPlease join me for a nice dinner, this evening @ 7pm.")
print(f"\nHello {guest_list[3]}!\nPlease join me for a nice dinner, this evening @ 7pm.")
print(f"\nHello {guest_list[4]}!\nPlease join me for a nice dinner, this evening @ 7pm.")
print(f"\nHello {guest_list[5]}!\nPlease join me for a nice dinner, this evening @ 7pm.")
print(f"\nHello {guest_list[6]}!\nPlease join me for a nice dinner, this evening @ 7pm.")

guest_bob = guest_list.pop(0)
print(f"\n\nDear {guest_bob}, I'm so sorry I can't invite you anymore.")

guest_jerry = guest_list.pop(2)
print(f"\n\nDear {guest_jerry}, I'm so sorry I can't invite you anymore.")

guest_michael = guest_list.pop(2)
print(f"\n\nDear {guest_michael}, I'm so sorry I can't invite you anymore.")

guest_henry = guest_list.pop(2)
print(f"\n\nDear {guest_henry}, I'm so sorry I can't invite you anymore.")

guest_tom = guest_list.pop(2)
print(f"\n\nDear {guest_tom}, I'm so sorry I can't invite you anymore.")

print(f"\n\nDear {guest_list[0]},\nYou're still invited!")
print(f"\n\nDear {guest_list[1]},\nYou're still invited!")

del guest_list[:2]
print(f"\n")
print(guest_list)
print(f"=========== END OF CODE ===========")