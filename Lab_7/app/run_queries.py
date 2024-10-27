from prettytable import PrettyTable
from config.db_config import conn

def execute_and_print_query(title, query, params=None):
    with conn.cursor() as cur:
        cur.execute(query, params)
        data = cur.fetchall()
        columns = [desc[0] for desc in cur.description]
        table = PrettyTable()
        table.field_names = columns
        table.add_rows(data)
        print(f"\n--- {title} ---\n")
        print(table)

queries = {
    "All individual clients": "SELECT * FROM Clients WHERE client_type = 'individual' ORDER BY last_name;",
    "Count clients by type": "SELECT client_type, COUNT(*) FROM Clients GROUP BY client_type;",
    "Cost per call": """
        SELECT call_id, duration_minutes * Rates.cost_per_minute AS call_cost
        FROM Calls JOIN Rates ON Calls.rate_id = Rates.rate_id;
    """,
    "Calls by selected type": """
        SELECT * FROM Calls WHERE rate_id = (
            SELECT rate_id FROM Rates WHERE call_type = %s
        );
    """,
    "Total cost per client": """
        SELECT Clients.client_id, SUM(duration_minutes * Rates.cost_per_minute) AS total_cost
        FROM Calls JOIN Phones ON Calls.phone_number = Phones.phone_number
        JOIN Clients ON Phones.client_id = Clients.client_id
        JOIN Rates ON Calls.rate_id = Rates.rate_id
        GROUP BY Clients.client_id;
    """,
    "Minutes per call type per client": """
        SELECT Clients.client_id, Rates.call_type, SUM(duration_minutes) AS total_minutes
        FROM Calls JOIN Phones ON Calls.phone_number = Phones.phone_number
        JOIN Clients ON Phones.client_id = Clients.client_id
        JOIN Rates ON Calls.rate_id = Rates.rate_id
        GROUP BY Clients.client_id, Rates.call_type;
    """
}

if __name__ == "__main__":
    for title, query in queries.items():
        params = ('mobile',) if title == "Calls by selected type" else None
        execute_and_print_query(title, query, params)
