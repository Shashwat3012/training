<%@ page session="true" %>
<%
String user = (String) session.getAttribute("username");
if (user == null) {
    response.sendRedirect("login.jsp");
}
%>
<html>
<head><title>Welcome</title></head>
<body>
<h2>Welcome, <%= user %>!</h2>
<form action="logout" method="post">
    <input type="submit" value="Logout">
</form>
</body>
</html>
