
from database import create_tables
from services import add_book, search_books

def main_menu():
    while True:
        print("\n=== Library System ===")
        print("1. เพิ่มหนังสือ")
        print("2. ค้นหาหนังสือ")
        print("0. ออกจากระบบ")
        choice = input("เลือกเมนู: ")

        if choice == "0":
            break

create_tables()
main_menu()