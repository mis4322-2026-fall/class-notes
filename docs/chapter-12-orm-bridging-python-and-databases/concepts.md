# Chapter 12 Concepts: ORM as a Class-Based Data Layer

## Why This Chapter Matters After Chapter 11

In Chapter 11, you practiced classes, objects, attributes, and methods for business entities.

ORM continues that same idea, but now objects can represent persistent data. Instead of manually writing SQL for every operation, you define a model class once and interact with data through Python objects and query methods.

For learners, this reduces friction between business logic and data handling.

## ORM in One Sentence

An ORM (Object-Relational Mapper) maps relational data to class-based objects so that developers can work mainly in Python while the framework handles SQL translation.

## Django ORM in This Course

This chapter uses Django ORM as the concrete example.

All walkthroughs and exercises in Chapters 12 and 13 use the same starter project reference:

- `starter-project/` in this chapter folder
- Shared app name: `operations`
- Shared model vocabulary: `Customer`, `Project`, `WorkItem`

At a high level:

1. You define a model class (for example, `Customer` or `Invoice`).
2. Django maps class fields to table columns.
3. You use ORM methods like `create`, `filter`, `get`, `save`, and `delete`.
4. You can inspect and edit records quickly in Django admin.

## Brief Setup Only

A full Django chapter comes later. For this chapter, setup is intentionally lightweight:

```bash
pip install django
django-admin startproject orm_intro_project
cd orm_intro_project
python manage.py startapp operations
```

Then add your app to `INSTALLED_APPS`, define model classes, run migrations, and use admin for quick record checks.

## OOP Connection You Should Keep in Mind

- Class definition: model blueprint.
- Object instance: one row-like entity.
- Attribute: one field value.
- Method call: one business action or data operation.

ORM does not replace OOP thinking. It applies OOP to persistence work.

## What This Chapter Does Not Cover

- Deep schema optimization.
- Advanced Django architecture.
- Performance tuning internals.

The focus is conceptual fluency plus practical first steps with model classes, CRUD, and admin.
