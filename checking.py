
def is_array_sorted_ascending(array):
    for position in range(len(array)-1):
        if array[position] > array[position+1]:
            return False
    return True

