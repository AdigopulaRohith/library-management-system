# Library Management System

A Library Management System built in Python using Object-Oriented
Programming. Being built and pushed module by module over 5 weeks.

## Progress

- [x] Week 1 — `Book` class
- [x] Week 2 — `Member` class
- [ ] Week 3 — `Library` core engine (issue/return, dictionary lookups)
- [ ] Week 4 — Search + reporting
- [ ] Week 5 — Final polish, duplicate-entry protection

## This week: `Member`

`Member` tracks a borrower's own state — the list of `book_id`s they
currently hold — kept separate from `Book`'s state. This separation
keeps each class focused on one responsibility, and makes it easy to
build the `Library` engine (next week) on top of both.

```bash
python3 member.py
```
