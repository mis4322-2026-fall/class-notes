# Section 12.4: CRUD Operations

## Overview

CRUD means create, read, update, and delete. Django ORM provides direct methods for each step, and Django admin gives a quick interface to inspect and edit records without building custom screens first.

Run these examples in the chapter `starter-project/` so CRUD and admin behavior stays aligned with the same `operations` app structure used in Chapter 13.

## Core Concepts

- Create with `Model.objects.create(...)`.
- Read with `get`, `filter`, and list-style querysets.
- Update by changing attributes and calling `save()`.
- Delete with `delete()`.
- Django admin is a practical UI for lightweight data management.

## Code Walkthrough (incremental)

Create a new invoice.

```python
invoice = Invoice.objects.create(
    invoice_number="INV-9001",
    customer_code="C-100",
    amount=1250.00,
    status="draft",
)
```

Read it back.

```python
invoice = Invoice.objects.get(invoice_number="INV-9001")
```

Update and save.

```python
invoice.status = "paid"
invoice.save()
```

Delete when no longer needed.

```python
invoice.delete()
```

Register models in admin.

```python
from django.contrib import admin
from .models import Invoice


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("invoice_number", "customer_code", "amount", "status")
    list_filter = ("status",)
    search_fields = ("invoice_number", "customer_code")
```

Launch admin and verify records visually.

```bash
python manage.py createsuperuser
python manage.py runserver
```

Then open `/admin` in the browser, sign in, and inspect invoice rows.

## Try It (optional)

Create one `Customer` and one `Invoice`, then use Django admin to edit the invoice status from `draft` to `paid`.

## Summary

CRUD operations and Django admin complete the class-to-data workflow: define a model class, operate on object records through ORM methods, and validate outcomes quickly in a practical UI.
