from dataclasses import dataclasses

@dataclasses
class Book:
    Book_id: str
    title: str
    author: str
    category: str
    status: str = "available"

@dataclasses
class Member:
    Member_id: str
    name: str
    classroom: str
    phone: str = ""
    