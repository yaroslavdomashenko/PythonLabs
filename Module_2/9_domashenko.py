coefficients = [-2, 2, 0, -1, 1, 2, 7]

print("Коефіцієнти полінома: ", "\033[31m" + " ".join(map(str, coefficients)) + "\033[0m")

x = float(input("Введіть значення x: "))

result = sum(coeff * (x ** i) for i, coeff in enumerate(reversed(coefficients)))

if result > 2_000_000_000:
    print("Переповнення")
else:
    print(f"P({x}) = {result:.2f}")
