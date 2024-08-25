import sqlite3

def create_database():
    connection = sqlite3.connect('prison_management.db')
    cursor = connection.cursor()

    # Create Prisoners table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Prisoners (
                        prisoner_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        date_of_birth DATE NOT NULL,
                        gender TEXT NOT NULL,
                        admission_date DATE NOT NULL,
                        release_date DATE,
                        status TEXT NOT NULL,
                        cell_id INTEGER,
                        crime_id INTEGER,
                        sentence_duration INTEGER NOT NULL,
                        medical_history TEXT,
                        FOREIGN KEY(cell_id) REFERENCES Cells(cell_id),
                        FOREIGN KEY(crime_id) REFERENCES Crimes(crime_id)
                      )''')

    # Create Cells table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Cells (
                        cell_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        block_name TEXT NOT NULL,
                        cell_number TEXT NOT NULL,
                        capacity INTEGER NOT NULL,
                        current_occupancy INTEGER NOT NULL
                      )''')

    # Create Crimes table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Crimes (
                        crime_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        crime_name TEXT NOT NULL,
                        description TEXT
                      )''')

    # Other tables can be created similarly...

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_database()
