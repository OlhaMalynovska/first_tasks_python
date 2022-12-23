# there is a list of friends ["John", "Marta", "James", "Amanda", "Marianna"].
# print to the console the names of each on a new line, right-aligned using
# the string method and formatting via f string. Also, above the names,
# in the first line, display the headings Names where the word names should be in the middle, and the rest of
#  the space is filled with the symbol "*"

friends =["John", "Marta", "James", "Amanda", "Marianna"]
s = "Name"
print(s.center(30,'*'))
for friend in friends:
  print(f"{friend : >30}")