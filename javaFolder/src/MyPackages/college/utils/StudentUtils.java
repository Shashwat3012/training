package MyPackages.college.utils;

import MyPackages.college.student.Student;

public class StudentUtils {
    public void printFullInfo(Student s) {
        s.displayPublicDetails();  // Can access public methods
        // s.displayProtectedDetails(); // ❌ Will give error: protected methods can't be accessed here

        // Direct access to fields
        System.out.println("Name from utils: " + s.name);
        // System.out.println("Age from utils: " + s.age); // ❌ protected - not in subclass
        // System.out.println("College from utils: " + s.college); // ❌ private - inaccessible
    }
}
