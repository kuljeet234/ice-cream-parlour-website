# ice-cream-parlour-website

A Django 4.2 starter for a small ice-cream parlour — themed home / about /
services pages, an admin-managed menu, and a basic order tracking flow.

## Setup

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

cd hello
python manage.py migrate
python manage.py createsuperuser   # for /admin
python manage.py runserver
```

Visit http://127.0.0.1:8000/.

## What's wired up

- `home.IceCream(name, flavor, price, is_available, description)` — the menu;
  edit through `/admin`. Available items are surfaced on the home page as
  `menu`.
- `home.Order` — UUID-tracked orders with `customer_name`, `customer_email`,
  `customer_phone`, an `IceCream` foreign key, `quantity`, and a status
  enum (PENDING / PREPARING / READY / DELIVERED / CANCELLED). Includes a
  `total_price` property.
- `home.ContactSubmission` — captured by the `/contact` form (ModelForm
  validation, server-side message length cap, Bootstrap success/error alerts).
- `/orders` lists every order, newest first, with a `select_related` join
  on the menu item.
- `/trackorders?id=<uuid>` looks up a single order by tracking ID.
