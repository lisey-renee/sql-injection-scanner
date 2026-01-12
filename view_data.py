import sqlite3

# Connect to the database
conn = sqlite3.connect('scan_results.db')
cursor = conn.cursor()

# Run a SQL query to get everything from the 'scans' table
cursor.execute("SELECT * FROM scans")
rows = cursor.fetchall()

print("--- DATABASE ENTRIES ---")
for row in rows:
    print(f"URL: {row[0]} | Payload: {row[1]} | Status: {row[2]}")

conn.close()
