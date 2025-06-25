<%@ page session="false" %>
<html>
<head><title>Register</title>
<script src="js/validation.js"></script>
</head>
<body>
<h2>Register</h2>
<form name="registerForm" action="register" method="post" onsubmit="return validateRegisterForm()">
    Username: <input type="text" name="username"><br/>
    Password: <input type="password" name="password"><br/>
    Confirm Password: <input type="password" name="confirm"><br/>
    <input type="submit" value="Register">
</form>
</body>
</html>
