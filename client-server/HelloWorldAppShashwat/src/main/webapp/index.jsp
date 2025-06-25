<%@ page contentType="text/html; charset=UTF-8" %>
<html>
<head><title>Hello World</title></head>
<body>
    <h2>Welcome to HelloWorldWebApp</h2>
    <p>This is a simple Hello World Dynamic Web Project created by Shashwat.</p>
    <p>This project familiarizes with the project structure.</p>
    
    <a href="<%= request.getContextPath() %>/hello">Go to Hello Servlet</a>
</body>
</html>
