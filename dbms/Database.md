# SQL 

## 1. Need for Database

Before databases, data was stored in text files or spreadsheets. This approach led to:

- Data redundancy (same data stored in multiple places)
- Data inconsistency (mismatch between versions)
- Difficulty in accessing or updating data
- No concurrency control or access management

A **Database Management System (DBMS)** solves these issues by:

- Centralizing and structuring data
- Enabling fast and secure data access
- Supporting concurrency and backup
- Enforcing integrity and reducing redundancy

Relational databases like MySQL, SQL Server, and PostgreSQL are built on the RDBMS concept, using **tables, keys, constraints**, and **SQL queries**.

---

## 2. Callable Statement, Prepared Statement, Stored Procedure

### Prepared Statement

- Used to execute **parameterized queries** securely.
- Compiles the query once and reuses it, improving performance.
- Prevents SQL injection attacks.

**Syntax Example:**

```sql
PREPARE stmt FROM 'SELECT * FROM students WHERE age > ?';
SET @min_age = 20;
EXECUTE stmt USING @min_age;
```

---

### Callable Statement

- Used to call **stored procedures** from SQL or application code.
- Accepts **IN**, **OUT**, and **INOUT** parameters.

**Syntax Example:**

```sql
CALL get_student_by_id(1);
```

---

### Stored Procedure

- A named set of SQL instructions stored in the database.
- Can accept parameters, return result sets, and include logic like IF/ELSE.

**Syntax Example:**

```sql
DELIMITER //
CREATE PROCEDURE get_student_by_id(IN student_id INT)
BEGIN
    SELECT * FROM students WHERE id = student_id;
END //
DELIMITER ;
```

Stored procedures improve modularity, performance, and reusability of SQL logic.

---

## 3. Normalization

Normalization is a process of organizing data to:

- Eliminate redundancy
- Improve data integrity
- Make updates more efficient

Normalization uses a series of **normal forms**, each adding stricter rules.

### 🔹 First Normal Form (1NF)
- All columns must have atomic (indivisible) values.
- No repeating groups.

**Bad:**

| ID | Name     | Subjects        |
|----|----------|-----------------|
| 1  | Shashwat | DBMS, OOP, OS   |

**Good (1NF):**

| ID | Name     | Subject |
|----|----------|---------|
| 1  | Shashwat | DBMS    |
| 1  | Shashwat | OOP     |
| 1  | Shashwat | OS      |

---

### 🔹 Second Normal Form (2NF)
- Must satisfy 1NF
- No **partial dependency** on part of a composite primary key

---

### 🔹 Third Normal Form (3NF)
- Must satisfy 2NF
- No **transitive dependency** (non-key fields depend only on the key)

---

**Example of Properly Normalized Structure:**

1. **Students Table**

| ID | Name     | Age | College |
|----|----------|-----|---------|
| 1  | Shashwat | 21  | VESIT   |

2. **Subjects Table**

| SubjectID | SubjectName |
|-----------|-------------|
| 101       | DBMS        |

3. **StudentSubjects Table**

| StudentID | SubjectID |
|-----------|-----------|
| 1         | 101       |

---

Normalization is critical to ensure clean, scalable database design in enterprise applications.
