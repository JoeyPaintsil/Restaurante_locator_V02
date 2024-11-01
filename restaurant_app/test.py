import psycopg2

try:
    connection = psycopg2.connect(
        dbname="railway",
        user="postgres",
        password="RtneJpSTVxuzpMAicUnwpjMazkuVqARX",
        host="postgres.railway.internal",  # Replace with public host if possible
        port="5432"
    )
    print("Connection successful")
except Exception as e:
    print("Connection failed:", e)
