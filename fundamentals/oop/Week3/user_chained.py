# Assignment: User using chaining
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
        return self
    
    def enroll(self):
        if self.is_rewards_member:
            print("User already a member.")
        else:
            self.is_rewards_member = True
            self.gold_cards_points = 200
        return self
#  Implement the spend_points(self, amount) method   
    def spend_points(self, amount):
        if amount < self.gold_cards_points:
            self.gold_cards_points-=amount
        return self

rod = User('Rodrigo', 'Arguello', 'rodrigo19662001@gmail.com', '45')
rod.display_info().enroll().spend_points(50).display_info()

jose = User('Jose', 'Frank', 'jose@gmail.com', '28')
jose.enroll().spend_points(80).display_info()
