# Improvements — Week 5

Reviewed the project against a similar public implementation and
addressed a few common issues:

| Issue | Fix |
|---|---|
| Linear list scans for lookups | `books` / `members` stored in dicts keyed by ID → O(1) average lookup |
| No search by title/author | Added `search_by_title()`, `search_by_author()`, `search_by_isbn()` |
| Duplicate ISBNs created a second, separate book entry | `add_book()` now merges copies into the existing entry for that ISBN |
| Duplicate members could be registered with the same email | `add_member()` now rejects a duplicate email |
| No due dates or transaction history | Issue/return events are logged with timestamps; issuing sets a 14-day due date |

These changes don't alter the public API used in earlier weeks — the
same `add_book`, `issue_book`, `return_book`, `search_by_title`, etc.
calls from Week 3/4 all still work the same way, just more robustly.
