# Micro Center

A desktop inventory & repair-order management app built with CustomTkinter, with a MySQL backend. Supports Admin/Employee login roles, stock tracking, order tracking, and add/update/delete/search across both tables.

## Features

- Role-based login (Admin / Employee)
- Live dashboard (total stock, orders, completed orders)
- Add / update / delete / search records for Stock and Orders tables
- Custom dark theme (forest-dark ttk theme)

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Create a `.env` file in the project root (see `.env.example`) with your MySQL credentials.
3. Run:
   ```
   python app.py
   ```

## Managing users and passwords

Login credentials are stored directly in `app.py`, in the login page section near the top of the file:

```python
au=["A001","A002"]
eu=["E001","E002"]
apas=["admlogin123"]
epas=["emplogin123"]
```

- `au` / `eu` are the valid Admin / Employee usernames.
- `apas` / `epas` are the valid Admin / Employee passwords.

To add or change a user, edit these lists directly and save the file:

- **Add a username**: append it to `au` or `eu`, e.g. `au=["A001","A002","A003"]`.
- **Add/change a password**: append or edit an entry in `apas` or `epas`.

## Security notes

This started as a school project and has since been cleaned up a bit for a public repo:

- DB credentials are read from `.env` (not committed) instead of being hardcoded.
- Login usernames/passwords are still plaintext lists in `app.py` (see above) — fine for a local school project, but if this were ever exposed to real users, hashing the passwords (e.g. with `bcrypt`) would be the next step.
