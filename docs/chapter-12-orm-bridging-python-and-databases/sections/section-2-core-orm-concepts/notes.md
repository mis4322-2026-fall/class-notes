# Section 12.2: Core ORM Concepts

## Overview

Django ORM starts with model classes. A model is a class that describes business data fields and behavior in one place.

For consistency, read this section against `starter-project/operations/models.py`.

## Core Concepts

- A Django model class extends `models.Model`.
- Class attributes define fields (for example, text, numeric, date).
- One model instance represents one row-like record.
- Model methods can hold useful display or business logic.
- Migrations apply model changes to the database structure.

## Code Walkthrough (incremental)

Define a small model class.

```python
from django.db import models


class Customer(models.Model):
    customer_code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)
    credit_limit = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.customer_code} - {self.name}"
```

Read this with Chapter 11 vocabulary:

- `Customer` is the class blueprint.
- `customer_code`, `name`, and other fields become object attributes.
- `__str__` improves readability when objects are listed.

Apply changes with migrations.

```bash
python manage.py makemigrations
python manage.py migrate
```

## Try It (optional)

Add one extra field to the model (for example, `segment`) and write one sentence about how that field appears as an attribute on each object instance.

## Summary

Model classes are the center of Django ORM. They keep data structure and object behavior close together, reinforcing OOP principles from the previous chapter.
