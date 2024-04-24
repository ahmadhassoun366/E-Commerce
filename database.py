import sqlite3

def init_db():
    try:
        with sqlite3.connect('database.db') as conn:
            conn.execute("PRAGMA foreign_keys = ON;")
            conn.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    userId INTEGER PRIMARY KEY, 
                    password TEXT,
                    email TEXT,
                    firstName TEXT,
                    lastName TEXT,
                    address1 TEXT,
                    address2 TEXT,
                    zipcode TEXT,
                    city TEXT,
                    state TEXT,
                    country TEXT, 
                    phone TEXT
                )
            ''')
            conn.execute('''
                CREATE TABLE IF NOT EXISTS categories (
                    categoryId INTEGER PRIMARY KEY,
                    name TEXT
                )
            ''')
            conn.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    productId INTEGER PRIMARY KEY,
                    name TEXT,
                    price REAL,
                    description TEXT,
                    image TEXT,
                    stock INTEGER,
                    categoryId INTEGER,
                    FOREIGN KEY(categoryId) REFERENCES categories(categoryId)
                )
            ''')
            conn.execute('''
                CREATE TABLE IF NOT EXISTS kart (
                    userId INTEGER,
                    productId INTEGER,
                    FOREIGN KEY(userId) REFERENCES users(userId),
                    FOREIGN KEY(productId) REFERENCES products(productId)
                )
            ''')
            conn.execute('''
                CREATE TABLE IF NOT EXISTS contact_us (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT,
                    message TEXT
                )
            ''')
            print("All tables created successfully")
    except Exception as e:
        print(f"An error occurred: {e}")
