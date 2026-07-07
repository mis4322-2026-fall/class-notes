# Section 11.2: Classes and Objects

## Overview

This section introduces the class syntax itself. The goal is to understand what a class definition does, how `__init__` builds object state, and how object instances can be inspected after creation.

## Core Concepts

- A class defines a blueprint.
- An object is one instance created from that blueprint.
- `__init__` runs at instantiation time.
- `self` refers to the current object being created or used.
- Instance attributes are stored on each object separately.
- Objects can be inspected through attributes, `__dict__`, `__repr__`, and custom methods.

## Code Walkthrough (incremental)

Define a simple class.

```python
class Product:
    def __init__(self, sku, name, unit_price):
        self.sku = sku
        self.name = name
        self.unit_price = unit_price
```

Create two separate objects.

```python
printer = Product("P-100", "Laser Printer", 249.0)
monitor = Product("P-200", "24-inch Monitor", 189.0)
```

Each object keeps its own state.

```python
printer.name
monitor.name
```

Inspect the stored attributes directly.

```python
printer.__dict__
```

Add a readable representation.

```python
class Product:
    def __init__(self, sku, name, unit_price):
        self.sku = sku
        self.name = name
        self.unit_price = unit_price

    def __repr__(self):
        return f"Product(sku={self.sku!r}, name={self.name!r}, unit_price={self.unit_price!r})"
```

Now the object prints in a way that helps debugging and inspection.

```python
printer
```

The important idea is that class definitions create a repeatable model. Objects are the individual business entities built from that model.

## Try It (optional)

Create a simple `Customer` class with three attributes. Instantiate two objects and inspect their `__dict__` output. Notice that the class stays the same, but the object state differs.

## Summary

Classes define structure; objects hold actual data. `__init__` is the point where incoming values become instance attributes, and inspection tools make object state easier to understand.
