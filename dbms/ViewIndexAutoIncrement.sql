CREATE TABLE auto_students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50)
);

CREATE INDEX idx_age ON students(age);

CREATE VIEW vesit_students AS
SELECT name, age FROM students WHERE college = 'VESIT';
