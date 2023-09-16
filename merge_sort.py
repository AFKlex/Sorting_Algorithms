from array_management import revers_array
import math 
def merge_sort_descending(array_to_sort): 
    merge_steps = int(math.log(len(array_to_sort),2)) +1

    new_array = make_array_into_array_of_arrays(array_to_sort)
    
    for _ in range(merge_steps):
        new_array = merge(new_array)
    
    return new_array

def make_array_into_array_of_arrays(array):
    new_array = []
    for _ in array:
        new_array.append([_])
    return new_array


def merge(array):
    new_array = []
    for index in range(0,len(array),2):

        if index+1 >= len(array):
            new_array.append(array[index])
            break
        arr1 = array[index]
        arr2 = array[index+1]
        merged_array = []

        #Merge Arrays
        while len(arr1) > 0 and len(arr2) > 0:

            if arr1[0] > arr2[0]:
                merged_array.append(arr1[0])
                arr1.pop(0)
            else:
                merged_array.append(arr2[0])
                arr2.pop(0)
            
            if len(arr1) == 0:
                for _ in arr2:
                    merged_array.append(_)
                break
            
            if len(arr2) == 0:
                for _ in arr1:
                    merged_array.append(_)
                break

        new_array.append(merged_array)

    return new_array

def merge_sort_ascending(array_to_sort):
    sorted_descending = merge_sort_descending(array_to_sort)
    return revers_array(sorted_descending)