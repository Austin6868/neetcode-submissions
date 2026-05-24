from typing import List

# shallow copy
def remove_element(arr: List[int], element: int) -> List[int]:
    copy_list = arr.copy()
    copy_list.remove(element)
    return copy_list

# do not modify below this line
arr = [1, 3, 5, 7, 9]

print(remove_element(arr, 3))
print(arr)
print(remove_element(arr, 9))
print(arr)
print(remove_element(arr, 1))
print(arr)
