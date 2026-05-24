from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    result = [0] * len(nested_arr)
    for i in range(len(nested_arr)):
        result[i] = max(nested_arr[i])
    return result


# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
