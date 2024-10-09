import math
import csv
import os

def save_to_csv(a, R, area_square, area_circle):
    with open('MyData.csv', 'w', newline='') as csvfile:
        fieldnames = ['Сторона квадрата', 'Радіус кола', 'Площа квадрата', 'Площа кола', 'Більша фігура']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        larger_figure = "Квадрат" if area_square > area_circle else "Коло"
        writer.writerow({
            'Сторона квадрата': a,
            'Радіус кола': R,
            'Площа квадрата': area_square,
            'Площа кола': f"{area_circle:.2f}",
            'Більша фігура': larger_figure
        })

def read_from_csv():
    if os.path.exists('MyData.csv'):
        with open('MyData.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)
            if data:
                row = data[0]
                if row:
                    a = float(row['Сторона квадрата'])
                    R = float(row['Радіус кола'])
                    area_square = float(row['Площа квадрата'])
                    area_circle = float(row['Площа кола'])
                    return a, R, area_square, area_circle
    return None

def print_results(language, a, R, area_square, area_circle):
    if language == "uk":
        print(f"Мова: Українська")
        print(f"Сторона квадрата a: {a}")
        print(f"Радіус кола R: {R}")
        print(f"Площа квадрата: {area_square}")
        print(f"Площа кола: {area_circle:.2f}")
        if area_square > area_circle:
            print("Площа квадрата більше.")
        else:
            print("Площа кола більше.")
    elif language == "en":
        print(f"Language: English")
        print(f"Square side a: {a}")
        print(f"Circle radius R: {R}")
        print(f"Square area: {area_square}")
        print(f"Circle area: {area_circle:.2f}")
        if area_square > area_circle:
            print("Square has a larger area.")
        else:
            print("Circle has a larger area.")
    else:
        print("Unsupported language.")

if __name__ == '__main__':
    data = read_from_csv()

    if data:
        a, R, square_area, circle_area = data
        language = input("Введіть мову інтерфейсу (uk/en): ")
    else:
        a = float(input("Введіть сторону квадрата a: "))
        R = float(input("Введіть радіус кола R: "))
        language = input("Введіть мову інтерфейсу (uk/en): ")

        square_area = a ** 2
        circle_area = math.pi * (R ** 2)

        save_to_csv(a, R, square_area, circle_area)

    print_results(language, a, R, square_area, circle_area)
