const baseURL = "http://localhost:8000";

async function loadWelcomeMessage() {
    try {
        const response = await fetch(`${baseURL}/home`);
        const data = await response.json();
        const welcomeMessage = document.createElement('p');
        welcomeMessage.textContent = data.message;
        document.querySelector('.container').appendChild(welcomeMessage);
    } catch (error) {
        console.error('Error loading welcome message:', error);
    }
}

loadWelcomeMessage();