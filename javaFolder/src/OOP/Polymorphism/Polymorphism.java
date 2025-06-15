package OOP.Polymorphism;

// Java Polymorphism : Runtime Polymorphism and Compile-time Polymorphism

// Base class for Runtime Polymorphism
class Shape {
    String name;
    
    public Shape(String name) {
        this.name = name;
    }
    
    // Method to be overridden
    public void draw() {
        System.out.println("Drawing a shape: " + name);
    }
    
    public double calculateArea() {
        return 0;
    }
}

class Circle extends Shape {
    double radius;
    
    public Circle(double radius) {
        super("Circle");
        this.radius = radius;
    }
    
    @Override
    public void draw() {
        System.out.println("Drawing a circle with radius: " + radius);
    }
    
    @Override
    public double calculateArea() {
        return Math.PI * radius * radius;
    }
}

class Rectangle extends Shape {
    double length, width;
    
    public Rectangle(double length, double width) {
        super("Rectangle");
        this.length = length;
        this.width = width;
    }
    
    @Override
    public void draw() {
        System.out.println("Drawing a rectangle " + length + " x " + width);
    }
    
    @Override
    public double calculateArea() {
        return length * width;
    }
}

class Triangle extends Shape {
    double base, height;
    
    public Triangle(double base, double height) {
        super("Triangle");
        this.base = base;
        this.height = height;
    }
    
    @Override
    public void draw() {
        System.out.println("Drawing a triangle with base: " + base + " and height: " + height);
    }
    
    @Override
    public double calculateArea() {
        return 0.5 * base * height;
    }
}

// Example class for Method Overloading (Compile-time Polymorphism)
class Calculator {
    String owner;
    
    public Calculator(String owner) {
        this.owner = owner;
    }
    
    // Method overloading - same method name, different parameters
    public int add(int a, int b) {
        System.out.println(owner + "'s calculator: Adding two integers");
        return a + b;
    }
    
    public double add(double a, double b) {
        System.out.println(owner + "'s calculator: Adding two doubles");
        return a + b;
    }
    
    public int add(int a, int b, int c) {
        System.out.println(owner + "'s calculator: Adding three integers");
        return a + b + c;
    }
    
    public String add(String a, String b) {
        System.out.println(owner + "'s calculator: Concatenating strings");
        return a + b;
    }
    
    // Method overloading with different parameter order
    public void displayInfo(String name, int age) {
        System.out.println("Name: " + name + ", Age: " + age);
    }
    
    public void displayInfo(int age, String name) {
        System.out.println("Age: " + age + ", Name: " + name);
    }
}

// Example for Student Polymorphism
class StudentBase {
    String name;
    int age;
    
    public StudentBase(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    public void attendClass() {
        System.out.println(name + " is attending class");
    }
    
    public void study() {
        System.out.println(name + " is studying");
    }
}

class EngineeringStudentPoly extends StudentBase {
    String college;
    
    public EngineeringStudentPoly(String name, int age, String college) {
        super(name, age);
        this.college = college;
    }
    
    @Override
    public void attendClass() {
        System.out.println(name + " from " + college + " is attending engineering class");
    }
    
    @Override
    public void study() {
        System.out.println(name + " is studying engineering subjects at " + college);
    }
}

class MedicalStudentPoly extends StudentBase {
    String college;
    
    public MedicalStudentPoly(String name, int age, String college) {
        super(name, age);
        this.college = college;
    }
    
    @Override
    public void attendClass() {
        System.out.println(name + " from " + college + " is attending medical class");
    }
    
    @Override
    public void study() {
        System.out.println(name + " is studying medical subjects at " + college);
    }
}

public class Polymorphism {
    public static void main(String[] args) {
        // Runtime Polymorphism - Method Overriding
        
        // Array of Shape references
        Shape[] shapes = {
            new Circle(5.0),
            new Rectangle(4.0, 6.0),
            new Triangle(3.0, 8.0)
        };
        
        // Runtime polymorphism - method called depends on actual object type
        for (Shape shape : shapes) {
            shape.draw();
            System.out.println("Area: " + shape.calculateArea());
            System.out.println();
        }
        
        // Compile-time Polymorphism  - Method Overloading
        Calculator calc = new Calculator("Shashwat Tripathi");
        
        System.out.println("Result: " + calc.add(10, 20));
        System.out.println("Result: " + calc.add(10.5, 20.5));
        System.out.println("Result: " + calc.add(10, 20, 30));
        System.out.println("Result: " + calc.add("Shashwat ", "Tripathi"));
        
        // Method overloading with different parameter order 
        calc.displayInfo("Shashwat Tripathi", 21);
        calc.displayInfo(21, "Shashwat Tripathi");
        
        //  Polymorphism Example 
        StudentBase[] students = {
            new EngineeringStudentPoly("Shashwat Tripathi", 21, "VESIT"),
            new MedicalStudentPoly("Shashwat Tripathi", 21, "VESIT")
        };
        
        for (StudentBase student : students) {
            student.attendClass();
            student.study();
            System.out.println();
        }
        
        // Dynamic Method Dispatch 
        StudentBase student1 = new EngineeringStudentPoly("Shashwat Tripathi", 21, "VESIT");
        StudentBase student2 = new MedicalStudentPoly("Shashwat Tripathi", 21, "VESIT");
        
        student1.attendClass(); // Calls EngineeringStudentPoly's method
        student2.attendClass(); // Calls MedicalStudentPoly's method
    }
}