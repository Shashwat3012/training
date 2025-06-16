package MyPackages.app;

import MyPackages.college.student.Student;
import MyPackages.college.utils.StudentUtils;

public class MainApp {
    public static void main(String[] args) {
        Student s1 = new Student("Shashwat", 21, "VESIT");

        // Accessing public method and field
        s1.displayPublicDetails();

        // Protected method and private fields are not accessible here
        // s1.displayProtectedDetails(); // ❌ error

        // Use utility class
        StudentUtils utils = new StudentUtils();
        utils.printFullInfo(s1);
    }
}
