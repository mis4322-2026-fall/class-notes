# Chapter 11 Concepts

Object-oriented programming in Python is most helpful when your program stops feeling like a collection of simple values and starts feeling like a collection of business entities.

In earlier chapters, dictionaries and lists were enough for many tasks. That works well when data is small, flat, and short-lived. But once the same kind of record appears in many places, the cost of staying with raw dictionaries rises:

- The same keys must be remembered everywhere.
- Validation rules get repeated across functions.
- Related calculations drift apart.
- It becomes harder to tell what behavior belongs to which kind of record.

Consider a plain dictionary model for an invoice:

```python
invoice = {
    "invoice_id": "INV-204",
    "customer_name": "Northwind Office Supply",
    "amount": 1800.0,
    "paid": False,
}
```

This is fine at first. The difficulty appears when multiple parts of a program need to answer questions such as:

- How much is still due?
- Can this invoice be marked paid?
- How should this invoice display in a report?

If each answer lives in a different function, the model becomes harder to maintain. A class gives those rules a home.

```python
class Invoice:
    def __init__(self, invoice_id, customer_name, amount, paid=False):
        self.invoice_id = invoice_id
        self.customer_name = customer_name
        self.amount = amount
        self.paid = paid

    def amount_due(self):
        return 0 if self.paid else self.amount
```

Now the invoice data and invoice behavior stay together.

## Why Classes Help

Classes help in four practical ways:

1. They define a repeatable structure for similar records.
2. They make business rules easier to locate and reuse.
3. They make state changes explicit through methods.
4. They prepare you to think about one object as one entity in a system.

That last point matters for Chapter 12. In ORM work, one Python object often represents one database row-like entity. A `Customer` object can stand in for one customer record. An `Invoice` object can stand in for one invoice record. A relationship between objects can preview a relationship between tables.

## Core Building Blocks

The class concept in Python centers on a few ideas:

- A class is a blueprint for creating objects.
- An object is one instance of that class.
- `__init__` runs when a new object is created and usually stores incoming values on `self`.
- Instance attributes hold the object state.
- Instance methods read or update that state.
- Special methods such as `__str__` and `__repr__` make objects easier to inspect.

## What This Chapter Emphasizes

This chapter does not treat OOP as a survey of advanced patterns. The focus is narrower and more useful for learners:

- constructor use
- instance attributes
- instance methods
- updating state
- simple validation
- readable object output
- small object relationships

That foundation is enough to make the next step natural: mapping business rows from a database into Python objects.
