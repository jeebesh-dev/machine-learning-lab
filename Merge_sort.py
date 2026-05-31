Numbers = input("Enter the numbers:")
numbers = list(map(int,Numbers.split()))
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    middle = len(arr) // 2
    left_part = arr[:middle]
    right_part = arr[middle:]
    sorted_left = merge_sort(left_part)
    sorted_right = merge_sort(right_part)
    return merge(sorted_left,sorted_right)

def merge(left,right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

sorted_numbers = merge_sort(numbers)
print(f"sorted list:{sorted_numbers}")