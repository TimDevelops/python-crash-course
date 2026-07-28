# 🛂 Access Control Scanner Challenge
#
# 1. Create a set of revoked badge numbers.
# 2. Create two empty lists: "approved" and "denied".
# 3. Start a loop to collect visitor info:
#    - Ask for the visitor's name (or type "done" to finish).
#    - If the name is "done", exit the loop.
#    - Otherwise, ask for their badge number.
#    - Check if the badge is revoked:
#        • If revoked: add the name to "denied" and display "ACCESS DENIED".
#        • If not: add the name to "approved" and display "ACCESS GRANTED".
# 4. Print the final "Access Summary" for "✅ Approved Visitors" & "⛔️ Denied Visitors":
#    - Sort both lists alphabetically.
#    - Display the total number of approved and denied visitors.

revoked = {0, 111, 123, 999}
approved = []
denied = []

print(f"\n===== 🛂 Access Control Scanner Challenge =====")

while True:
    name = input(f'\nWhat is your name? (type "done" to finish): ')

    if name.lower() == 'done':
        break

    badge_num = int(input(f'\nWhat is your badge number? '))

    if badge_num in revoked:
        denied.append(name)
        print(f'\n::ACCESS DENIED::')

    else:
        approved.append(name)
        print(f'\n::ACCESS GRANTED::')

# print(f'\n✅ Approved Visitors: {sorted(approved)}\n\n⛔️ Denied Visitors: {sorted(denied)}\n\nTotal Number of Visitors: {len(approved + denied)}')

print(f"=== ACCESS SUMMARY ===")

print("✅ Approved Visitors")
for person in sorted(approved):
    print(f' - {person}')

print("⛔️ Denied Visitors")
for person in sorted(denied):
    print(f' - {person}')

print(f"Approved Visitors: {len(approved)}")
print(f"Denied Visitors: {len(denied)}")