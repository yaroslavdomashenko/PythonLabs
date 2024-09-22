import csv
from datetime import datetime
import pandas as pd

def calculate_age(birth_date):
    today = datetime.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

def read_csv_data(filename):
    employees = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            birth_date = datetime.strptime(row['Дата народження'], '%Y-%m-%d')
            age = calculate_age(birth_date)
            employees.append({
                'Прізвище': row['Прізвище'],
                'Ім’я': row['Ім’я'],
                'По батькові': row['По батькові'],
                'Дата народження': birth_date,
                'Вік': age
            })
    return employees

def categorize_by_age(employees):
    all_employees = employees
    younger_18 = [emp for emp in employees if emp['Вік'] < 18]
    between_18_and_45 = [emp for emp in employees if 18 <= emp['Вік'] <= 45]
    between_45_and_70 = [emp for emp in employees if 45 < emp['Вік'] <= 70]
    older_70 = [emp for emp in employees if emp['Вік'] > 70]

    return {
        'all': all_employees,
        'younger_18': younger_18,
        '18-45': between_18_and_45,
        '45-70': between_45_and_70,
        'older_70': older_70
    }

def write_to_excel(filename, categorized_data):
    # Створюємо ExcelWriter
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        for sheet_name, data in categorized_data.items():
            df = pd.DataFrame(data)
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    print("Excel файл успішно створений!")

if __name__ == "__main__":
    try:
        employees = read_csv_data('employees.csv')

        categorized_data = categorize_by_age(employees)

        write_to_excel('employees_by_age.xlsx', categorized_data)

        print("Ok")
    except FileNotFoundError:
        print("Помилка: файл CSV не знайдено.")
    except Exception as e:
        print(f"Помилка при створенні XLSX файлу: {e}")


