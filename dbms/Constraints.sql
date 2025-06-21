CREATE TABLE test_constraints (
    id INT NOT NULL UNIQUE,
    name VARCHAR(50) DEFAULT 'Shashwat',
    age INT CHECK (age >= 18)
);

ALTER TABLE students ADD CONSTRAINT fk_score FOREIGN KEY (id) REFERENCES scores(student_id);
