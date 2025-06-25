<%@ page session="false" %>
<html>
<head><title>Login</title>
<script src="js/validation.js"></script>
</head>
<body>
<h2>Login</h2>
<form name="loginForm" action="login" method="post" onsubmit="return validateLoginForm()">
    Username: <input type="text" name="username"><br/>
    Password: <input type="password" name="password"><br/>
    <input type="submit" value="Login">
</form>
<p><a href="register.jsp">Register Here</a></p>
<% String error = request.getParameter("error"); if (error != null) { %>
<p style="color:red;"><%= error %></p>
<% } %>
</body>
</html>
