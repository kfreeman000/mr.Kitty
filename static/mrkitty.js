var slideIndex = 0;
showSlides();

function showSlides() {
    var i;
    var slides = document.getElementsByClassName("mySlides");

    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }

    slideIndex++;

    if (slideIndex > slides.length) {
        slideIndex = 1;
    }

    slides[slideIndex - 1].style.display = "block";

    setTimeout(showSlides, 3000); 
}

function sendMessage() {
    var userInput = document.getElementById("userInput").value;
    displayMessage("You: " + userInput, "user-message");


    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                var botResponse = `SmartKitty: ${response.bot_response}`;
                displayMessage(botResponse, "bot-message"); // Add a class for bot messages
            } else {
                console.error("Error:", xhr.statusText);
            }
        }
    };
    xhr.send(JSON.stringify({ user_input: userInput }));

    document.getElementById("userInput").value = "";
    console.log("Sending:", userInput);

}

function displayMessage(message, messageClass) {
    var chatMessages = document.getElementById("chat-messages"); // Select the correct container
    var messageElement = document.createElement("div");
    messageElement.classList.add("message", messageClass); // Add message and user/bot class
    messageElement.textContent = message;
    chatMessages.appendChild(messageElement);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}