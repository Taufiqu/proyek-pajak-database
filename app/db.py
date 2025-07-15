# backend/db.py
import psycopg2
from config import Config

def connect_db():
    try:
        connection = psycopg2.connect(
            user=Config.USER,
            password=Config.PASSWORD,
            host=Config.HOST,
            port=Config.PORT,
            dbname=Config.DBNAME
        )
        print("✅ Database connection successful!")
        return connection
    except Exception as e:
        print("❌ Failed to connect to the database:", e)
        return None

if __name__ == "__main__":
    conn = connect_db()
    if conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT NOW();")
            result = cursor.fetchone()
            print("📅 Current Time:", result)
        conn.close()
        print("🔒 Connection closed.")
        """Buat folder upload jika belum ada."""
        Config.init_app()