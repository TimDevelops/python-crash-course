# class Restaurant:
#     """A simple attempt to model a restaurant."""

#     def __init__(self,restaurant_name,cuisine_type):
#         """Initialize restaurant name and cuisine type."""
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         """Describes the name and cuisine type of restaurant."""
#         print(f"This restaurant's name is {self.restaurant_name}.\n\tThey serve {self.cuisine_type}.")

#     def open_restaurant(self):
#         print(f"{self.restaurant_name} is open for business!")

#     def closed_restaurant(self):
#             print(f"Unfortunately, {self.restaurant_name} is closed!")

# tim_burger = Restaurant("Tim's Burger Joint","American")
# joe_italian = Restaurant("Joe's Italian Meatball","Italian")
# veggie_house = Restaurant("Vegan House - Veggie's Only",'Vegan')
# tim_burger.describe_restaurant()
# joe_italian.describe_restaurant()
# veggie_house.describe_restaurant()

class Users:
    def __init__(self,first_name,last_name,employee_id,nickname,gender):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.nickname = nickname
        self.gender = gender

    def describe_user(self):
        print(f"Name: {self.first_name.title()} {self.last_name.title()}\nEmployee ID #: {self.employee_id}\nNickname: {self.nickname.title()}\nGender: {self.gender}")

    def greet_user(self):
        print(f"Greetings {self.first_name.title()}!\n\tOr should I say, {self.nickname.title()}.. It's nice to finally meet you!\n\tI know that you are {self.gender} and your employee ID is {self.employee_id}.")

user1 = Users('timothy','greer',123,'tim','man')
user2 = Users('billy','bob',654,'bill','man')
user3 = Users('james','craig',123,'jim','he')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()