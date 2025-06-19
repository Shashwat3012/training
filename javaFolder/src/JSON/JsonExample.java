package JSON;



import org.json.JSONArray;
import org.json.JSONObject;

public class JsonExample {

    public static void main(String[] args) {
        // Basic JSON Object
        JSONObject student = new JSONObject();
        student.put("name", "Shashwat");
        student.put("age", 21);
        student.put("college", "VESIT");

        System.out.println("Student JSON:\n" + student.toString(2));

        // JSON Array of names
        JSONArray names = new JSONArray();
        names.put("Shashwat");
        names.put("Harkirat");
        names.put("Piyush");
        names.put("Kunal");

        System.out.println("\nNames JSON Array:\n" + names.toString(2));

        // Nested JSON Object (Address inside student)
        JSONObject address = new JSONObject();
        address.put("city", "Mumbai");
        address.put("pin", "400074");
        student.put("address", address);

        System.out.println("\nStudent with Address:\n" + student.toString(2));

        // JSON Array of Students
        JSONArray students = new JSONArray();

        JSONObject s1 = new JSONObject();
        s1.put("id", 1);
        s1.put("name", "Shashwat");

        JSONObject s2 = new JSONObject();
        s2.put("id", 2);
        s2.put("name", "Harkirat");

        students.put(s1);
        students.put(s2);

        System.out.println("\nStudents Array:\n" + students.toString(2));

        // Parse JSON String
        String jsonStr = "{\"id\": 10, \"name\": \"Piyush\", \"college\": \"VESIT\"}";
        JSONObject parsed = new JSONObject(jsonStr);
        System.out.println("\nParsed JSON from String:\n" + parsed.toString(2));

        // Custom Object to JSON
        Student kunal = new Student(4, "Kunal", 21, "VESIT");
        JSONObject kunalJson = new JSONObject();
        kunalJson.put("id", kunal.getId());
        kunalJson.put("name", kunal.getName());
        kunalJson.put("age", kunal.getAge());
        kunalJson.put("college", kunal.getCollege());

        System.out.println("\nKunal as JSON:\n" + kunalJson.toString(2));
    }

    // POJO for Student (must have getters to use with JSONObject)
    static class Student {
        private int id;
        private String name;
        private int age;
        private String college;

        public Student(int id, String name, int age, String college) {
            this.id = id;
            this.name = name;
            this.age = age;
            this.college = college;
        }

        public int getId() { return id; }
        public String getName() { return name; }
        public int getAge() { return age; }
        public String getCollege() { return college; }
    }
}
