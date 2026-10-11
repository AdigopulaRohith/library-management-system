# Library Management System

A Library Management System built in Python using Object-Oriented
Programming. Being built and pushed module by module over 5 weeks.

## Progress

- [x] Week 1 — `Book` class
- [ ] Week 2 — `Member` class
- [ ] Week 3 — `Library` core engine (issue/return, dictionary lookups)
- [ ] Week 4 — Search + reporting
- [ ] Week 5 — Final polish, duplicate-entry protection

## This week: `Book`

`Book` models a single title in the library — title, author, ISBN,
and how many copies are available vs. total. It exposes `issue_copy()`
and `return_copy()` so copy counts stay consistent no matter what calls
them later.

```bash
python3 book.py
```
