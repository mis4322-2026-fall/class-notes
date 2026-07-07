# Section 11.4: Modeling Data with Classes

## Overview

This section brings the chapter together by modeling related business entities with classes. The emphasis is not advanced OOP theory. The emphasis is practical data modeling: one object can represent one business entity, and relationships between objects can mirror relationships between records.

## Core Concepts

- A class can represent one row-like entity such as a customer, invoice, task, or project.
- Objects can hold references to other objects.
- A collection of objects can model one-to-many relationships.
- Class methods can expose row-like views for export or reporting.
- This object model previews the core ORM idea used in Chapter 12.

## Code Walkthrough (incremental)

Start with two related classes.

```python
class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name


class Invoice:
    def __init__(self, invoice_id, customer, amount, paid=False):
        self.invoice_id = invoice_id
        self.customer = customer
        self.amount = amount
        self.paid = paid
```

Create one customer and two invoices tied to that customer.

```python
customer = Customer("C-200", "Acme Health")

invoice_a = Invoice("INV-1", customer, 800.0)
invoice_b = Invoice("INV-2", customer, 1200.0, paid=True)
```

Each invoice now points to a customer object instead of carrying duplicate customer fields everywhere.

```python
invoice_a.customer.name
invoice_b.customer.customer_id
```

Add behavior that returns a row-like export.

```python
class Invoice:
    def __init__(self, invoice_id, customer, amount, paid=False):
        self.invoice_id = invoice_id
        self.customer = customer
        self.amount = amount
        self.paid = paid

    def export_row(self):
        return {
            "invoice_id": self.invoice_id,
            "customer_id": self.customer.customer_id,
            "customer_name": self.customer.name,
            "amount": self.amount,
            "paid": self.paid,
        }
```

This is the important bridge to ORM thinking. In the next chapter, database rows will be mapped into Python objects with fields and relationships. The mental model is the same:

- one object represents one entity
- object attributes hold field values
- object relationships represent related records

## Try It (optional)

Sketch a tiny data model for `Project` and `Task`. Decide which fields belong to each class and how one project should keep track of many task objects.

## Summary

Modeling data with classes makes Python code look more like the business system it represents. That is why classes are such a useful bridge into ORM work: they let you think in terms of entities, fields, and relationships before a database library is even involved.
