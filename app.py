import sys

def binary_search(array: list[int], x: int, low: int, high: int):
    while low <= high:
        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return None

def find_pairs(ordered_array: list[int], target_sum: int) -> list[tuple[int, int]]:
    pairs = []
    mid = round(len(ordered_array) / 2)
    for i in range(mid):
        item = ordered_array[i]
        target_addend = target_sum - item
        result = binary_search(ordered_array, target_addend, 0, len(ordered_array)-1)
        if result:
            pairs.append((item, target_addend))
    return pairs

def get_sorted_array_and_target_sum_from_input(input_1_array, input_2_target_value):
    input_1_numbers = input_1_array.split(',')
    unsorted_array = [int(x) for x in input_1_numbers]
    sorted_array = sorted(unsorted_array)
    target_sum = int(input_2_target_value)
    return (sorted_array, target_sum)

if __name__ == "__main__":
    input_1 = sys.argv[1]
    input_2 = sys.argv[2]

    (sorted_array, target_sum)= get_sorted_array_and_target_sum_from_input(input_1, input_2)
    pairs = find_pairs(sorted_array, target_sum)
    print(pairs)
