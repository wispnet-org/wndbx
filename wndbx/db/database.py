import sqlite3

def initialize_db():
    connection = sqlite3.connect("app_data.db")
    cursor = connection.cursor()
    
    # Example: Create tables if they don't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)''')
    connection.commit()
    connection.close()

def get_user_data(user_id):
    connection = sqlite3.connect("app_data.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
    data = cursor.fetchone()
    connection.close()
    return data
