const baseURL = "http://localhost:8000";
let currentScore = 0;
let currentQuestion = null;

async function loadQuestion() {
    try {
        const response = await fetch(`${baseURL}/quiz/question`);
        if (!response.ok) throw new Error('Failed to load question');
        currentQuestion = await response.json();
        
        document.getElementById('question').textContent = currentQuestion.text;
        const optionsContainer = document.getElementById('options');
        optionsContainer.innerHTML = '';
        
        currentQuestion.options.forEach(option => {
            const button = document.createElement('button');
            button.textContent = option;
            button.onclick = () => submitAnswer(option);
            optionsContainer.appendChild(button);
        });
    } catch (error) {
        console.error('Error loading question:', error);
        document.getElementById('error').textContent = 'Failed to load question. Please try again.';
    }
}

async function submitAnswer(answer) {
    try {
        const response = await fetch(`${baseURL}/quiz/answer`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                id: currentQuestion.id,
                answer: answer,
                score: currentScore
            })
        });
        
        if (!response.ok) throw new Error('Failed to submit answer');
        const result = await response.json();
        
        const feedback = document.getElementById('feedback');
        feedback.textContent = result.is_correct ? 'Correct!' : `Wrong! The correct answer was ${result.correct_answer}`;
        feedback.className = result.is_correct ? 'correct' : 'wrong';
        
        currentScore = result.score;
        document.getElementById('score').textContent = `Current Score: ${currentScore}`;
        document.getElementById('highScore').textContent = `High Score: ${result.high_score}`;
        
        // Load next question after a short delay
        setTimeout(loadQuestion, 1500);
    } catch (error) {
        console.error('Error submitting answer:', error);
        document.getElementById('error').textContent = 'Failed to submit answer. Please try again.';
    }
}

// Initialize the quiz
document.addEventListener('DOMContentLoaded', async () => {
    try {
        const response = await fetch(`${baseURL}/quiz/highscore`);
        if (!response.ok) throw new Error('Failed to load high score');
        const data = await response.json();
        document.getElementById('highScore').textContent = `High Score: ${data.high_score}`;
        loadQuestion();
    } catch (error) {
        console.error('Error initializing quiz:', error);
        document.getElementById('error').textContent = 'Failed to initialize quiz. Please reload the page.';
    }
});
