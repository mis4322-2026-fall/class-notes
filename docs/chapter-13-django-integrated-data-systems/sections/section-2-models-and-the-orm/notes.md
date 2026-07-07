# Section 13.2: Models and the ORM

## Overview

This section revisits models and ORM from Chapter 12, but now from a web-view perspective. The goal is not schema design; the goal is retrieving business data that pages can display.

Keep using the same `starter-project/operations/models.py` models so web-layer examples stay consistent with Chapter 12.

## Core Concepts

- Views should call model queries to retrieve records needed for one page.
- Keep query intent simple: filter, order, and slice for business relevance.
- Convert query results into context dictionaries for templates.
- Keep model concerns (field definitions, relationships) in the model layer.
- Keep presentation concerns (labels, table headers, formatting) in templates.

## Code Walkthrough (incremental)

Start with a focused ORM query for one business page.

```python
open_invoices = Invoice.objects.filter(status="open").order_by("-due_date")[:10]
```

Then prepare view context.

```python
context = {
    "title": "Open Invoices",
    "invoice_rows": open_invoices,
    "open_total": sum(invoice.amount for invoice in open_invoices),
}
```

Return the context to a template.

```python
return render(request, "billing/open_invoices.html", context)
```

This pattern keeps data retrieval and page rendering connected but cleanly separated.

## Try It (optional)

Take one Chapter 12 query and place it inside a mock view. Add one context key that would help a manager interpret the records quickly.

## Summary

Section 2 connects ORM knowledge to practical web output: query what the page needs, shape context clearly, and hand it to templates.
