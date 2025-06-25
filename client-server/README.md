# Java Web Application Training: Client-Server Integration

This repository covers the complete flow of integrating client-side and server-side logic using Servlets, JSP, and JavaScript, while hosting the application on Tomcat.

---

## 📘 Topics Covered

### 1. 🌐 Servlets, JSP, and Servlet Mapping
- Learn to build Java-based dynamic web applications using:
  - **Servlets**
  - **JavaServer Pages (JSP)**
  - Mapping using `web.xml` or annotations
- 📖 Reference: [Oracle Java EE Tutorial - Servlets and JSP](https://docs.oracle.com/javaee/6/tutorial/doc/gilik.html)

---

### 2. 📡 HTTP Methods & Status Codes
- Understand various HTTP methods (`GET`, `POST`, etc.)
- Learn standard HTTP response status codes (`200 OK`, `404 Not Found`, `500 Internal Server Error`, etc.)
- 📖 Reference: [REST API Tutorial - HTTP Status Codes](http://www.restapitutorial.com/httpstatuscodes.html)

---

### 3. 🖥️ Hello World Web Application
- Create a basic **dynamic web project in Eclipse**
- Use **Apache Tomcat** to host the application
- Understand the typical structure:
  - `WEB-INF`, `web.xml`, `src`, and `WebContent` folders
- Output: A basic **"Hello World"** page served via a Servlet

---

### 4. 🔐 User Login and Registration Flow
- Build a simple web application with:
  - **Login form**
  - **Registration form**
- Features:
  - Successful login welcomes the user
  - New users must register
  - Logout button returns user to login page
  - Incorrect credentials show error message and reload login form
- Stack: **JSP + Servlet + Tomcat**
- Images:

1. Register Page:
![alt text](<Screenshot 2025-06-25 171945.png>)

2. Login Page
![alt text](<Screenshot 2025-06-25 172038.png>)

3. Home Page
![alt text](<Screenshot 2025-06-25 172049.png>)

4. After Logout, you are redirected to Login page
![alt text](<Screenshot 2025-06-25 171903-1.png>)
---

### 5. ✅ Client-side Validation with JavaScript
- Implement front-end validations (e.g., empty field check, email format, password match) using JavaScript
- Ensures form data is validated before reaching the server

---

## 🛠️ Development Notes

- Use **Eclipse IDE** with **Dynamic Web Project**
- Ensure **Apache Tomcat Server** is added and properly configured
- Steps for changes:
  - After modifying Java/Servlet code: **Clean & Build Project**, then **Restart Tomcat**
  - After modifying JSP/HTML/JS: Just **Save and Refresh**, no server restart needed
- Enable **Auto Build** in Eclipse to simplify development flow

---

## 🚀 Pre-requisites

Make sure you have the following installed:
- JDK 8 or higher
- Eclipse IDE for Enterprise Java Developers
- Apache Tomcat (v9 recommended)

---

