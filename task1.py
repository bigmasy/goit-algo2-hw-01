def find_min_max(arr):
    if len(arr) == 1: # один елемент в масиві
        return arr[0], arr[0]
    
    if len(arr) == 2: # два елементи в масиві
        return (arr[0], arr[1]) if arr[0] < arr[1] else (arr[1], arr[0])
    
    mid = len(arr) // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])
    
    return (min(left_min, right_min), max(left_max, right_max))

# Приклад використання
arr = [38, 27, 43, 3, 9, 82, 10]
result= find_min_max(arr)
print(result)  # 3, 82
