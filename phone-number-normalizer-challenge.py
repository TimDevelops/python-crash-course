# 📱 Phone Number Formatter
#
# 1. Ask the user to enter a U.S. phone number in **any format**.
# 2. Use .strip() to remove any leading/trailing spaces.
# 3. Replace common separators (-, (, ), .) with spaces.
# 4. Use .split() to break into chunks, then .join() to merge the digits.
# 5. Check if the cleaned number has **exactly 10 digits**.
# 6. If yes, format it like this: (123) 456-7890
# 7. If not, print an error message: "Please enter exactly 10 digits."

phone_number = input("Enter a U.S. phone number (10 digits): ").strip()

phone_number = ''.join(phone_number.split('-'))
phone_number = ''.join(phone_number.split('('))
phone_number = ''.join(phone_number.split(')'))
phone_number = ''.join(phone_number.split('.'))
phone_number = ''.join(phone_number.split(' '))

num_list = list(phone_number)

num1 = "".join(num_list[:3])
num2 = "".join(num_list[3:6])
num3 = "".join(num_list[6:])

if len(num_list) == 10:
     print(f'Formatted number: ({num1}) {num2}-{num3}')
else:
     print(f'Please enter exactly 10 digits.')