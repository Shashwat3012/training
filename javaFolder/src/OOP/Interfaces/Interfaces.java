package OOP.Interfaces;


// Interfaces Example 

// Basic interface for student operations
interface StudentOperations {
    // All variables in interface are public, static, and final by default
    int MAX_SUBJECTS = 10;
    double MIN_PASSING_GRADE = 40.0;
    
    // All methods in interface are public and abstract by default
    void study();
    void attendLecture();
    double calculateGPA();
    boolean isEligibleForExam();
    
    // Default method (Java 8 feature)
    default void displayMotivation() {
        System.out.println("Keep learning and growing!");
    }
    
    // Static method (Java 8 feature)
    static void showStudentGuidelines() {
        System.out.println("=== Student Guidelines ===");
        System.out.println("1. Attend all lectures");
        System.out.println("2. Complete assignments on time");
        System.out.println("3. Maintain minimum " + MIN_PASSING_GRADE + "% attendance");
        System.out.println("4. Maximum " + MAX_SUBJECTS + " subjects per semester");
    }
}

// Interface for college activities
interface CollegeActivities {
    void participate();
    void organize();
    String getActivityType();
}

// Interface for academic performance
interface AcademicPerformance {
    double getPercentage();
    String getGrade();
    void updateMarks(double marks);
}

// Functional interface (has only one abstract method)
@FunctionalInterface
interface Calculator {
    double calculate(double a, double b);
    
    // Default methods are allowed
    default void printResult(double result) {
        System.out.println("Result: " + result);
    }
}

// Class implementing single interface
class RegularStudent implements StudentOperations {
    private String name;
    private int age;
    private String college;
    private double[] marks;
    private int subjectCount;
    
    public RegularStudent(String name, int age, String college) {
        this.name = name;
        this.age = age;
        this.college = college;
        this.marks = new double[MAX_SUBJECTS];
        this.subjectCount = 0;
    }
    
    // Implementing interface methods
    @Override
    public void study() {
        System.out.println(name + " is studying at " + college);
    }
    
    @Override
    public void attendLecture() {
        System.out.println(name + " is attending a lecture");
    }
    
    @Override
    public double calculateGPA() {
        if (subjectCount == 0) return 0.0;
        
        double total = 0;
        for (int i = 0; i < subjectCount; i++) {
            total += marks[i];
        }
        return total / subjectCount / 10; // Converting to 4.0 scale
    }
    
    @Override
    public boolean isEligibleForExam() {
        return calculateGPA() * 10 >= MIN_PASSING_GRADE;
    }
    
    // Additional methods
    public void addSubjectMarks(double mark) {
        if (subjectCount < MAX_SUBJECTS) {
            marks[subjectCount++] = mark;
        } else {
            System.out.println("Cannot add more subjects. Maximum limit reached.");
        }
    }
    
    public void displayInfo() {
        System.out.println("Name: " + name + ", Age: " + age + ", College: " + college);
        System.out.println("GPA: " + String.format("%.2f", calculateGPA()));
        System.out.println("Eligible for exam: " + isEligibleForExam());
    }
}

// Class implementing multiple interfaces
class StudentLeader implements StudentOperations, CollegeActivities, AcademicPerformance {
    private String name;
    private int age;
    private String college;
    private double totalMarks;
    private int subjects;
    private String currentActivity;
    
    public StudentLeader(String name, int age, String college) {
        this.name = name;
        this.age = age;
        this.college = college;
        this.totalMarks = 0;
        this.subjects = 0;
        this.currentActivity = "Academic Excellence";
    }
    
    // Implementing Student Operations interface
    @Override
    public void study() {
        System.out.println(name + " is studying leadership and academics");
    }
    
    @Override
    public void attendLecture() {
        System.out.println(name + " is attending lecture and taking notes for others");
    }
    
    @Override
    public double calculateGPA() {
        return subjects > 0 ? (totalMarks / subjects) / 10 : 0.0;
    }
    
    @Override
    public boolean isEligibleForExam() {
        return getPercentage() >= MIN_PASSING_GRADE;
    }
    
    // Implementing CollegeActivities interface
    @Override
    public void participate() {
        System.out.println(name + " is participating in " + currentActivity);
    }
    
    @Override
    public void organize() {
        System.out.println(name + " is organizing college events and activities");
    }
    
    @Override
    public String getActivityType() {
        return currentActivity;
    }
    
    // Implementing AcademicPerformance interface
    @Override
    public double getPercentage() {
        return subjects > 0 ? totalMarks / subjects : 0.0;
    }
    
    @Override
    public String getGrade() {
        double percentage = getPercentage();
        if (percentage >= 90) return "A+";
        else if (percentage >= 80) return "A";
        else if (percentage >= 70) return "B";
        else if (percentage >= 60) return "C";
        else if (percentage >= 50) return "D";
        else return "F";
    }
    
    @Override
    public void updateMarks(double marks) {
        totalMarks += marks;
        subjects++;
    }
    
    // Additional methods
    public void setCurrentActivity(String activity) {
        this.currentActivity = activity;
    }
    
