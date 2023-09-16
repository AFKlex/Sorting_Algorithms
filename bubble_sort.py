from array_management import revers_array
def bubble_sort_ascending(array_to_sort):
    for _ in array_to_sort:
        for index in range(len(array_to_sort)-1):
            if array_to_sort[index] >= array_to_sort[index+1]:
                switcher = array_to_sort[index]
                array_to_sort[index] = array_to_sort[index+1] 
                array_to_sort[index+1] = switcher
    
    return array_to_sort

def bubble_sort_descending(array_to_sort):
    array_sorted_ascending = bubble_sort_ascending(array_to_sort)
    return  revers_array(array_sorted_ascending)