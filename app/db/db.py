import sqlite3

def init_db():
    conn = sqlite3.connect('motivation.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS quotes (id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT)''')
    conn.commit()
    conn.close()

def add_user(user_id):
    conn = sqlite3.connect('motivation.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO users (user_id) VALUES (?)', (user_id,))
    conn.commit()
    conn.close()

def get_all_users():
    conn = sqlite3.connect('motivation.db')
    cursor = conn.cursor()
    cursor.execute('SELECT user_id FROM users')
    users = [row[0] for row in cursor.fetchall()]
    conn.close()
    return users

def add_quote(text):
    conn = sqlite3.connect('motivation.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO quotes (text) VALUES (?)', (text,))
    conn.commit()
    conn.close()

def get_random_quote():
    conn = sqlite3.connect('motivation.db')
    cursor = conn.cursor()
    cursor.execute('SELECT text FROM quotes ORDER BY RANDOM() LIMIT 1')
    quote = cursor.fetchone()
    conn.close()
    return quote[0] if quote else None