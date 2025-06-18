package Exceptions;

import java.util.*;

public class MainApp {
    public static void main(String[] args) {
        StudentManager manager = new StudentManager();

        // Students to test all cases
        List<StudentManager.Student> students = List.of(
            new StudentManager.Student("Shashwat", 21, "VESIT"),       // Valid
            new StudentManager.Student("Kunal", 17, "VESIT"),         // Invalid age
            new StudentManager.Student("Rahul", 25, "IITB"),           // Invalid college
            new StudentManager.Student("Harkirat", 32, "VESIT")           // Invalid age
        );

        // Batch register students
        manager.batchRegister(students);

        // Show exception hierarchy in action
        System.out.println("\n[Hierarchy Demonstration]");
        manager.hierarchyDemo();

        // throw vs throws demo
        System.out.println("\n[Throw vs Throws Demonstration]");
        try {
            manager.throwVsThrowsDemo("shashwat@vesit.edu");
            manager.throwVsThrowsDemo("invalid-email");
        } catch (IllegalArgumentException e) {
            System.out.println("Caught exception: " + e.getMessage());
        }
    }
}
