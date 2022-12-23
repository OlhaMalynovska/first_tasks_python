#
# #Variant~1 use list
# Eleks = ["Pavlo", "Bogdan", "Anton", "Dmytro", "Anna", "Alla", "Artem"]
# Toshiba = ["Kasja", "Dasja", "Anton", "Alla", "Vasja", "Asja", "Artem"]
# print(Eleks+Toshiba)



#Variant~2 use set
eleks = {"Pavlo", "Bogdan", "Anton", "Dmytro", "Anna", "Alla", "Artem"}
toshiba ={"Kasja", "Dasja", "Anton", "Alla", "Vasja", "Asja", "Artem"}

toshiba.update(eleks)
eleks.clear()

print(toshiba)
