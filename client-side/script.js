document
  .getElementById("registrationForm")
  .addEventListener("submit", function (e) {
    e.preventDefault();

    const name = document.getElementById("name").value.trim();
    const age = parseInt(document.getElementById("age").value);
    const email = document.getElementById("email").value.trim();
    const phone = document.getElementById("phone").value.trim();
    const gender = document.querySelector("input[name='gender']:checked");

    // Validate using regex
    const nameRegex = /^[a-zA-Z\s]{3,50}$/;
    const phoneRegex = /^[6-9]\d{9}$/;
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

    if (!nameRegex.test(name)) {
      alert("❌ Invalid name: Only alphabets (3–50 chars) allowed.");
      return;
    }

    if (isNaN(age) || age < 17 || age > 30) {
      alert("❌ Age must be between 17 and 30.");
      return;
    }

    if (!emailRegex.test(email)) {
      alert("❌ Invalid email format.");
      return;
    }

    if (!phoneRegex.test(phone)) {
      alert("❌ Invalid phone number. Must be 10 digits, start with 6–9.");
      return;
    }

    if (!gender) {
      alert("❌ Please select gender.");
      return;
    }

    // Success
    alert(`✅ Registration Successful!
  Name: ${name}
  Age: ${age}
  Email: ${email}
  Phone: ${phone}
  Gender: ${gender.value}
  College: VESIT`);
  });
