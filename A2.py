def search_books(keyword):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM books
        WHERE title LIKE ? OR author LIKE ?
    """, (f"%{keyword}%", f"%{keyword}%"))
    rows = cur.fetchall()
    conn.close()
    return rows