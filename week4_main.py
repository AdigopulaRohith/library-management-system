from library import Library


def print_books(books):
    if not books:
        print("No books found.")
    for b in books:
        print(f"  {b}")


def demo():
    lib = Library()

    lib.add_book("The Pragmatic Programmer", "David Thomas", "9780135957059", 2)
    lib.add_book("Clean Code", "Robert C. Martin", "9780132350884", 1)
    lib.add_book("Introduction to Algorithms", "Cormen et al.", "9780262033848", 3)

    lib.add_member("Rohith", "rohith@example.com")
    lib.add_member("Aditi", "aditi@example.com")

    print("\n--- Issuing books ---")
    lib.issue_book(book_id=1, member_id=1)
    lib.issue_book(book_id=2, member_id=1)
    lib.issue_book(book_id=2, member_id=2)  # no copies left, should fail

    print("\n--- Searching ---")
    print("Search by title 'clean':")
    print_books(lib.search_by_title("clean"))

    print("\nSearch by author 'cormen':")
    print_books(lib.search_by_author("cormen"))

    print("\n--- Returning books ---")
    lib.return_book(book_id=1, member_id=1)

    print("\n--- Available books ---")
    print_books(lib.list_available_books())

    print("\n--- Books issued to Rohith ---")
    print_books(lib.list_member_books(member_id=1))


if __name__ == "__main__":
    demo()
