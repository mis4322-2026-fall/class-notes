# Section 13.1: Django as a Framework

## Overview

This section explains Django as a structured web workflow rather than a collection of isolated files. You will follow the path from browser request to rendered response.

Use `starter-project/` as the reference directory structure while reading this section (`mis_portal`, `operations`, templates).

## Core Concepts

- Django processes each page through a request-response pipeline.
- URLconf decides which view handles a path.
- A view organizes business data and selects a template.
- A template formats that data for user-facing presentation.
- Django's MVT language maps closely to familiar MVC ideas.

## Code Walkthrough (incremental)

Start with a URL pattern that maps business paths to views.

```python
urlpatterns = [
    path("orders/open/", views.open_orders_view, name="open-orders"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
]
```

Now build a minimal view that returns data to a template.

```python
def open_orders_view(request):
    context = {"title": "Open Orders", "count": 12}
    return render(request, "orders/open_orders.html", context)
```

Finally, render that context in a template.

```html
<h1>{{ title }}</h1>
<p>Total open orders: {{ count }}</p>
```

The same pattern repeats for most business screens.

## Try It (optional)

Use `python manage.py runserver` and visit two different URLs in your app. Identify which URL pattern and view each page uses.

## Summary

Django gives a predictable path from request to response. Understanding this flow is the foundation for adding data exposure, forms, and admin productivity in later sections.
