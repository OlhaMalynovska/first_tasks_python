#Треба перевірити

#You have a group of people with non-unique names. Generate a list of non-duplicate names
#(you cannot use set for this task. If there are 2 johns in the list, you need to take only one of them.
 #"John Dow", "John Dow", "Marta Dow" => "John Dow", "Marta Dow ")

 #Dictionaries cannot have two items with the same key:
 #"John Dow", "John Dow", "Marta Dow"

people = {"John Dow", "John Dow", "Marta Dow" }

lastname = "Dow"

# creates a dictionary with keys and values
dictionary_name= dict.fromkeys(people, lastname)

print(dictionary_name.keys())
