from array_management import revers_array

def insertion_sort_ascending(array_to_sort):
    sorted_array = []
    for item in array_to_sort:

        if (len(sorted_array) == 0):
            sorted_array.append(item)

        for index_sorted_element in range(len(sorted_array)):
            if item <= sorted_array[index_sorted_element]:
                sorted_array.insert(index_sorted_element,item)
                break
            if index_sorted_element == len(sorted_array)-1:
                sorted_array.append(item)

    sorted_array.pop(0)
    return sorted_array

def insertion_sort_decending(array_to_sort):
    array_sorted_ascending = insertion_sort_ascending(array_to_sort)
    return revers_array(array_sorted_ascending)