// Screening Questionnaire JavaScript
// Handles multi-step form, conditional logic, and submission

let questions = [];
let currentQuestionIndex = 0;
let responses = {};

// Initialize when page loads
document.addEventListener('DOMContentLoaded', async function() {
    await loadQuestions();
    renderQuestion();
    updateProgress();
    setupNavigation();
});

// Load questions from API
async function loadQuestions() {
    try {
        const response = await fetch('/api/questions');
        questions = await response.json();
        document.getElementById('totalQuestions').textContent = questions.length;
    } catch (error) {
        console.error('Error loading questions:', error);
        alert('Failed to load questions. Please refresh the page.');
    }
}

// Render current question
function renderQuestion() {
    const question = questions[currentQuestionIndex];
    if (!question) return;

    // Check if question should be shown (conditional logic)
    if (question.conditional && question.display_condition) {
        const dependsOn = question.display_condition.depends_on;
        const showIfValue = question.display_condition.show_if_value;

        if (responses[dependsOn] !== showIfValue) {
            // Skip this question
            responses[question.question_id] = null;
            if (currentQuestionIndex < questions.length - 1) {
                currentQuestionIndex++;
                renderQuestion();
                return;
            }
        }
    }

    const container = document.getElementById('questionsContainer');

    // Build options HTML
    let optionsHtml = '';
    question.response_options.forEach((option, index) => {
        const value = option.value !== null ? option.value : 'NA';
        const checked = responses[question.question_id] === String(value) ? 'checked' : '';

        optionsHtml += `
            <label class="option-label">
                <input type="radio"
                       name="${question.question_id}"
                       value="${value}"
                       ${checked}
                       onchange="saveResponse('${question.question_id}', this.value)">
                <span>${option.label}</span>
            </label>
        `;
    });

    container.innerHTML = `
        <div class="question-card active">
            <div class="question-section">${question.section_name}</div>
            <div class="question-text">${question.question_text}</div>
            <div class="question-options">
                ${optionsHtml}
            </div>
        </div>
    `;
}

// Save response
function saveResponse(questionId, value) {
    responses[questionId] = value;
    console.log('Response saved:', questionId, value);
}

// Update progress bar
function updateProgress() {
    const progress = ((currentQuestionIndex + 1) / questions.length) * 100;
    document.getElementById('progressBar').style.width = progress + '%';
    document.getElementById('currentQuestion').textContent = currentQuestionIndex + 1;

    // Update button visibility
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const submitBtn = document.getElementById('submitBtn');

    prevBtn.disabled = currentQuestionIndex === 0;

    if (currentQuestionIndex === questions.length - 1) {
        nextBtn.style.display = 'none';
        submitBtn.style.display = 'inline-flex';
    } else {
        nextBtn.style.display = 'inline-flex';
        submitBtn.style.display = 'none';
    }
}

// Setup navigation
function setupNavigation() {
    document.getElementById('prevBtn').addEventListener('click', goToPrevious);
    document.getElementById('nextBtn').addEventListener('click', goToNext);
    document.getElementById('screeningForm').addEventListener('submit', handleSubmit);
}

// Go to previous question
function goToPrevious() {
    if (currentQuestionIndex > 0) {
        currentQuestionIndex--;
        renderQuestion();
        updateProgress();
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
}

// Go to next question
function goToNext() {
    const currentQuestion = questions[currentQuestionIndex];

    // Validate response
    if (!responses[currentQuestion.question_id]) {
        alert('Please select an answer before continuing.');
        return;
    }

    if (currentQuestionIndex < questions.length - 1) {
        currentQuestionIndex++;
        renderQuestion();
        updateProgress();
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
}

// Handle form submission
async function handleSubmit(event) {
    event.preventDefault();

    const currentQuestion = questions[currentQuestionIndex];

    // Validate final response
    if (!responses[currentQuestion.question_id]) {
        alert('Please select an answer before submitting.');
        return;
    }

    // Show loading modal
    const modal = document.getElementById('loadingModal');
    modal.classList.add('active');

    try {
        // Submit responses to backend
        const response = await fetch('/api/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ responses: responses })
        });

        const result = await response.json();

        if (result.success) {
            // Redirect to results page
            window.location.href = '/results';
        } else {
            throw new Error('Submission failed');
        }
    } catch (error) {
        console.error('Error submitting responses:', error);
        modal.classList.remove('active');
        alert('Failed to submit your responses. Please try again.');
    }
}
