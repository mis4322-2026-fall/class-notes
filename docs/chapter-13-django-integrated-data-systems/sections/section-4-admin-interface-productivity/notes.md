# Section 13.4: Admin Interface & Productivity

## Overview

Django admin helps teams operate data quickly while the full web app is still evolving. In business contexts, this supports daily tasks like status correction, record verification, and exception handling.

Use the same `starter-project/operations/admin.py` file for all admin examples so configuration remains tied to the shared models.

## Core Concepts

- Admin is an operational interface, not the primary customer-facing UI.
- `list_display`, `list_filter`, and `search_fields` improve daily data workflows.
- Admin actions can speed repetitive updates with controlled logic.
- Admin and web views should complement each other in the same workflow.
- Keep admin configuration practical and business-oriented.

## Code Walkthrough (incremental)

Register a model for admin use.

```python
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("customer_code", "name", "tier", "is_active")
```

Add filters and search for faster operations.

```python
list_filter = ("tier", "is_active")
search_fields = ("customer_code", "name", "account_manager")
```

Add a small action for operational cleanup.

```python
@admin.action(description="Deactivate selected customers")
def deactivate_customers(modeladmin, request, queryset):
    queryset.update(is_active=False)
```

These changes reduce time-to-action for business teams.

## Try It (optional)

Pick one model from Chapter 12 and define `list_display` fields that would help a manager review records quickly.

## Summary

Admin improves operational productivity by making common inspection and update tasks fast, searchable, and consistent.
