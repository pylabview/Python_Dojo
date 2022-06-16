# Assignment: User
# Author: Rodrigo Arguello
# Date: 06/15/2022

class User:
    def __init__(self, first_name, last_name, email, age) -> None:
        self.is_rewards_member = False
        self.gold_cards_points = 0
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        
    
    def display_info(self):
        print(f"************")
        print(f"User first name: {self.first_name}")
        print(f"User last name: {self.last_name}")
        print(f"User email: {self.email}") 
        print(f"User age: {self.age}")
        print(f"Is User a reward member: {self.is_rewards_member}")
        print(f"User cars points: {self.gold_cards_points}")
        print(f"************")

    def enroll(self):
        if self.is_rewards_member:
            print("User already a member.")
        else:
            self.is_rewards_member = True
            self.gold_cards_points = 200
#  Implement the spend_points(self, amount) method   
    def spend_points(self, amount):
        if amount < self.gold_cards_points:
            self.gold_cards_points-=amount

rod = User('Rodrigo', 'Arguello', 'rodrigo19662001@gmail.com', '45')

rod.display_info()

rod.enroll()
        
rod.display_info()

# Make 2 more instances of the User class.
jose = User('Jose', 'Frank', 'jose@gmail.com', '28')
martha = User('Martha', 'Smith', 'martha@gmail.com', '35')

# Have the first user spend 50 points
rod.spend_points(50)

# Have the second user enroll.
jose.enroll()
# Have the second user spend 80 points
jose.spend_points(80)
# Call the display method on all the users.
rod.display_info()
jose.display_info()
martha.display_info()

# BONUS: Implement the logic for testing if already a member and try to re-enroll the first user.
rod.enroll()

# BONUS: Implement the logic to prevent over-spending and call the spend_points method with 40 points on the 3rd user.
martha.enroll()

martha.spend_points(170)
martha.display_info()

martha.spend_points(40)
martha.display_info()


 #Attributes:
# On instantiation of a user, the following attributes should be passed in as arguments:

# first_name
# last_name
# email
# age
# Also include default attributes:

# is_rewards_member - default value of False
# gold_card_points = 0
# Methods:
# display_info(self) - Have this method print all of the users' details on separate lines.
# enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
# spend_points(self, amount) - have this method decrease the user's points by the amount specified.
# Ninja Bonuses:

# Add logic in the enroll method to check if they are a member already, and if they are, print "User already a member." and return False, otherwise return True.
# Add logic in the spend points method to be sure they have enough points to spend that amount and handle appropriately.