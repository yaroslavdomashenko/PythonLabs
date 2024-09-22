import csv
from faker import Faker
import random

fake = Faker('uk_UA')

male_patronymics = ['Іванович', 'Петрович', 'Сергійович', 'Олександрович', 'Володимирович',
                    'Миколайович', 'Богданович', 'Юрійович', 'Михайлович', 'Андрійович']
female_patronymics = ['Іванівна', 'Петрівна', 'Сергіївна', 'Олександрівна', 'Володимирівна',
                      'Миколаївна', 'Богданівна', 'Юріївна', 'Михайлівна', 'Андріївна']

def generate_employee(gender):
    if gender == 'male':
        first_name = fake.first_name_male()
        patronymic = random.choice(male_patronymics)
        last_name = fake.last_name_male()
    else:
        first_name = fake.first_name_female()
        patronymic = random.choice(female_patronymics)
        last_name = fake.last_name_female()

    birth_date = fake.date_of_birth(minimum_age=16, maximum_age=85)
    position = fake.job()
    city = fake.city()
    address = fake.address()
    phone = fake.phone_number()
    email = fake.email()

    return [last_name, first_name, patronymic, 'Чоловік' if gender == 'male' else 'Жінка', birth_date, position, city, address, phone, email]

def generate_employees_data(num_employees=2000):
    employees = []
    male_count = int(num_employees * 0.6)
    female_count = num_employees - male_count

    for _ in range(male_count):
        employees.append(generate_employee('male'))

    for _ in range(female_count):
        employees.append(generate_employee('female'))

    random.shuffle(employees)

    return employees

def write_to_csv(filename, employees):
    header = ['Прізвище', 'Ім’я', 'По батькові', 'Стать', 'Дата народження','Посада', 'Місто проживання', 'Адреса проживання', 'Телефон', 'Email']

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(employees)

    print("CSV файл успішно створений!")

if __name__ == "__main__":
    employees = generate_employees_data()
    write_to_csv('employees.csv', employees)

