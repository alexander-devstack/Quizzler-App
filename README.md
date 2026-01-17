# Quizzler – API-Powered Trivia Quiz (Tkinter)

Quizzler is a Python quiz application that fetches True/False trivia questions from the **Open Trivia Database API**, displays them in a clean Tkinter GUI, and tracks your score in real time.[file:380][file:383][file:381]

> This project demonstrates API integration with `requests`, OOP design, and event-driven GUI programming with Tkinter.[file:380][file:383]

---

## Features

- Fetches 10 random True/False questions from the Open Trivia Database on startup.[file:380]  
- Clean Tkinter interface with a dark theme (`#375362`) and a white question canvas.[file:383]  
- Two button controls: **True** and **False** with image icons.[file:383]  
- Visual feedback: canvas background flashes **green** for correct and **red** for incorrect answers.[file:383]  
- Real-time score display in the top-right corner.[file:383]  
- Automatically unescapes HTML entities in questions (e.g., `&quot;` becomes `"`).[file:382]  
- Shows a completion message and disables buttons when all questions are answered.[file:383]

---

## How it works

### Architecture

The app uses a **Model-View-Controller (MVC)** pattern:

- **Model**: `Question` class stores each question and its correct answer.[file:379][file:381]  
- **Controller**: `QuizBrain` manages quiz state (score, current question, answer checking).[file:382]  
- **View**: `QuizInterface` handles all UI rendering and user interaction.[file:383]  
- **Data layer**: `data.py` fetches questions from the API.[file:380]

### Components

#### `question_model.py`

Defines the `Question` class with two attributes:
- `text`: the question text
- `answer`: the correct answer (string)[file:379][file:381]

#### `data.py`

- Uses `requests` to call the Open Trivia Database API with these parameters:
  - `amount=10`: fetch 10 questions
  - `type=boolean`: True/False questions only[file:380]
- Parses the JSON response and extracts the `results` array into `question_data`.[file:380]
- Includes commented fallback data in case the API is unavailable.[file:380]

#### `quiz_brain.py`

**`QuizBrain` class:**

- **Attributes:**
  - `question_number`: current question index (0-based)
  - `score`: number of correct answers
  - `question_list`: list of `Question` objects
  - `current_question`: the active question[file:382]

- **Methods:**
  - `still_has_questions()`: returns `True` if more questions remain.[file:382]
  - `next_question()`: advances to the next question, unescapes HTML entities, and returns formatted question text (`Q.1: ...`).[file:382]
  - `check_answer(user_answer)`: compares user input (case-insensitive) to the correct answer, increments score if correct, and returns `True`/`False`.[file:382]

#### `ui.py`

**`QuizInterface` class:**

- **Initialization:**
  - Creates a Tk window titled **"Quizzler"** with dark background.[file:383]
  - Canvas (300×250) displays the question text centered, word-wrapped to 280 pixels.[file:383]
  - Score label in the top-right shows `Score: 0` initially.[file:383]
  - Two buttons with PNG images (`images/true.png` and `images/false.png`).[file:383]
  - Calls `get_next_question()` to load the first question immediately.[file:383]

- **Methods:**
  - `get_next_question()`:
    - Resets canvas background to white.
    - If questions remain, updates the score label and question text.
    - If quiz is complete, shows a congratulations message and disables buttons.[file:383]
  
  - `right_answer()` / `wrong_answer()`:
    - Pass `"True"` or `"False"` to `quiz.check_answer()`.[file:383]
    - Call `give_feedback()` with the result.[file:383]
  
  - `give_feedback(is_right)`:
    - Changes canvas background to **green** (correct) or **red** (incorrect).
    - After 1 second, calls `get_next_question()` to load the next question.[file:383]

#### `main.py`

- Imports all modules and fetches `question_data` from `data.py`.[file:381]  
- Converts each dictionary in `question_data` into a `Question` object and builds `question_bank`.[file:381]  
- Creates a `QuizBrain` instance with the question bank.[file:381]  
- Launches `QuizInterface`, which runs the Tkinter event loop.[file:381]  
- After the window closes, prints the final score to the console.[file:381]

---

## File structure
.
├── main.py
├── question_model.py
├── data.py
├── quiz_brain.py
├── ui.py
└── images

## Requirements
Python 3.10+

Libraries:

tkinter (standard library)

requests

html (standard library)[file:380][file:382][file:383]

## How to run
1.Clone the repository and navigate to the project folder.
2.Ensure the images folder contains true.png and false.png.[file:383]
3.Install dependencies (see Requirements).

## Run the app:

bash
python main.py
1.Answer each question by clicking the True or False button.[file:383]
2.Watch the canvas background flash green or red for instant feedback.[file:383]
3.Your final score will be printed to the console when you complete all 10 questions.[file:381]

### Customization
1.Change question count or category
2.Edit the parameters dictionary in data.py:
parameters = {
    "amount": 20,           # fetch 20 questions
    "type": "boolean",
    "category": 18          # add a category ID (18 = Science: Computers)
}
3.See the Open Trivia Database API docs for all available categories and parameters.[file:380]
4.Use multiple choice questions
Change "type": "boolean" to "type": "multiple" in data.py.[file:380]
Update ui.py to add four answer buttons instead of two.[file:383]
Modify quiz_brain.py to handle multiple choices.[file:382]

### Notes
This project is a learning exercise for API integration, OOP design, and Tkinter GUI development.[file:380][file:381][file:383]
The app requires an internet connection to fetch questions from the API.[file:380]
HTML entities in questions (like &quot; or &#039;) are automatically decoded using html.unescape().[file:382]

    ├── true.png
    └── false.png
