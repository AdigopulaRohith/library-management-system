from datetime import datetime, timedelta
from book import Book
from member import Member


class Library:
    """Core Library Management System.

    Books and members are stored in dictionaries keyed by ID, giving
    O(1) average lookups instead of scanning a list.
    """

    LOAN_PERIOD_DAYS = 14

    def __init__(self):
        self.books = {}      # book_id -> Book
        self.members = {}    # member_id -> Member
        self.transactions = []
        self._next_book_id = 1
        self._next_member_id = 1

    # ---------- Book management ----------

    def add_book(self, title, author, isbn, total_copies=1):
        book_id = self._next_book_id
        self.books[book_id] = Book(book_id, title, author, isbn, total_copies)
        self._next_book_id += 1
        print(f"Added book: {self.books[book_id]}")
        return book_id

    # ---------- Member management ----------

    def add_member(self, name, email):
        member_id = self._next_member_id
        self.members[member_id] = Member(member_id, name, email)
        self._next_member_id += 1
        print(f"Added member: {self.members[member_id]}")
        return member_id

    # ---------- Issue / Return ----------

    def issue_book(self, book_id, member_id):
        book = self.books.get(book_id)
        member = self.members.get(member_id)

        if not book:
            print("Book not found.")
            return False
        if not member:
            print("Member not found.")
            return False
        if not book.is_available():
            print(f"'{book.title}' has no available copies right now.")
            return False

        book.issue_copy()
        member.issue_book(book_id)

        due_date = datetime.now() + timedelta(days=self.LOAN_PERIOD_DAYS)
        self.transactions.append({
            "type": "ISSUE", "book_id": book_id, "member_id": member_id,
            "date": datetime.now(), "due_date": due_date,
        })
        print(f"Issued '{book.title}' to {member.name}. Due: {due_date.strftime('%Y-%m-%d')}")
        return True

    def return_book(self, book_id, member_id):
        book = self.books.get(book_id)
        member = self.members.get(member_id)

        if not book or not member:
            print("Book or member not found.")
            return False
        if book_id not in member.issued_books:
            print(f"{member.name} does not currently have '{book.title}'.")
            return False

        book.return_copy()
        member.return_book(book_id)

        self.transactions.append({
            "type": "RETURN", "book_id": book_id, "member_id": member_id,
            "date": datetime.now(),
        })
        print(f"'{book.title}' returned by {member.name}.")
        return True


if __name__ == "__main__":
    # quick sanity check for this week's module
    lib = Library()
    bid = lib.add_book("Clean Code", "Robert C. Martin", "9780132350884", 1)
    mid = lib.add_member("Rohith", "rohith@example.com")
    lib.issue_book(bid, mid)
    lib.issue_book(bid, mid)  # should fail, no copies left
    lib.return_book(bid, mid)
