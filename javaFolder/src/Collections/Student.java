package Collections;

public class Student implements Comparable<Student> {
    private int id;
    private String name;

    public Student(int id, String name) {
        this.id = id;
        this.name = name;
    }

    public int getId() { return id; }
    public String getName() { return name; }

    @Override
    public int compareTo(Student o) {
        return this.name.compareTo(o.name); // default sort by name
    }

    @Override
    public String toString() {
        return id + " - " + name;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Student)) return false;
        Student other = (Student) obj;
        return id == other.id && name.equals(other.name);
    }

    @Override
    public int hashCode() {
        return id * 31 + name.hashCode();
    }
}
