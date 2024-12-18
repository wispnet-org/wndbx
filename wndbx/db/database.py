import sqlite3

class Database:
    def __init__(self, db_name="profiles.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS profiles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                firstname TEXT,
                middlename TEXT,
                lastname TEXT,
                age TEXT,
                dob TEXT,
                phone_numbers TEXT,
                emails TEXT,
                cars_and_plates TEXT
            )
        ''')
        self.conn.commit()

    def insert_profile(self, data):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO profiles (firstname, middlename, lastname, age, dob, phone_numbers, emails, cars_and_plates)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', data)
        self.conn.commit()

    def fetch_profile_by_id(self, profile_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM profiles WHERE id = ?", (profile_id,))
        return cursor.fetchone()
