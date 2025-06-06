// Student class with simplified structure
package basics;


class Student {
    private String name;
    private int age;
    private double marks;

    private static String university = "Delhi University";
    private static int totalStudents = 0;

    // Default constructor
    public Student() {
        this.name = "Unknown";
        this.age = 0;
        this.marks = 0.0;
        totalStudents++;
    }

    // Parameterized constructor
    public Student(String name, int age) {
        this.name = name;
        this.age = age;
        this.marks = 0.0;
        totalStudents++;
    }

    // Method to display basic info
    public void displayInfo() {
        System.out.println(name + " (" + age + " yrs) - Marks: " + marks + "% - " + university);
    }

    // Method to take exam
    public void takeExam(double obtainedMarks) {
        this.marks = obtainedMarks;
        System.out.println(name + " scored " + marks + "%");
    }

    // Method overloading example
    public void displaySummary() {
        System.out.println(name + " - " + marks + "%");
    }

    public void displaySummary(boolean detailed) {
        if (detailed) {
            displayInfo();
        } else {
            displaySummary();
        }
    }

    // Getter and Setter
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public static int getTotalStudents() {
        return totalStudents;
    }

    public boolean isSameAge(Student other) {
        return this.age == other.age;
    }
}

// Main class
public class ClassesObjects {
    public static void main(String[] args) {
        Student s1 = new Student("Shashwat", 21);
        Student s2 = new Student("Amit", 21);
        Student s3 = new Student();

        s1.takeExam(85);
        s2.takeExam(78);

        s1.displaySummary();
        s2.displaySummary(true);

        if (s1.isSameAge(s2)) {
            System.out.println(s1.getAge() + " is the same age as " + s2.getAge());
        }

        System.out.println("Total students: " + Student.getTotalStudents());
    }
}
