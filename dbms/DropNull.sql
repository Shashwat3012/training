-- NULL values
INSERT INTO students (id, name, age, college) VALUES (5, 'New', NULL, NULL);

SELECT * FROM students WHERE age IS NULL;

-- GROUP BY
SELECT age, COUNT(*) FROM students GROUP BY age;

-- HAVING
SELECT age, COUNT(*) as total FROM students GROUP BY age HAVING total > 1;

-- NULL functions
SELECT IFNULL(college, 'No College') FROM students;

-- ALTER
ALTER TABLE students ADD gender VARCHAR(10);

-- DROP
DROP TABLE test_constraints;
