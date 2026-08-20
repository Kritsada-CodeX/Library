def create_tables():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS books (
        book_id TEXT PRIMARY KEY,
         title TEXT NOT NULL,
        author TEXT,
        category TEXT,
        status TEXT DEFAULT "available"
    )""")
    conn.commit()
    conn.close()