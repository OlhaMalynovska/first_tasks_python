# Треба перевірити
# you have a list of elements [1, 2, 3, 4, 5, 6, 7, 8]. Loop through the list using the foreach loop.
# The element with an odd index is put into a new list of tuples where the first element is the index
# and the second is the value. [(index, value)]. accordingly, elements
# with an even index are placed in another list of tuples with the same format as in the case with odd indices.
elements = [1, 2, 3, 4, 5, 6, 7, 8]
odd_list = []
list_index_odd_list = []
even_list = []
list_index_even_list = []
for element in elements:
    index = elements.index(element)
    if index % 2 == 0:
        (odd_list.append(element))
        (list_index_odd_list.append(index))
    else:
        even_list.append(element)
        list_index_even_list.append(index)
print('List of tuples, elements with even indexes --------',tuple(zip(list_index_even_list, even_list)))
print('List of tuples, elements with odd indexes --------',tuple(zip(list_index_odd_list,odd_list)))






