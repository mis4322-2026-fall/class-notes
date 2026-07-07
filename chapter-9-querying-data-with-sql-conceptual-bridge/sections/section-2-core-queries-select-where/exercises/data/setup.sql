PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS departments;

CREATE TABLE departments (
    department_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL,
    cohort_year INTEGER NOT NULL,
    major_dept_id INTEGER NOT NULL,
    FOREIGN KEY (major_dept_id) REFERENCES departments(department_id)
);

CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    course_code TEXT NOT NULL UNIQUE,
    title TEXT NOT NULL,
    department_id INTEGER NOT NULL,
    credits INTEGER NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    term TEXT NOT NULL,
    grade_point REAL NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

INSERT INTO departments (department_id, name) VALUES
    (1, 'Information Systems'),
    (2, 'Finance'),
    (3, 'Marketing');

INSERT INTO students (student_id, full_name, cohort_year, major_dept_id) VALUES
    (1, 'Ana Silva', 2024, 1),
    (2, 'Bruno Costa', 2023, 1),
    (3, 'Carla Gomez', 2024, 2),
    (4, 'Diego Lima', 2022, 3),
    (5, 'Elena Ruiz', 2024, 1),
    (6, 'Fatima Noor', 2025, 1);

INSERT INTO courses (course_id, course_code, title, department_id, credits) VALUES
    (101, 'MIS201', 'Data Management', 1, 3),
    (102, 'MIS310', 'Business Analytics', 1, 3),
    (103, 'FIN220', 'Corporate Finance', 2, 3),
    (104, 'MKT205', 'Digital Marketing', 3, 3),
    (105, 'MIS330', 'Data Warehousing', 1, 3);

INSERT INTO enrollments (enrollment_id, student_id, course_id, term, grade_point) VALUES
    (1, 1, 101, '2026-Spring', 3.7),
    (2, 1, 102, '2026-Spring', 3.9),
    (3, 2, 101, '2026-Spring', 3.2),
    (4, 3, 103, '2026-Spring', 3.8),
    (5, 4, 104, '2026-Spring', 3.1),
    (6, 5, 101, '2026-Spring', 3.6),
    (7, 5, 105, '2026-Spring', 3.8),
    (8, 2, 105, '2026-Spring', 3.4),
    (9, 3, 102, '2026-Fall', 3.5),
    (10, 1, 105, '2026-Fall', 4.0);
