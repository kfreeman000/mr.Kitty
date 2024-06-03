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
    displayMessage("You: " + userInput);

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                // Parse JSON response
                var response = JSON.parse(xhr.responseText);
                var botResponse = `Bot: ${response.bot_response}`;
                displayMessage(botResponse);
            } else {
                console.error("Error:", xhr.statusText);
            }
        }
    };
    xhr.send(JSON.stringify({ user_input: userInput }));

    document.getElementById("userInput").value = "";


        }
function displayMessage(message) {
            var chatbotContainer = document.querySelector(".chatbot");
            var messageElement = document.createElement("div");
            messageElement.classList.add("message");
            messageElement.textContent = message;
            chatbotContainer.appendChild(messageElement);
            chatbotContainer.scrollTop = chatbotContainer.scrollHeight;
        }