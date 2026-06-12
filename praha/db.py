import psycopg

def connect():
    try:
        conn = psycopg.connect(
            dbname="obce",
            user="student",
            password="student",
            host="localhost",
            port=5432
        )
        return conn
    except Exception as e:
        print("Chyba DB:", e)
        return None