const.0.0.1:5000/chatbot";

function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() === "") return;

    // Display user message
    addMessageToChatBox("User", userInput);

    fetch(endpoint, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ prompt: userInput })
    })
    .then(response => response.text())  // Changed to response.text() for debugging
    .then(data => {
        // Display chatbot response
        addMessageToChatBox("Chatbot", data);
    })
    .catch(error => {
        console.error('Error:', error);
        addMessageToChatBox("Error", "There was an error processing your request.");
    });

    document.getElementById('user-input').value = "";
}

function addMessageToChatBox(sender, message) {
    const chatBox = document.getElementById('chat-box');
    const messageElement = document.createElement('div');
    messageElement.textContent = `${sender}: ${message}`;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function sendMessage() {
    console.log("sendMessage called");  // Debugging statement
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() === "") return;

    console.log("User input:", userInput);  // Debugging statement

    // Display user message
    addMessageToChatBox("User", userInput);

    fetch(endpoint, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ prompt: userInput })
    })
    .then(response => response.text())  // Changed to response.text() for debugging
    .then(data => {
        console.log("Response data:", data);  // Debugging statement
        // Display chatbot response
        addMessageToChatBox("Chatbot", data);
    })
    .catch(error => {
        console.error('Error:', error);
        addMessageToChatBox("Error", "There was an error processing your request.");
    });

    document.getElementById('user-input').value = "";
}