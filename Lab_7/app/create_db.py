from config.db_config import conn

def create_clients_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Clients (
        client_id SERIAL PRIMARY KEY,
        client_type VARCHAR(20) NOT NULL,
        address VARCHAR(100),
        last_name VARCHAR(50),
        first_name VARCHAR(50),
        middle_name VARCHAR(50)
    );
    """)

def create_phones_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Phones (
        phone_number VARCHAR(15) PRIMARY KEY,
        client_id INTEGER REFERENCES Clients(client_id) ON DELETE CASCADE
    );
    """)

def create_rates_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Rates (
        rate_id SERIAL PRIMARY KEY,
        call_type VARCHAR(20),
        cost_per_minute NUMERIC(5, 2)
    );
    """)

def create_calls_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Calls (
        call_id SERIAL PRIMARY KEY,
        call_date DATE,
        phone_number VARCHAR(15) REFERENCES Phones(phone_number),
        duration_minutes INT,
        rate_id INTEGER REFERENCES Rates(rate_id)
    );
    """)

def create_tables():
    with conn.cursor() as cursor:
        create_clients_table(cursor)
        create_phones_table(cursor)
        create_rates_table(cursor)
        create_calls_table(cursor)
    conn.commit()

if __name__ == "__main__":
    create_tables()
