Numbers = input("Enter the numbers:")
numbers = list(map(int,Numbers.split()))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    
    left_part = []
    for x in arr[1:]:
        if x<= pivot:
            left_part.append(x)

    right_part = []
    for x in arr[1:]:
        if x > pivot:
            right_part.append(x)

    return quick_sort(left_part) + [pivot] + quick_sort(right_part)

sorted_list = quick_sort(numbers)
print(f"Original list: {numbers}")
print(f"Sorted list: {sorted_list}")               

