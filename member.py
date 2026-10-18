class Member:
    """Represents a library member."""

    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.issued_books = []  # list of book_ids currently held

    def issue_book(self, book_id):
        self.issued_books.append(book_id)

    def return_book(self, book_id):
        if book_id in self.issued_books:
            self.issued_books.remove(book_id)

    def __str__(self):
        return (f"[{self.member_id}] {self.name} ({self.email}) - "
                f"{len(self.issued_books)} book(s) issued")


if __name__ == "__main__":
    # quick sanity check for this week's module
    m = Member(1, "Rohith", "rohith@example.com")
    print(m)
    m.issue_book(101)
    print(m)
