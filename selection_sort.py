from array_management import revers_array

def selection_sort_decending(array_to_sort):
    hightes_item = find_hightes_element(array_to_sort)+1
    for position in range(int(len(array_to_sort))):
        hightes_item = find_higest_element_grather_than(array_to_sort,hightes_item)
        index_highes_item = array_to_sort.index(hightes_item)
        switcher = array_to_sort[position]
        array_to_sort[position] = array_to_sort[index_highes_item]
        array_to_sort[index_highes_item] = switcher
    return array_to_sort

def selection_sort_ascending(array_to_sort):
    decending_array = selection_sort_decending(array_to_sort)
    return revers_array(decending_array)

def find_hightes_element(array):
    highes_item = 0
    for item in array:
        if item > highes_item:
            highes_item = item
    return highes_item


def find_higest_element_grather_than(array, grather_than):
    hightes_item = 0
    for index in range(len(array)):
        if hightes_item < array[index] and array[index] < grather_than:
            hightes_item = array[index]
    return hightes_item

