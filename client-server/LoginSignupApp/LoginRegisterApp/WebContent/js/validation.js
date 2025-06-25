function validateLoginForm() {
    let username = document.forms["loginForm"]["username"].value;
    let password = document.forms["loginForm"]["password"].value;
    if (username == "" || password == "") {
        alert("All fields are required");
        return false;
    }
    return true;
}

function validateRegisterForm() {
    let username = document.forms["registerForm"]["username"].value;
    let password = document.forms["registerForm"]["password"].value;
    let confirm = document.forms["registerForm"]["confirm"].value;
    if (username == "" || password == "" || confirm == "") {
        alert("All fields are required");
        return false;
    }
    if (password !== confirm) {
        alert("Passwords do not match");
        return false;
    }
    return true;
}
