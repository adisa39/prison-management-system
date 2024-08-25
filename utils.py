import sqlite3
DATABASE_NAME = 'prison_management.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row  # This allows accessing columns by name
    return conn

def create_prisoner(first_name, last_name, date_of_birth, gender, admission_date, status, sentence_duration,
                    cell_id=None, crime_id=None, medical_history=None):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO Prisoners (first_name, last_name, date_of_birth, gender, admission_date, status, sentence_duration, cell_id, crime_id, medical_history)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (first_name, last_name, date_of_birth, gender, admission_date, status, sentence_duration, cell_id,
                    crime_id, medical_history))
    connection.commit()
    connection.close()


def read_prisoner(prisoner_id):
    connection = sqlite3.connect('prison_management.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Prisoners WHERE prisoner_id=?", (prisoner_id,))
    prisoner = cursor.fetchone()
    connection.close()
    return prisoner


def update_prisoner(prisoner_id, first_name=None, last_name=None, date_of_birth=None, gender=None, admission_date=None,
                    status=None, sentence_duration=None, cell_id=None, crime_id=None, medical_history=None):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    # Dynamically construct the SQL UPDATE query
    updates = []
    params = []

    if first_name:
        updates.append("first_name=?")
        params.append(first_name)
    if last_name:
        updates.append("last_name=?")
        params.append(last_name)
    if date_of_birth:
        updates.append("date_of_birth=?")
        params.append(date_of_birth)
    if gender:
        updates.append("gender=?")
        params.append(gender)
    if admission_date:
        updates.append("admission_date=?")
        params.append(admission_date)
    if status:
        updates.append("status=?")
        params.append(status)
    if sentence_duration:
        updates.append("sentence_duration=?")
        params.append(sentence_duration)
    if cell_id:
        updates.append("cell_id=?")
        params.append(cell_id)
    if crime_id:
        updates.append("crime_id=?")
        params.append(crime_id)
    if medical_history:
        updates.append("medical_history=?")
        params.append(medical_history)

    params.append(prisoner_id)

    cursor.execute(f"UPDATE Prisoners SET {', '.join(updates)} WHERE prisoner_id=?", params)
    connection.commit()
    connection.close()


def delete_prisoner(prisoner_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Prisoners WHERE prisoner_id=?", (prisoner_id,))
    conn.commit()
    conn.close()


def get_all_prisoners():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Prisoners")
    prisoners = cursor.fetchall()
    conn.close()
    return prisoners


def search_prisoners(search_term):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM Prisoners WHERE first_name LIKE ? OR last_name LIKE ?"
    cursor.execute(query, ('%' + search_term + '%', '%' + search_term + '%'))
    prisoners = cursor.fetchall()
    conn.close()
    return prisoners

def filter_prisoners_by_status(status):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM Prisoners WHERE status=?"
    cursor.execute(query, (status,))
    prisoners = cursor.fetchall()
    conn.close()
    return prisoners

def get_prisoner_count_by_status():
    """
    Returns a dictionary with the count of prisoners by their status.
    Example: {"Incarcerated": 100, "Released": 50, "Transferred": 20}
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    SELECT status, COUNT(*) as count
    FROM Prisoners
    GROUP BY status
    """
    cursor.execute(query)
    rows = cursor.fetchall()

    conn.close()

    prisoner_counts = {row['status']: row['count'] for row in rows}
    return prisoner_counts

def get_total_prisoners():
    """
    Returns the total number of prisoners in the database.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT COUNT(*) FROM Prisoners"
    cursor.execute(query)
    total_prisoners = cursor.fetchone()[0]

    conn.close()
    return total_prisoners

def get_total_guard_count():
    """
    Returns the total number of guards in the database.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT COUNT(*) FROM Guards"
    cursor.execute(query)
    total_guards = cursor.fetchone()[0]

    conn.close()
    return total_guards

def get_total_incident_reports():
    """
    Returns the total number of incident reports in the database.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT COUNT(*) FROM IncidentReports"
    cursor.execute(query)
    total_incidents = cursor.fetchone()[0]

    conn.close()
    return total_incidents

def get_total_visitors():
    """
    Returns the total number of visitors in the database.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT COUNT(*) FROM Visitors"
    cursor.execute(query)
    total_visitors = cursor.fetchone()[0]

    conn.close()
    return total_visitors

def get_prisoner_sentence_summary():
    """
    Returns a summary of prisoner sentences, e.g., average, minimum, and maximum sentence lengths.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    SELECT AVG(sentence_length) as avg_sentence,
           MIN(sentence_length) as min_sentence,
           MAX(sentence_length) as max_sentence
    FROM Prisoners
    """
    cursor.execute(query)
    summary = cursor.fetchone()

    conn.close()
    return summary



if __name__ == "__main__":
    # Example usage
    # create_prisoner('nametest10', 'nametest11', '1990-01-01', 'Male', '2024-08-01', 'Released', 120)
    prisoner = read_prisoner(4)
    print(prisoner)
    # update_prisoner(1, first_name='Jonathan', last_name='Doe')
    # delete_prisoner(1)
