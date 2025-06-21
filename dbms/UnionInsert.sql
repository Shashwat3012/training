SELECT * FROM scores;


SELECT name as n FROM students
UNION
SELECT subject as s FROM scores;

-- SELECT INTO
CREATE TABLE copy_students AS
SELECT * FROM students;

-- INSERT INTO SELECT
INSERT INTO copy_students
SELECT * FROM students WHERE age > 21;
