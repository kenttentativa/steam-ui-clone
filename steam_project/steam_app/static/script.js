document.addEventListener("DOMContentLoaded", function () {
    console.log("Steam UI Clone Loaded");

    // Example: Alert when clicking a game
    document.querySelectorAll(".game").forEach(game => {
        game.addEventListener("click", function () {
            alert("Game clicked: " + this.querySelector("p").textContent);
        });
    });
    
    document.getElementById("logoutBtn").addEventListener("click", function () {
        alert("You have been logged out!");
        // Redirect to login page or perform session cleanup
        window.location.href = "login.html"; // Change if needed
    });    

    // Example: Dark Mode Toggle (optional)
    const body = document.body;
    const toggleDarkMode = document.createElement("button");
    toggleDarkMode.textContent = "Toggle Dark Mode";
    toggleDarkMode.style.position = "fixed";
    toggleDarkMode.style.bottom = "20px";
    toggleDarkMode.style.right = "20px";
    toggleDarkMode.style.padding = "10px";
    toggleDarkMode.style.cursor = "pointer";

    document.body.appendChild(toggleDarkMode);

    toggleDarkMode.addEventListener("click", () => {
        body.classList.toggle("dark-mode");
        if (body.classList.contains("dark-mode")) {
            body.style.backgroundColor = "#0f172a";
        } else {
            body.style.backgroundColor = "#1b2838";
        }
    });
});
