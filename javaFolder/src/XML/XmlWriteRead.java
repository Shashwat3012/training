package XML;

import javax.xml.parsers.*;
import javax.xml.transform.*;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;

import org.w3c.dom.*;

import java.io.File;

public class XmlWriteRead {

    static String filePath = "./src/XML/students.xml";

    public static void main(String[] args) {
        try {
            writeXML();
            readXML();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    static void writeXML() throws Exception {
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        DocumentBuilder builder = factory.newDocumentBuilder();

        // Root element
        Document doc = builder.newDocument();
        Element root = doc.createElement("students");
        doc.appendChild(root);

        // Add Shashwat
        root.appendChild(createStudent(doc, "1", "Shashwat", "21", "VESIT"));
        root.appendChild(createStudent(doc, "2", "Harkirat", "22", "VESIT"));
        root.appendChild(createStudent(doc, "3", "Piyush", "21", "VESIT"));
        root.appendChild(createStudent(doc, "4", "Kunal", "23", "VESIT"));

        // Write to XML file
        Transformer t = TransformerFactory.newInstance().newTransformer();
        t.setOutputProperty(OutputKeys.INDENT, "yes");
        t.transform(new DOMSource(doc), new StreamResult(new File(filePath)));

        System.out.println("XML written to " + filePath);
    }

    static Element createStudent(Document doc, String id, String name, String age, String college) {
        Element student = doc.createElement("student");

        Element idEl = doc.createElement("id");
        idEl.appendChild(doc.createTextNode(id));
        student.appendChild(idEl);

        Element nameEl = doc.createElement("name");
        nameEl.appendChild(doc.createTextNode(name));
        student.appendChild(nameEl);

        Element ageEl = doc.createElement("age");
        ageEl.appendChild(doc.createTextNode(age));
        student.appendChild(ageEl);

        Element collegeEl = doc.createElement("college");
        collegeEl.appendChild(doc.createTextNode(college));
        student.appendChild(collegeEl);

        return student;
    }

    static void readXML() throws Exception {
        File file = new File(filePath);
        if (!file.exists()) {
            System.out.println("No XML file found to read.");
            return;
        }

        DocumentBuilder builder = DocumentBuilderFactory.newInstance().newDocumentBuilder();
        Document doc = builder.parse(file);

        NodeList list = doc.getElementsByTagName("student");
        System.out.println("\n--- Reading XML ---");

        for (int i = 0; i < list.getLength(); i++) {
            Node s = list.item(i);
            if (s.getNodeType() == Node.ELEMENT_NODE) {
                Element student = (Element) s;
                String id = student.getElementsByTagName("id").item(0).getTextContent();
                String name = student.getElementsByTagName("name").item(0).getTextContent();
                String age = student.getElementsByTagName("age").item(0).getTextContent();
                String college = student.getElementsByTagName("college").item(0).getTextContent();

                System.out.println("ID: " + id + ", Name: " + name + ", Age: " + age + ", College: " + college);
            }
        }
    }
}
