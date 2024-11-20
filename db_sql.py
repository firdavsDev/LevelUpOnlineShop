import sqlite3  # import sqlite3 module


# custom manager for opening sqlite3 and closing it
class OpenSqlite:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()


# Create a connection to the database
with OpenSqlite("new_db.sqlite3") as cursor:
    # Create a table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT,
            price REAL,
            stock INTEGER
        );
    """
    )

    # Insert a record
    cursor.execute(
        """
        INSERT INTO products (name, description, price, stock)
        VALUES ("Apple", "Apple from USA", 1.2, 100);
    """
    )

    # Select all records from the table
    cursor.execute("SELECT * FROM products;")

    # Fetch all records
    records = cursor.fetchall()
    print(records)
