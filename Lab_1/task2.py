# Створити рекурсивну функцію fib(k), яка повертає список n чисел Фібоначчі.
# Написати програму яка виводить k чисел Фібоначчі, використовуючи функцію fib(k).

def fib(k):
    if k <= 0:
        return []
    elif k == 1:
        return [0]
    elif k == 2:
        return [0, 1]
    else:
        fib_list = fib(k - 1)
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list

if __name__ == "__main__":
    k = int(input("Enter the value of k: "))
    fib_sequence = fib(k)
    print(f"The first {k} Fibonacci numbers: {fib_sequence}")
