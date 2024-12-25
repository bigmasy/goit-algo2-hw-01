def quick_select(arr, k):
    
    if k < 1 or k > len(arr): # Перевірка на допустимість значення k
        raise IndexError("k is out of range")

# Допоміжна функція для розбиття масиву навколо опорного елемента
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1  # Позиція опорного елемента після розбиття

# Основна рекурсивна функція для пошуку k-го найменшого елемента
    def quick_select_recursive(arr, low, high, k):
        if low <= high:
            pivot_index = partition(arr, low, high)  # Розбиття навколо pivot
            if pivot_index == k:
                return arr[pivot_index]  # Повертаємо k-й елемент
            elif pivot_index < k:
                return quick_select_recursive(arr, pivot_index + 1, high, k)  # Шукаємо в правій частині
            else:
                return quick_select_recursive(arr, low, pivot_index - 1, k)  # Шукаємо в лівій частині

    # Викликаємо основну функцію для пошуку k-го елемента
    return quick_select_recursive(arr, 0, len(arr) - 1, k - 1)  # k-1, оскільки індексація з 0

# Приклад використання
arr = [38, 27, 43, 3, 9, 82, 10]
k = 3
result = quick_select(arr, k)
print(f"{k}-й найменший елемент: {result}")  # Output: 10
