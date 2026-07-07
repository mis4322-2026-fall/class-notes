# Section 13.3: Views and Data Exposure

## Overview

Views are where request input is translated into business output. This section shows how function-based and class-based views prepare template-ready context without overcomplicating architecture.

Map each walkthrough to files in `starter-project/operations/views.py`, `starter-project/operations/urls.py`, and `starter-project/operations/templates/`.

## Core Concepts

- Function-based views are direct and readable for small workflows.
- Class-based views provide reusable structure for repeated page patterns.
- Basic request handling usually means reading `GET` or `POST` values.
- Templates should receive already-prepared context, not raw business logic.
- Data exposure quality matters: users need clear summaries, not raw records only.

## Code Walkthrough (incremental)

Start with a small function-based view.

```python
def sales_list_view(request):
    region = request.GET.get("region")
    rows = SalesRecord.objects.all()
    if region:
        rows = rows.filter(region=region)
    return render(request, "sales/list.html", {"rows": rows, "region": region})
```

Add a class-based view for reusable summary behavior.

```python
class SalesSummaryView(View):
    template_name = "sales/summary.html"

    def get(self, request):
        total = SalesRecord.objects.filter(status="open").count()
        return render(request, self.template_name, {"open_count": total})
```

Both forms are valid. Choose based on complexity and team readability.

## Try It (optional)

Add one input filter (for example, minimum amount) to a list view and include the selected value in template context.

## Summary

Views are the translation layer between requests and business-facing pages. Strong context design makes template output more useful for decision-making.
