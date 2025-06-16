package MyPackages.college.student;

// Class with public and protected members
public class Student {
    public String name;
    protected int age;
    private String college;

    public Student(String name, int age, String college) {
        this.name = name;
        this.age = age;
        this.college = college;
    }

    public void displayPublicDetails() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }

    protected void displayProtectedDetails() {
        System.out.println("College: " + college);
    }
}
