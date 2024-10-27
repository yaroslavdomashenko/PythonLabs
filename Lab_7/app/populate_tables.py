from config.db_config import conn
from faker import Faker
import random

faker = Faker()
CALL_TYPES = ['local', 'intercity', 'mobile']

def insert_clients(cursor):
    clients = [
        (faker.random_element(['individual', 'department']), faker.address(), faker.last_name(), faker.first_name(),
         faker.first_name())
        for _ in range(5)
    ]
    cursor.executemany(
        "INSERT INTO Clients (client_type, address, last_name, first_name, middle_name) VALUES (%s, %s, %s, %s, %s)",
        clients
    )
    cursor.execute("SELECT client_id FROM Clients")
    return [client[0] for client in cursor.fetchall()]


def insert_phones(cursor, client_ids):
    phones = [(faker.phone_number()[:15], random.choice(client_ids)) for _ in range(7)]
    cursor.executemany(
        "INSERT INTO Phones (phone_number, client_id) VALUES (%s, %s)",
        phones
    )

def insert_rates(cursor):
    rates = [(call_type, round(random.uniform(0.5, 2.5), 2)) for call_type in CALL_TYPES]
    cursor.executemany(
        "INSERT INTO Rates (call_type, cost_per_minute) VALUES (%s, %s)",
        rates
    )

def insert_calls(cursor, phones):
    calls = [
        (faker.date_this_month(), phone[0], random.randint(1, 20), random.randint(1, len(CALL_TYPES)))
        for phone in phones
    ]
    cursor.executemany(
        "INSERT INTO Calls (call_date, phone_number, duration_minutes, rate_id) VALUES (%s, %s, %s, %s)",
        calls
    )

def populate_tables():
    with conn.cursor() as cursor:
        client_ids = insert_clients(cursor)
        insert_phones(cursor, client_ids)
        insert_rates(cursor)

        cursor.execute("SELECT phone_number FROM Phones")
        phones = cursor.fetchall()
        insert_calls(cursor, phones)

    conn.commit()


if __name__ == "__main__":
    populate_tables()
