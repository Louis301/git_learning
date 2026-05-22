import random

def quicksort(arr: list) -> list:
	print(f"Валид. длины списка arr (<= 1 == {len(arr) <= 1})...")
	if len(arr) <= 1:
		return arr
	
	print("Выбор опорного элемента...")
	pivot = random.choice(arr)
	
	print("Разделение массива...")
	left   = [x for x in arr if x < pivot]
	middle = [x for x in arr if x == pivot]
	right  = [x for x in arr if x > pivot]
	
	print("Рекурсивный вызов и объединение...")
	return quicksort(left) + middle + quicksort(right)

# ===================================================
max_n = 10

list_ = [random.randint(1, 100) for _ in range(max_n)]

print(quicksort(list_))
