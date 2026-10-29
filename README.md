# Library Management System

A Library Management System built in Python using Object-Oriented
Programming. Being built and pushed module by module over 5 weeks.

## Progress

- [x] Week 1 — `Book` class
- [x] Week 2 — `Member` class
- [x] Week 3 — `Library` core engine (issue/return, dictionary lookups)
- [ ] Week 4 — Search + reporting
- [ ] Week 5 — Final polish, duplicate-entry protection

## This week: `Library` core engine

`Library` ties `Book` and `Member` together. Books and members are
stored in dictionaries keyed by `book_id` / `member_id`, so issuing or
returning a book is an O(1) average lookup instead of scanning a list.
`issue_book()` and `return_book()` validate availability and update
both the book and member state consistently.

```bash
python3 library.py
```
