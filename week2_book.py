class Book:
    """Represents a single book in the library."""

    def __init__(self, book_id, title, author, isbn, total_copies=1):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        self.available_copies = total_copies

    def is_available(self):
        return self.available_copies > 0

    def issue_copy(self):
        if self.is_available():
            self.available_copies -= 1
            return True
        return False

    def return_copy(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        return False

    def __str__(self):
        return (f"[{self.book_id}] {self.title} by {self.author} "
                f"(ISBN: {self.isbn}) - {self.available_copies}/{self.total_copies} available")


if __name__ == "__main__":
    # quick sanity check for this week's module
    b = Book(1, "Clean Code", "Robert C. Martin", "9780132350884", total_copies=2)
    print(b)
    b.issue_copy()
    print(b)