    public void displayCompleteInfo() {
        System.out.println("=== Student Leader Information ===");
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("College: " + college);
        System.out.println("Percentage: " + String.format("%.2f", getPercentage()) + "%");
        System.out.println("Grade: " + getGrade());
        System.out.println("GPA: " + String.format("%.2f", calculateGPA()));
        System.out.println("Current Activity: " + getActivityType());
        System.out.println("Eligible for Exam: " + isEligibleForExam());
    }
}

// Abstract class implementing an interface
abstract class CollegeStudent implements StudentOperations {
    protected String name;
    protected String college;
    
    public CollegeStudent(String name, String college) {
        this.name = name;
        this.college = college;
    }
    
    // Implementing some interface methods
    @Override
    public void study() {
        System.out.println(name + " from " + college + " is studying");
    }
    
    @Override
    public void attendLecture() {
        System.out.println(name + " is attending lecture at " + college);
    }
    
    // Abstract method to be implemented by subclasses
    public abstract void selectMajor();
}

// Concrete class extending abstract class
class EngineeringStudent extends CollegeStudent {
    private String branch;
    private double[] semesterMarks;
    private int currentSemester;
    
    public EngineeringStudent(String name, String college, String branch) {
        super(name, college);
        this.branch = branch;
        this.semesterMarks = new double[8]; // 8 semesters
        this.currentSemester = 0;
    }
    
    @Override
    public void selectMajor() {
        System.out.println(name + " has selected " + branch + " engineering");
    }
    
    @Override
    public double calculateGPA() {
        if (currentSemester == 0) return 0.0;
        double total = 0;
        for (int i = 0; i < currentSemester; i++) {
            total += semesterMarks[i];
        }
        return (total / currentSemester) / 10;
    }
    
    @Override
    public boolean isEligibleForExam() {
        return calculateGPA() * 10 >= MIN_PASSING_GRADE;
    }
    
    public void completeSemester(double marks) {
        if (currentSemester < 8) {
            semesterMarks[currentSemester++] = marks;
        }
    }
    
    public void displayEngineeringInfo() {
        System.out.println("Engineering Student: " + name);
        System.out.println("College: " + college);
        System.out.println("Branch: " + branch);
        System.out.println("Current Semester: " + (currentSemester + 1));
        System.out.println("CGPA: " + String.format("%.2f", calculateGPA()));
    }
}

// Main class demonstrating interfaces
public class Interfaces {
    public static void main(String[] args) {
        // Show static method from interface
        StudentOperations.showStudentGuidelines();
        System.out.println();
        
        // Regular student example
        RegularStudent student1 = new RegularStudent("Shashwat", 21, "VESIT");
        
        student1.study();
        student1.attendLecture();
        student1.addSubjectMarks(85);
        student1.addSubjectMarks(92);
        student1.addSubjectMarks(78);
        student1.addSubjectMarks(88);
        student1.displayInfo();
        student1.displayMotivation(); // Default method from interface
        System.out.println();
        
        // Student leader example (multiple interfaces)
        StudentLeader leader = new StudentLeader("Priya", 22, "VESIT");
        
        leader.updateMarks(90);
        leader.updateMarks(85);
        leader.updateMarks(92);
        leader.setCurrentActivity("Technical Fest Organization");
        leader.study();
        leader.attendLecture();
        leader.participate();
        leader.organize();
        leader.displayCompleteInfo();
        System.out.println();
        
        // Engineering student example (abstract class implementing interface)
        EngineeringStudent engStudent = new EngineeringStudent("Shashwat", "VESIT", "Computer Science");
        
        engStudent.selectMajor();
        engStudent.study();
        engStudent.attendLecture();
        engStudent.completeSemester(85);
        engStudent.completeSemester(88);
        engStudent.completeSemester(92);
        engStudent.displayEngineeringInfo();
        System.out.println();
        
        // Functional interface example with lambda expressions
        // Using lambda expressions with functional interface
        Calculator add = (a, b) -> a + b;
        Calculator multiply = (a, b) -> a * b;
        Calculator divide = (a, b) -> b != 0 ? a / b : 0;
        
        double num1 = 15.5, num2 = 4.5;
        
        System.out.println("Numbers: " + num1 + " and " + num2);
        
        double sum = add.calculate(num1, num2);
        add.printResult(sum);
        
        double product = multiply.calculate(num1, num2);
        multiply.printResult(product);
        
        double quotient = divide.calculate(num1, num2);
        divide.printResult(quotient);
        
        System.out.println();
        
        // Interface reference example
        StudentOperations[] students = {
            new RegularStudent("Amit", 20, "VESIT"),
            new StudentLeader("Sneha", 21, "VESIT"),
            new EngineeringStudent("Rahul", "VESIT", "Mechanical")
        };
        
        for (StudentOperations student : students) {
            student.study();
            student.attendLecture();
            System.out.println("GPA: " + String.format("%.2f", student.calculateGPA()));
            student.displayMotivation();
            System.out.println();
        }
    }
}