package Exceptions;

import java.io.*;
import java.util.*;

public class StudentManager {

    // Student class to hold data
    static class Student {
        String name;
        int age;
        String college;

        Student(String name, int age, String college) {
            this.name = name;
            this.age = age;
            this.college = college;
        }

        public String toCSV() {
            return name + "," + age + "," + college;
        }
    }

    // Custom Checked Exception
    static class InvalidAgeException extends Exception {
        public InvalidAgeException(String msg) {
            super(msg);
        }
    }

    // Custom Unchecked Exception
    static class CollegeMismatchException extends RuntimeException {
        public CollegeMismatchException(String msg) {
            super(msg);
        }
    }

    // Custom Wrapper Exception
    static class DataWriteException extends Exception {
        public DataWriteException(String msg, Throwable cause) {
            super(msg, cause);
        }
    }

    // Validate input (throws checked and unchecked exceptions)
    public void validateStudent(Student s) throws InvalidAgeException {
        if (s.age < 18 || s.age > 30)
            throw new InvalidAgeException("Invalid age for student: " + s.age);
        if (!"VESIT".equalsIgnoreCase(s.college))
            throw new CollegeMismatchException("Only VESIT students allowed. Got: " + s.college);
    }

    // Simulate saving to file (may throw checked exception)
    public void saveStudent(Student s) throws DataWriteException {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("students.csv", true))) {
            writer.write(s.toCSV());
            writer.newLine();
        } catch (IOException e) {
            throw new DataWriteException("Could not save student to file.", e);
        }
    }

    // Register student — combines validation and persistence
    public void register(Student s) throws InvalidAgeException, DataWriteException {
        validateStudent(s);
        saveStudent(s);
    }

    // Demonstrate Hierarchy of Exceptions
    public void hierarchyDemo() {
        try {
            int[] nums = {1, 2, 3};
            System.out.println(nums[5]); // Triggers ArrayIndexOutOfBoundsException
        } catch (IndexOutOfBoundsException e) {
            System.out.println("[Hierarchy] IndexOutOfBoundsException caught.");
        } catch (RuntimeException e) {
            System.out.println("[Hierarchy] General RuntimeException caught.");
        } catch (Exception e) {
            System.out.println("[Hierarchy] General Exception caught.");
        }
    }

    // Demonstrate throw vs throws
    public void throwVsThrowsDemo(String email) throws IllegalArgumentException {
        if (email == null || !email.contains("@")) {
            throw new IllegalArgumentException("Invalid email format.");
        }
        System.out.println("Valid email: " + email);
    }

    // Bulk registration from input list (handling per student)
    public void batchRegister(List<Student> students) {
        for (Student s : students) {
            try {
                register(s);
                System.out.println("Registered: " + s.name);
            } catch (InvalidAgeException | DataWriteException e) {
                System.out.println("❌ Error for " + s.name + ": " + e.getMessage());
            } catch (CollegeMismatchException e) {
                System.out.println("⚠️ Rejected " + s.name + ": " + e.getMessage());
            } finally {
                System.out.println("----");
            }
        }
    }
}
