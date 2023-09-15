
def is_array_sorted_ascending(array):
    for position in range(len(array)-1):
        if array[position] > array[position+1]:
            return False
    return True

def revers_array(array): 
    new_array = []
    for item in array:
        new_array.insert(0,item)
    return new_array

