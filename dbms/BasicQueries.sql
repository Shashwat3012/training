CREATE DATABASE shashwat_newdb;
USE shashwat_newdb;

CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    college VARCHAR(50)
);


INSERT INTO students VALUES
(1, 'Shashwat', 21, 'VESIT'),
(2, 'Harkirat', 22, 'VESIT'),
(3, 'Piyush', 21, 'VESIT'),
(4, 'Kunal', 23, 'VESIT');



SELECT * FROM students;
SELECT DISTINCT college FROM students;
SELECT * FROM students WHERE age = 21;
SELECT * FROM students WHERE age > 21 AND college = 'VESIT';
SELECT * FROM students ORDER BY age DESC;


UPDATE students SET age = 22 WHERE name = 'Shashwat';
DELETE FROM students WHERE name = 'Kunal';

SELECT * FROM students WHERE name LIKE 'S%';
SELECT * FROM students WHERE name IN ('Shashwat', 'Piyush');
SELECT * FROM students WHERE age BETWEEN 20 AND 22;
SELECT name AS student_name FROM students;

-- Select Top
SELECT * FROM students LIMIT 2;

-- SQL Injection
SELECT * FROM students WHERE name = '' OR 1=1;