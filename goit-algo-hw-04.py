import random
import timeit
import matplotlib.pyplot as plt

# Сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Вимірювання часу виконання
def measure_time(sort_function, data, number=3):
    timer = timeit.Timer(lambda: sort_function(data.copy()))
    time_taken = timer.timeit(number=number) / number
    return time_taken

# Генерація тестових даних
def generate_data(size, ordered=False):
    if ordered:
        return sorted([random.randint(0, size) for _ in range(size)])
    return [random.randint(0, size) for _ in range(size)]

# Розміри тестових масивів
sizes = [10, 100, 1000, 10000]

# Кількість повторів для кожного розміру масиву
repeats = 3

# Запуск тестів
results = {}
for size in sizes:
    print(f"Розмір масиву: {size}")
    data = generate_data(size)
    
    # Вимірюємо час виконання сортування злиттям
    merge_time = sum(measure_time(merge_sort, data, number=repeats) for _ in range(repeats)) / repeats
    print(f"Час виконання сортування злиттям: {merge_time} секунд")
    
    # Вимірюємо час виконання сортування вставками
    insertion_time = sum(measure_time(insertion_sort, data, number=repeats) for _ in range(repeats)) / repeats
    print(f"Час виконання сортування вставками: {insertion_time} секунд")
    
    # Вимірюємо час виконання Timsort (вбудованого сортування в Python)
    timsort_time = sum(measure_time(sorted, data, number=repeats) for _ in range(repeats)) / repeats
    print(f"Час виконання Timsort: {timsort_time} секунд")
    
    results[size] = {
        "merge_sort": merge_time,
        "insertion_sort": insertion_time,
        "timsort": timsort_time
    }

# Витягуємо дані для побудови графіків
merge_times = [results[size]['merge_sort'] for size in sizes]
insertion_times = [results[size]['insertion_sort'] for size in sizes]
timsort_times = [results[size]['timsort'] for size in sizes]

# Побудова графіків
plt.figure(figsize=(10, 6))
plt.plot(sizes, merge_times, label='Merge Sort', marker='o')
plt.plot(sizes, insertion_times, label='Insertion Sort', marker='o')
plt.plot(sizes, timsort_times, label='Timsort', marker='o')
plt.xlabel('Size of array')
plt.ylabel('Time (seconds)')
plt.title('Comparison of Sorting Algorithms')
plt.legend()
plt.grid(True)
plt.show()
