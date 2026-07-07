# Chapter 13 Concepts: Django as the Web Application Layer

## Positioning in the Course

Chapter 12 introduced Django ORM and model classes as the data layer.

Chapters 12 and 13 share the same starter project reference so directory structure and models stay consistent:

- `starter-project/` in each chapter
- App: `operations`
- Core models: `Customer`, `Project`, `WorkItem`

Chapter 13 focuses on what happens when a user opens a URL in a browser:

1. Request arrives
2. URLconf selects a view
3. View reads/organizes data
4. Template renders output
5. Response is returned

For learners, this chapter is about exposing business data clearly, not about framework internals.

## Request-Response Pipeline (Practical View)

A Django app is a structured workflow for turning business questions into web pages.

- Request: browser asks for a path like `/orders/open/`
- URLconf: Django matches that path to a view
- View: Python logic prepares data and decides which template to use
- Template: HTML with placeholders displays the data
- Response: rendered page is returned to the user

This pipeline gives predictable boundaries between routing, logic, and presentation.

## MVC and Django MVT Mapping

Many teams often hear MVC. Django is usually described as MVT.

- Model (MVC) <-> Model (Django): business entities and data rules
- View (MVC) <-> Template (Django): what users see
- Controller (MVC) <-> View + URLconf (Django): request handling and flow control

The naming differs, but the business goal is the same: move data from storage to users in a controlled way.

## Connecting to Chapter 12 Models

In this chapter, model use stays light and practical.

Typical web-layer patterns:

- Query recent records for a dashboard
- Filter active/inactive items
- Build summary context for templates
- Handle basic form input before querying

You are not redesigning schema here. You are exposing already-modeled data to business users.

## Forms and Basic Input Handling

Basic request handling means:

- Reading query parameters for filtering
- Reading POST values from submitted forms
- Validating simple required fields
- Returning clear success/error feedback

The objective is dependable business workflow behavior, not advanced form internals.

## Admin as an Operations Tool

Django admin is productive because it provides:

- Quick list/detail views for records
- Search and filter for operational checks
- Controlled edits for business corrections

In many environments, this helps teams verify data and take action without building custom screens for every small task.

## What This Chapter Deliberately Avoids

- Deployment internals
- Advanced architecture patterns
- Middleware/deep lifecycle internals
- Complex security hardening flows

The emphasis remains concept-first and practical: routing, views, templates, forms, and admin-enabled operations.
