num1 = 42 # variable declaration, initialize number, integer
num2 = 2.3 # variable declaration, initialized number, float
boolean = True #variable declaration, initialized boolean
string = 'Hello World'#variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']#variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, initialize dict
fruit = ('blueberry', 'strawberry', 'banana')#variable declaration, initialize dict
print(type(fruit))# log statement, type check
print(pizza_toppings[1])#log statement, list, access value
pizza_toppings.append('Mushrooms') #list add value
print(person['name'])# log statement, dict, access value
person['name'] = 'George'# dict change value
person['eye_color'] = 'blue'# dict add value 
print(fruit[2])# log statement, tuple, access value 

if num1 > 45:# conditional if, logical expression
    print("It's greater") # log statement
else:
    print("It's lower")# log statement

if len(string) < 5:# conditional if, logical expression
    print("It's a short word!")# log statement
elif len(string) > 15:# conditional else if, logical expression
    print("It's a long word!")# log statement
else: # conditional else
    print("Just right!")# log statement

for x in range(5): # for loop start(0) stop (4) 
    print(x)# log statement
for x in range(2,5): # for loop start (2) stop (4)
    print(x)# log statement
for x in range(2,10,3): # for loop start (2) stop (8) because steps of 3
    print(x) # log statement
x = 0 # while loop counter initialization
while(x < 5): # while loop start
    print(x)# log statement:
    x += 1 # increment

pizza_toppings.pop()# list, delete value 
pizza_toppings.pop(1)# list, delete value at index 1 

print(person) # log statetament, print dict
person.pop('eye_color') # KeyError: 'eye_color'
print(person)# log statetament, print dict

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times(): #function
    for num in range(10): # for loop start (0) stop (9)
        print('Hello') # log statement 'Hello' ten times

print_hello_ten_times()

def print_hello_x_times(x): # function
    for num in range(x):# for loop start (0) stop (x)
        print('Hello')# log statement 'Hello' x times

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10): # function default parameter 10
    for num in range(x): # for loop start (0) stop(x or 10 by default)
        print('Hello')# log statement 'Hello'

print_hello_x_or_ten_times() # calling function to print Hello 10 times
print_hello_x_or_ten_times(4) # calling function to print Hello with argument 4 times


"""
Bonus section
"""

# print(num3) NameError: name <num3> is not defined
# num3 = 72 --> variable declaration and initialization to 72
# fruit[0] = 'cranberry' --> Tuple change value
# print(person['favorite_team']) --> KeyError: 'favorite_team'
# print(pizza_toppings[7]) IndexError: list index out of range
#   print(boolean) --> IndentationError: unexpected indent
# fruit.append('raspberry') --> Tuple add value
# fruit.pop(1) --> Tuple delete value
