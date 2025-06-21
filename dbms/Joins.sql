CREATE TABLE scores (
    student_id INT,
    subject VARCHAR(50),
    marks INT
);

INSERT INTO scores VALUES
(1, 'DBMS', 85),
(1, 'OS', 80),
(2, 'DBMS', 70),
(3, 'OS', 90);

-- INNER JOIN
SELECT s.name, sc.subject, sc.marks
FROM students s
INNER JOIN scores sc ON s.id = sc.student_id;

-- LEFT JOIN
SELECT s.name, sc.subject, sc.marks
FROM students s
LEFT JOIN scores sc ON s.id = sc.student_id;

-- RIGHT JOIN
SELECT s.name, sc.subject, sc.marks
FROM students s
RIGHT JOIN scores sc ON s.id = sc.student_id;
