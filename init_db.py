import sqlite3

conn = sqlite3.connect("app.db")
c = conn.cursor()

# --- Users table ---
c.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);
""")

# --- Quiz Scores table ---
c.execute("""
CREATE TABLE IF NOT EXISTS scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    module TEXT,
    score INTEGER,
    total INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(id)
);
""")

conn.commit()
conn.close()

print("Database initialized successfully!")
