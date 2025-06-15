package OOP.Overriding;


// Parent class
class Person {
    String name;
    int age;
    
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    // Method to be overridden
    public void introduce() {
        System.out.println("Hi, I am " + name + " and I am " + age + " years old");
    }
    
    public void displayInfo() {
        System.out.println("Name: " + name + ", Age: " + age);
    }
}

// Child class overriding parent methods
class CollegeStudent extends Person {
    String college;
    String course;
    
    public CollegeStudent(String name, int age, String college, String course) {
        super(name, age);
        this.college = college;
        this.course = course;
    }
    
    // Overriding the introduce method
    @Override
    public void introduce() {
        System.out.println("Hello! I am " + name + ", " + age + " years old");
        System.out.println("I study " + course + " at " + college);
    }
    
    // Overriding the displayInfo method
    @Override
    public void displayInfo() {
        super.displayInfo(); // Call parent method
        System.out.println("College: " + college + ", Course: " + course);
    }
}

// Another child class with different overriding
class WorkingProfessional extends Person {
    String company;
    String position;
    
    public WorkingProfessional(String name, int age, String company, String position) {
        super(name, age);
        this.company = company;
        this.position = position;
    }
    
    // Different implementation of introduce method
    @Override
    public void introduce() {
        System.out.println("Greetings! I'm " + name + ", age " + age);
        System.out.println("I work as " + position + " at " + company);
    }
    
    @Override
    public void displayInfo() {
        super.displayInfo();
        System.out.println("Company: " + company + ", Position: " + position);
    }
}

// Example with same variable names (super keyword usage)
class Student {
    int marks = 80;
    
    public void display() {
        System.out.println("Student class display method");
    }
}

class VESITStudent extends Student {
    int marks = 95; // Same variable name as parent
    
    @Override
    public void display() {
        System.out.println("VESIT Student class display method");
    }
    
    public void showMarks() {
        System.out.println("Child class marks: " + marks);
        System.out.println("Parent class marks: " + super.marks);
    }
    
    public void showBothDisplays() {
        display(); // Child class method
        super.display(); // Parent class method
    }
}

public class Overriding {
    public static void main(String[] args) {
        // Method Overriding Example         
        // Creating objects
        Person person = new Person("Shashwat Tripathi", 21);
        CollegeStudent student = new CollegeStudent("Shashwat Tripathi", 21, "VESIT", "Computer Engineering");
        WorkingProfessional professional = new WorkingProfessional("Shashwat Tripathi", 21, "ISS Stoxx", "Junior Analyst");
        
        System.out.println("Person introduction:");
        person.introduce();
        
        System.out.println("\nStudent introduction:");
        student.introduce();
        
        System.out.println("\nProfessional introduction:");
        professional.introduce();
        
        
        // Method Overriding - Display Info 
        System.out.println("Person info:");
        person.displayInfo();
        
        System.out.println("\nStudent info:");
        student.displayInfo();
        
        System.out.println("\nProfessional info:");
        professional.displayInfo();
        
        
        // Super Keyword Example
        VESITStudent vesitStudent = new VESITStudent();
        vesitStudent.showMarks();
        vesitStudent.showBothDisplays();
    }
}