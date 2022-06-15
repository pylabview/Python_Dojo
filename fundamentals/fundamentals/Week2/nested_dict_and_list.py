
#   1. Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# TODO: Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x)

#TODO: Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0] ['last_name'] = 'Bryant'
print(students)

# TODO In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

# TODO: Change the value 20 in z to 30

z[0]['y'] = 30
print(z)

#2. Iterate Through a List of Dictionaries
# TODO: Create a function iterateDictionary(some_list) that, given a list of dictionaries, 
# the function loops through each dictionary in the list and prints each key and the associated value. 

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(students):
    for s in students:
        ptr_str = ''
        for k,v in s.items():
            ptr_str = ptr_str + k + ' - ' + v + ', '
        print(ptr_str[:-2])
        
iterateDictionary(students)

#3. Get Values From a List of Dictionaries
# TODO: Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries
# and a key name, the function prints the value stored in that key for each dictionary. 

def iterateDictionary2(k,l):
    for d in l:
        print(d[k])
    print('')

iterateDictionary2('first_name', students)


iterateDictionary2('last_name', students) 

# 4. Iterate Through a Dictionary with List Values
#TODO: Create a function printInfo(some_dict) that given a dictionary whose values are all lists,
# prints the name of each key along with the size of its list, and then prints the associated values
# within each key's list

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    for k,v in dojo.items():
        print(f"{len(v)} {k.upper()}")
        for idx,item in enumerate(v):
            print(item)
        print('')

printInfo(dojo)





