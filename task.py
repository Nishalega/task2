def find_pairs(arr, target):
    complements = {}
    pairs = []
   
    for num in arr:
        complement = target - num
        if complement in complements:
            pairs.append([num, complement])
        else:
            complements[num] = True
   
    return pairs

def merge_and_find_combinations(arr, target):
    merged_arr = sorted(arr)
    double_target = 2 * target
    combinations = []
   
    for i in range(len(merged_arr)):
        num = merged_arr[i]
        remaining = double_target - num
        temp_arr = merged_arr[i+1:]
       
        left = 0
        right = len(temp_arr) - 1
       
        while left < right:
            if temp_arr[left] + temp_arr[right] == remaining:
                combinations.append([num] + temp_arr[left:right+1])
                left += 1
                right -= 1
            elif temp_arr[left] + temp_arr[right] < remaining:
                left += 1
            else:
                right -= 1
   
    return combinations


input_arr = [1, 3, 2, 2, -4, -6, -2, 8]
target_value = 4

first_combination = find_pairs(input_arr, target_value)
merged_array = sorted(input_arr)
double_target = 2 * target_value
second_combination = merge_and_find_combinations(merged_array, double_target)

print("First Combination For", target_value, ":", first_combination)
print("Merge Into a single Array :", merged_array)
print("Second Combination For", double_target, ":", second_combination)
