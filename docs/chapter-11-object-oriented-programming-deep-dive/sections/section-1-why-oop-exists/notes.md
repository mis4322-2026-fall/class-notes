# Section 11.1: Why OOP Exists

## Overview

Object-oriented programming becomes useful when a program is no longer just processing values and is instead managing many related business entities. In data and operations work, those entities often look familiar: customer, invoice, employee, ticket, product, or project.

## Core Concepts

- A dictionary can store a record, but it does not define what behavior belongs with that record.
- As programs grow, repeated key access and duplicated business rules make dictionary-only models harder to maintain.
- A class gives one place to define structure and behavior together.
- One object can stand for one business entity, which is the mental bridge to ORM work.

## Code Walkthrough (incremental)

Start with a plain dictionary.

```python
invoice = {
    "invoice_id": "INV-301",
    "customer_name": "Atlas Retail",
    "amount": 950.0,
    "paid": False,
}
```

This works, but business logic now has to live somewhere else.

```python
def amount_due(invoice_record):
    return 0 if invoice_record["paid"] else invoice_record["amount"]


def display_label(invoice_record):
    status = "PAID" if invoice_record["paid"] else "OPEN"
    return f"{invoice_record['invoice_id']} - {status}"
```

Those functions are still manageable for one entity type. The problem appears when every entity type starts collecting detached helper functions.

Move the logic into a class.

```python
class InvoiceRecord:
    def __init__(self, invoice_id, customer_name, amount, paid=False):
        self.invoice_id = invoice_id
        self.customer_name = customer_name
        self.amount = amount
        self.paid = paid

    def amount_due(self):
        return 0 if self.paid else self.amount

    def display_label(self):
        status = "PAID" if self.paid else "OPEN"
        return f"{self.invoice_id} - {status}"
```

Now create one object.

```python
invoice = InvoiceRecord("INV-301", "Atlas Retail", 950.0)
```

Read behavior from the object itself.

```python
due_now = invoice.amount_due()
label = invoice.display_label()
```

The main advantage is not syntax alone. The advantage is maintainability: the invoice rules stay with the invoice model.

## Try It (optional)

Take one dictionary-based business record you have seen before, such as a customer or ticket, and list three pieces of behavior that should probably live with that entity instead of being scattered across separate functions.

## Summary

OOP exists because growing programs need better organization. Classes help when data and behavior should travel together, especially when one Python object represents one meaningful business entity.
