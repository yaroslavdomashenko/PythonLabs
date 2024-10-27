# Домашенко Ярослав Олегович, ІПЗ-22011бск, Варіант 9
import random

# Завдання 1. Створення масиву із заданими властивостями
array = [random.randint(-99, 99) for _ in range(44)]

positive_count = int(0.3 * 44)
positive_indices = random.sample(range(44), positive_count)
for i in positive_indices:
    array[i] = abs(array[i])

max_value = max(array)
max_count = random.choice([3, 4])
max_indices = random.sample(range(44), max_count)
for i in max_indices:
    array[i] = max_value

print("Згенерований масив:", array)

# Завдання 2. Збереження масиву в файл
with open('array.txt', 'w') as f:
    f.write(' '.join(map(str, array)))
print("Масив збережено в 'array.txt'.")

# Завдання 3. Зчитування масиву з файлу та виведення його на екран
with open('array.txt', 'r') as f:
    loaded_array = list(map(int, f.read().split()))
print("Масив з файлу:", loaded_array)

# Завдання 4. Візуалізація масиву
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
bars = plt.barh(range(len(loaded_array)), loaded_array, color='grey')

for i, val in enumerate(loaded_array):
    if val == max_value:
        bars[i].set_color('red')
        plt.text(val, i, str(val), va='center', ha='right')

for i, val in enumerate(loaded_array):
    if val > 0 and val != max_value:
        bars[i].set_color('blue')
        plt.text(val, i, str(val), va='center', ha='left')

plt.xlabel("Значення елементів")
plt.ylabel("Індекс елемента")
plt.title("Горизонтальна стовпчаста діаграма масиву")
plt.show()

# Завдання 5. Пошук позицій другого та третього максимальних елементів
sorted_unique_vals = sorted(set(loaded_array), reverse=True)
second_max = sorted_unique_vals[1]
third_max = sorted_unique_vals[2]
second_max_pos = [i for i, v in enumerate(loaded_array) if v == second_max]
third_max_pos = [i for i, v in enumerate(loaded_array) if v == third_max]

print("Позиції другого максимального елемента:", second_max_pos)
print("Позиції третього максимального елемента:", third_max_pos)

# Завдання 6. Пошук кількості та суми елементів між другим та третім додатними елементами
positive_positions = [i for i, x in enumerate(loaded_array) if x > 0]
if len(positive_positions) >= 3:
    start, end = positive_positions[1], positive_positions[2]
    elements_between = loaded_array[start+1:end]
    count_between = len(elements_between)
    sum_between = sum(elements_between)
else:
    count_between = 0
    sum_between = 0

print("Кількість елементів між другим і третім додатними:", count_between)
print("Сума елементів між другим і третім додатними:", sum_between)

# Завдання 7. Перетворення масиву з сортуванням
positive_sorted = sorted([x for x in loaded_array if x > 0])
negative_sorted = sorted([x for x in loaded_array if x <= 0], reverse=True)
transformed_array = positive_sorted + negative_sorted

print("Перетворений масив:", transformed_array)

plt.figure(figsize=(10, 6))
bars = plt.barh(range(len(transformed_array)), transformed_array, color='grey')

for i, val in enumerate(transformed_array):
    if val > 0:
        bars[i].set_color('blue')
        plt.text(val, i, str(val), va='center', ha='left')

plt.xlabel("Значення елементів")
plt.ylabel("Індекс елемента")
plt.title("Горизонтальна стовпчаста діаграма перетвореного масиву")
plt.show()
