import sqlite3

# Database connection
conn = sqlite3.connect("user_data.db")
c = conn.cursor()

# Create table (if it doesn't exist)
c.execute('''CREATE TABLE IF NOT EXISTS users (
                email text PRIMARY KEY,
                password_hash text NOT NULL
             )''')

# Commit changes and close connection
conn.commit()
conn.close()

print("Database and table created successfully!")
