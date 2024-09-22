import csv
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd

def calculate_age(birth_date):
    today = datetime.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

def read_csv_data(filename):
    employees = []
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                birth_date = datetime.strptime(row['Дата народження'], '%Y-%m-%d')
                age = calculate_age(birth_date)
                employees.append({
                    'last_name': row['Прізвище'],
                    'first_name': row['Ім’я'],
                    'patronymic': row['По батькові'],
                    'gender': row['Стать'],
                    'birth_date': birth_date,
                    'age': age
                })
        print("Ok")
    except FileNotFoundError:
        print("Помилка: файл CSV не знайдено.")
        return []
    except Exception as e:
        print(f"Помилка при відкритті файлу CSV: {e}")
        return []

    return employees

def count_by_gender(employees):
    male_count = sum(1 for emp in employees if emp['gender'] == 'Чоловік')
    female_count = sum(1 for emp in employees if emp['gender'] == 'Жінка')

    print(f"Чоловіків: {male_count}, Жінок: {female_count}")

    plt.figure(figsize=(6, 6))
    labels = ['Чоловіки', 'Жінки']
    counts = [male_count, female_count]
    plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=90, colors=['blue', 'pink'])
    plt.title('Розподіл співробітників за статтю')
    plt.show()

def count_by_age_group(employees):
    younger_18 = sum(1 for emp in employees if emp['age'] < 18)
    between_18_and_45 = sum(1 for emp in employees if 18 <= emp['age'] <= 45)
    between_45_and_70 = sum(1 for emp in employees if 45 < emp['age'] <= 70)
    older_70 = sum(1 for emp in employees if emp['age'] > 70)

    print(f"Молодше 18: {younger_18}, 18-45: {between_18_and_45}, 45-70: {between_45_and_70}, Старше 70: {older_70}")

    plt.figure(figsize=(6, 6))
    labels = ['Молодше 18', '18-45', '45-70', 'Старше 70']
    counts = [younger_18, between_18_and_45, between_45_and_70, older_70]
    plt.bar(labels, counts, color=['green', 'orange', 'blue', 'red'])
    plt.title('Розподіл співробітників за віковими категоріями')
    plt.show()

def count_by_gender_and_age(employees):
    categories = {
        'Молодше 18': {'Чоловіки': 0, 'Жінки': 0},
        '18-45': {'Чоловіки': 0, 'Жінки': 0},
        '45-70': {'Чоловіки': 0, 'Жінки': 0},
        'Старше 70': {'Чоловіки': 0, 'Жінки': 0}
    }

    for emp in employees:
        age = emp['age']
        gender = 'Чоловіки' if emp['gender'] == 'Чоловік' else 'Жінки'
        if age < 18:
            categories['Молодше 18'][gender] += 1
        elif 18 <= age <= 45:
            categories['18-45'][gender] += 1
        elif 45 < age <= 70:
            categories['45-70'][gender] += 1
        else:
            categories['Старше 70'][gender] += 1

    print(categories)

    # Побудова діаграм
    for category, counts in categories.items():
        plt.figure(figsize=(6, 6))
        labels = list(counts.keys())
        values = list(counts.values())
        plt.bar(labels, values, color=['blue', 'pink'])
        plt.title(f'Розподіл за статтю в категорії {category}')
        plt.show()

if __name__ == "__main__":
    employees = read_csv_data('employees.csv')

    if employees:
        count_by_gender(employees)
        count_by_age_group(employees)
        count_by_gender_and_age(employees)
