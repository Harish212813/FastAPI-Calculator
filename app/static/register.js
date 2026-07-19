const registerForm = document.getElementById("register-form");
const message = document.getElementById("message");

registerForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const username = document.getElementById("username").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById(
        "confirm-password"
    ).value;

    message.textContent = "";

    if (username.length < 3) {
        message.textContent =
            "Username must be at least 3 characters long.";
        return;
    }

    if (password.length < 8) {
        message.textContent =
            "Password must be at least 8 characters long.";
        return;
    }

    if (password !== confirmPassword) {
        message.textContent = "Passwords do not match.";
        return;
    }

    try {
        const response = await fetch("/register", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                username,
                email,
                password,
            }),
        });

        const data = await response.json();

        if (!response.ok) {
            message.textContent =
                data.detail || "Registration failed.";
            return;
        }

        localStorage.setItem(
            "access_token",
            data.access_token
        );

        message.textContent = data.message;
        registerForm.reset();
    } catch (error) {
        message.textContent =
            "Unable to connect to the server.";
    }
});