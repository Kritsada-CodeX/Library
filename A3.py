def can_borrow(book_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT status FROM books WHERE book_id=?",
(book_id,))
    book = cur.fetchone()
    conn.close()

    if book is None:
        return False, "ไม่พบรหัสหนังสือนี้"
    if book["status"] != "available":
        return False, "หนังสือเล่มนี้ถูกยืมอยู่"
    return True, "สามารถยืมได้"