package Collections;

import java.util.*;

public class CollectionsCustom {
    public static void main(String[] args) {

        List<Integer> marks = new ArrayList<>(Arrays.asList(88, 45, 99, 45));
        System.out.println("Original Marks: " + marks);
        Collections.sort(marks);
        System.out.println("Sorted Marks: " + marks);

        List<Student> students = new ArrayList<>();
        students.add(new Student(101, "Shashwat"));
        students.add(new Student(103, "Harkirat"));
        students.add(new Student(102, "Piyush"));
        students.add(new Student(104, "Kunal"));

        System.out.println("\nOriginal Students:");
        students.forEach(s -> System.out.println(s));

        Collections.sort(students); // Comparable
        System.out.println("\nSorted by Name (Comparable):");
        students.forEach(s -> System.out.println(s));

        students.sort(new StudentComparatorById()); // Comparator
        System.out.println("\nSorted by ID (Comparator):");
        students.forEach(s -> System.out.println(s));

        Set<Integer> rollSet = new HashSet<>(Arrays.asList(11, 21, 11, 5));
        System.out.println("\nUnique Roll Nos (Set): " + rollSet);

        Set<Student> studentSet = new HashSet<>(students);
        System.out.println("Student Set (no duplicates):");
        studentSet.forEach(s -> System.out.println(s));

        Map<Integer, String> studentMap = new HashMap<>();
        studentMap.put(1, "Shashwat");
        studentMap.put(2, "Piyush");
        studentMap.put(3, "Kunal");
        studentMap.put(4, "Harkirat");

        System.out.println("\nMap of Roll to Name:");
        studentMap.forEach((k, v) -> System.out.println(k + " => " + v));

        Map<Integer, Student> studentObjectMap = new TreeMap<>();
        for (Student s : students) studentObjectMap.put(s.getId(), s);

        System.out.println("\nMap of ID to Student Object:");
        studentObjectMap.forEach((id, s) -> System.out.println(id + ": " + s));

        List<Student> sortByNameComparator = new ArrayList<>(studentSet);
        sortByNameComparator.sort(new StudentComparatorByName());
        System.out.println("\nStudent List Sorted by Name (Comparator):");
        sortByNameComparator.forEach(s -> System.out.println(s));
    }
}
