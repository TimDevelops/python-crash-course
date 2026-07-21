# 1. Add new print statement - on a new line
#    which says 'We hear you like the color xxx! xxx is a string with color 
# 2. extend the function with another  input parameter 'color', that defaults to 'red'
# 3. Capture the color via an input box as variable:color 
# 4. Change the 'You are xx!' text to say 'you will be xx+1 years old next birthday 
#  adding 1 to the age
# 5. Capitalize first letter of the 'name', and rest are small caps 
# 6. Favorite color should be in lowercase 

def greeting(name,age=28,color="red"):
    print(f"Hello {name.capitalize()}!\nYou will be {age + 1} years old next year!")
    print(f"We hear your favorite color is {color.lower()}!")


name = input("Enter your name: ").title()
age = input("Enter your age: ")
color = input("What's your favorite color? ").lower()
greeting(name,int(age),color)