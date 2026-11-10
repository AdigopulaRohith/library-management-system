# Library Management System

A Library Management System built in Python using Object-Oriented
Programming, developed and released module by module over 5 weeks.

## Progress

- [x] Week 1 — `Book` class
- [x] Week 2 — `Member` class
- [x] Week 3 — `Library` core engine (issue/return, dictionary lookups)
- [x] Week 4 — Search + reporting
- [x] Week 5 — Final polish, duplicate-entry protection ✅

## Features

- **Book management** — add/remove books, track total vs. available copies
- **Member management** — add/remove members, track issued books per member
- **Issue & Return** — with due-date tracking and validation
- **Search** — by title, author, or ISBN
- **Reports** — available books, books issued to a specific member
- **Transaction log** — every issue/return recorded with a timestamp
- **Duplicate protection** — repeat ISBNs add copies instead of duplicating; repeat member emails are rejected

See [IMPROVEMENTS.md](IMPROVEMENTS.md) for the specific drawbacks found
and fixed in this final pass.

## Project Structure

```
book.py       # Book class
member.py     # Member class
library.py    # Library class — core OOP logic
main.py       # Demo script
IMPROVEMENTS.md
```

## Getting Started

```bash
python3 main.py
```

## Possible Extensions

- Persist data to a file or database (SQLite/JSON)
- Fine calculation for overdue books
- CLI menu or REST API layer on top of `Library`
- Unit tests for `Book`, `Member`, and `Library`

## License

MIT
