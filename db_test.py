from psycopg import connect

conn = connect(
    host="localhost",
    port="5432",
    dbname="jornada",
    user="postgres",
    password="postgres",
)

cur = conn.cursor()
cur.execute("SELECT 1")
print(cur.fetchone())
