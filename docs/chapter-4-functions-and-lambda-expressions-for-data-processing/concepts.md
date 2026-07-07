# Concepts

Chapter 4 focuses on writing reusable logic for data work. In business contexts, the same transformation patterns appear repeatedly: clean input values, compute metrics, group records, and produce summaries. Functions and lambda expressions help you express those patterns clearly.

## Function Fundamentals for Data Work

Functions package a process behind a meaningful name. Instead of repeating list and dictionary logic across a script, you define one function and call it whenever needed.

Key ideas:
- Parameters define what data the function needs.
- Return values define what result the function produces.
- A clear function name communicates business intent.

## Function Design for Lists and Dictionaries

Most business data in Python appears as lists of records (dictionaries). Well-designed functions:
- Accept predictable input shapes.
- Handle missing or empty data safely.
- Return structured output that downstream code can trust.

Function design is not only about correctness. It is also about maintainability and testability.

## Lambda Expressions

A lambda is a compact anonymous function, useful for small one-step operations where naming a full function would add noise.

Common uses include:
- `sorted(..., key=lambda item: ...)`
- `filter(lambda item: ..., records)`
- `map(lambda item: ..., records)`

Lambdas are best when the logic is short and obvious. If logic grows beyond a simple expression, use a named function.

## Functions and Lambdas in Data Pipelines

Data pipelines often follow a repeatable sequence:
1. Filter records.
2. Transform fields.
3. Aggregate results.
4. Format output.

Named functions provide structure for major stages, while lambdas can keep simple key, filter, or mapping operations concise. Together, they support clean, testable data processing that scales to later topics such as CSV, APIs, and Pandas.

## Why This Matters

Professionals frequently need reliable reporting logic that can be reused across datasets and periods. Function-based design reduces copy-paste errors, improves readability, and makes business rules easier to verify.
