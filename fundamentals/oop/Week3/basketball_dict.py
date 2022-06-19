# Assignment: Basketball Dictionaries
# Author: Rodrigo Arguello
# Date: 06/18/2022


players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33, "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32, "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
    	"name": "", 
    	"age":16, 
    	"position": "P", 
    	"team": "en"
    }
]


kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}
    
# Create your Player instances here!
# player_jason = ???



class Player:
    def __init__(self,kwargs):
        self.name = kwargs.get('name')
        self.age =  kwargs.get('age')
        self.position = kwargs.get('position')
        self.team = kwargs.get('team')
        
    @classmethod
    def add_team(cls, team_list):
        player_instances=[]
        for item in team_list:
            player_instances.append(cls(item))
        return player_instances
            
    def __repr__(self) -> str:
        return f"Player name: {self.name}, age: {self.age}, position: {self.position}, team: {self.team}"

player1 = Player(kevin)

player2 = Player(jason)

player3 = Player(kyrie)

print(player1)
print(player2)
print(player3)

# ... (class definition and large list of players here)
new_team = []
# Write your for loop here to populate the new_team variable with Player objects.
    
for item in players:
    new_team.append(Player(item))

print(new_team)

# Testing classmethod
new_list_1 = Player.add_team(players)

print(new_list_1)


