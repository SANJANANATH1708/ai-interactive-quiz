
import streamlit as st
import random
import re

st.set_page_config(
    page_title="AI Interactive Quiz Game",
    page_icon="🧠",
    layout="centered"
)

# --------------------------------------------------
# QUESTION BANK: EXACTLY 50 QUESTIONS
# --------------------------------------------------

QUESTIONS = [
    # 1–15: MCQs
    {
        "type": "MCQ",
        "q": "Who introduced the term Artificial Intelligence?",
        "options": ["Alan Turing", "John McCarthy", "Charles Babbage", "Bill Gates"],
        "answer": 1,
        "explanation": "John McCarthy introduced the term Artificial Intelligence."
    },
    {
        "type": "MCQ",
        "q": "The Turing Test is associated with which scientist?",
        "options": ["Alan Turing", "John McCarthy", "Herbert Simon", "Marvin Minsky"],
        "answer": 0,
        "explanation": "Alan Turing proposed the test to evaluate machine behaviour."
    },
    {
        "type": "MCQ",
        "q": "An AI agent perceives its environment through:",
        "options": ["Sensors", "Effectors", "Printers", "Compilers"],
        "answer": 0,
        "explanation": "Sensors collect information from the environment."
    },
    {
        "type": "MCQ",
        "q": "An agent acts upon its environment through:",
        "options": ["Sensors", "Effectors", "Percepts", "Databases"],
        "answer": 1,
        "explanation": "Effectors or actuators enable an agent to perform actions."
    },
    {
        "type": "MCQ",
        "q": "The information an agent receives at a particular time is called:",
        "options": ["Path cost", "Percept", "Goal test", "Heuristic"],
        "answer": 1,
        "explanation": "A percept is the information received by an agent at a particular time."
    },
    {
        "type": "MCQ",
        "q": "A rational agent chooses an action expected to:",
        "options": [
            "Maximise its performance measure",
            "Use the most memory",
            "Take the longest time",
            "Ignore its environment"
        ],
        "answer": 0,
        "explanation": "A rational agent selects actions that maximise expected performance."
    },
    {
        "type": "MCQ",
        "q": "Which is a performance measure for a vacuum-cleaning agent?",
        "options": [
            "Amount of dust removed",
            "Colour of the vacuum",
            "Brand of the battery",
            "Packaging size"
        ],
        "answer": 0,
        "explanation": "The amount of dust removed helps measure cleaning performance."
    },
    {
        "type": "MCQ",
        "q": "Which is NOT a basic component of problem formulation?",
        "options": [
            "Initial state",
            "Successor function",
            "Goal test",
            "Monitor wallpaper"
        ],
        "answer": 3,
        "explanation": "Problem formulation includes the initial state, actions or successor function, goal test and path cost."
    },
    {
        "type": "MCQ",
        "q": "The collection of possible states and transitions in a problem is called:",
        "options": ["State space", "Operating system", "Data type", "Memory card"],
        "answer": 0,
        "explanation": "A state space represents the possible states and transitions of a problem."
    },
    {
        "type": "MCQ",
        "q": "Which data structure is commonly used by Breadth-First Search (BFS)?",
        "options": ["Queue", "Stack only", "Spreadsheet", "Image file"],
        "answer": 0,
        "explanation": "BFS uses a queue to explore nodes level by level."
    },
    {
        "type": "MCQ",
        "q": "Which data structure is commonly associated with Depth-First Search (DFS)?",
        "options": ["Queue only", "Stack", "Spreadsheet", "Image file"],
        "answer": 1,
        "explanation": "DFS uses a stack or recursive calls to explore a branch deeply."
    },
    {
        "type": "MCQ",
        "q": "A heuristic function h(n) estimates:",
        "options": [
            "The estimated cost from a node to the goal",
            "The colour of a node",
            "The computer's battery level",
            "The number of users online"
        ],
        "answer": 0,
        "explanation": "A heuristic estimates the remaining cost or distance to the goal."
    },
    {
        "type": "MCQ",
        "q": "A* Search evaluates a node using:",
        "options": ["f(n) = g(n) + h(n)", "f(n) = g(n) - h(n)", "f(n) = h(n) only", "f(n) = g(n) × h(n)"],
        "answer": 0,
        "explanation": "A* combines the path cost so far, g(n), with the heuristic estimate, h(n)."
    },
    {
        "type": "MCQ",
        "q": "A Constraint Satisfaction Problem (CSP) consists of:",
        "options": [
            "Variables, domains and constraints",
            "Only images and videos",
            "Only a goal test",
            "Only a queue"
        ],
        "answer": 0,
        "explanation": "CSPs are defined by variables, their domains and constraints."
    },
    {
        "type": "MCQ",
        "q": "Hill Climbing chooses a move mainly by:",
        "options": [
            "Improving the current state's evaluation",
            "Always returning to the initial state",
            "Ignoring neighbouring states",
            "Selecting a random file"
        ],
        "answer": 0,
        "explanation": "Hill Climbing moves towards a neighbouring state with a better evaluation."
    },

    # 16–20: TRUE/FALSE
    {
        "type": "True/False",
        "q": "AI systems can be designed to learn from data.",
        "options": ["True", "False"],
        "answer": 0,
        "explanation": "Machine learning allows AI systems to learn patterns from data."
    },
    {
        "type": "True/False",
        "q": "BFS explores nodes level by level.",
        "options": ["True", "False"],
        "answer": 0,
        "explanation": "BFS explores nodes in increasing order of depth."
    },
    {
        "type": "True/False",
        "q": "DFS always finds the shortest path in every search problem.",
        "options": ["True", "False"],
        "answer": 1,
        "explanation": "DFS does not generally guarantee the shortest path."
    },
    {
        "type": "True/False",
        "q": "A deterministic environment has its next state determined by the current state and action.",
        "options": ["True", "False"],
        "answer": 0,
        "explanation": "In a deterministic environment, the current state and action determine the next state."
    },
    {
        "type": "True/False",
        "q": "An optimal solution has the lowest path cost among the available solutions.",
        "options": ["True", "False"],
        "answer": 0,
        "explanation": "An optimal solution is the least-cost solution."
    },

    # 21–25: ASSERTION–REASON
    {
        "type": "Assertion–Reason",
        "q": "Assertion: A* uses both path cost so far and a heuristic estimate. Reason: Its evaluation is f(n) = g(n) + h(n).",
        "options": [
            "Both are true, and the reason explains the assertion",
            "Both are true, but the reason does not explain the assertion",
            "Assertion is true, reason is false",
            "Assertion is false, reason is true"
        ],
        "answer": 0,
        "explanation": "The formula directly explains why A* uses both costs."
    },
    {
        "type": "Assertion–Reason",
        "q": "Assertion: BFS uses a queue. Reason: A queue processes nodes in first-in, first-out order.",
        "options": [
            "Both are true, and the reason explains the assertion",
            "Both are true, but the reason does not explain the assertion",
            "Assertion is true, reason is false",
            "Assertion is false, reason is true"
        ],
        "answer": 0,
        "explanation": "FIFO ordering helps BFS explore each depth level before the next."
    },
    {
        "type": "Assertion–Reason",
        "q": "Assertion: A rational agent considers its performance measure. Reason: Rational behaviour aims to maximise expected performance.",
        "options": [
            "Both are true, and the reason explains the assertion",
            "Both are true, but the reason does not explain the assertion",
            "Assertion is true, reason is false",
            "Assertion is false, reason is true"
        ],
        "answer": 0,
        "explanation": "The performance measure helps determine how successful an agent's actions are."
    },
    {
        "type": "Assertion–Reason",
        "q": "Assertion: DFS explores a branch deeply before backtracking. Reason: DFS commonly uses a stack or recursion.",
        "options": [
            "Both are true, and the reason explains the assertion",
            "Both are true, but the reason does not explain the assertion",
            "Assertion is true, reason is false",
            "Assertion is false, reason is true"
        ],
        "answer": 0,
        "explanation": "The stack or recursive approach supports depth-first exploration."
    },
    {
        "type": "Assertion–Reason",
        "q": "Assertion: A CSP has variables, domains and constraints. Reason: Constraints specify which combinations of values are allowed.",
        "options": [
            "Both are true, and the reason explains the assertion",
            "Both are true, but the reason does not explain the assertion",
            "Assertion is true, reason is false",
            "Assertion is false, reason is true"
        ],
        "answer": 0,
        "explanation": "Constraints restrict the permitted assignments to CSP variables."
    },

    # 26–30: FILL IN THE BLANKS
    {
        "type": "Fill in the Blank",
        "q": "The collection of possible states in a problem is called the ______.",
        "answers": ["state space", "statespace"],
        "explanation": "The state space contains the possible states of a problem."
    },
    {
        "type": "Fill in the Blank",
        "q": "The information received by an agent at a particular time is called a ______.",
        "answers": ["percept"],
        "explanation": "A percept is the input an agent receives at a particular time."
    },
    {
        "type": "Fill in the Blank",
        "q": "BFS commonly uses a ______ to manage the nodes waiting to be explored.",
        "answers": ["queue"],
        "explanation": "A queue follows first-in, first-out ordering."
    },
    {
        "type": "Fill in the Blank",
        "q": "In A* Search, f(n) = g(n) + ______.",
        "answers": ["h(n)", "hn", "h"],
        "explanation": "h(n) is the heuristic estimate of the remaining cost."
    },
    {
        "type": "Fill in the Blank",
        "q": "A CSP consists of variables, domains and ______.",
        "answers": ["constraints", "constraint"],
        "explanation": "Constraints specify which assignments are permitted."
    },

    # 31–35: MATCH THE FOLLOWING
    {
        "type": "Match the Following",
        "q": "Match each AI term with its correct description.",
        "left": ["BFS", "DFS", "CSP", "Heuristic"],
        "matches": [
            "Explores level by level",
            "Explores a branch deeply",
            "Variables, domains and constraints",
            "Estimates remaining cost"
        ],
        "correct": {
            "BFS": "Explores level by level",
            "DFS": "Explores a branch deeply",
            "CSP": "Variables, domains and constraints",
            "Heuristic": "Estimates remaining cost"
        },
        "explanation": "Each term describes a different search technique or problem-solving concept."
    },
    {
        "type": "Match the Following",
        "q": "Match each agent term with its function.",
        "left": ["Sensors", "Effectors", "Percept", "Performance measure"],
        "matches": [
            "Receive information",
            "Perform actions",
            "Information received at a time",
            "Evaluates success"
        ],
        "correct": {
            "Sensors": "Receive information",
            "Effectors": "Perform actions",
            "Percept": "Information received at a time",
            "Performance measure": "Evaluates success"
        },
        "explanation": "Sensors perceive, effectors act, percepts are received information, and performance measures evaluate results."
    },
    {
        "type": "Match the Following",
        "q": "Match each problem component with its meaning.",
        "left": ["Initial state", "Successor function", "Goal test", "Path cost"],
        "matches": [
            "Starting point",
            "Possible next states",
            "Checks goal achievement",
            "Cost of a path"
        ],
        "correct": {
            "Initial state": "Starting point",
            "Successor function": "Possible next states",
            "Goal test": "Checks goal achievement",
            "Path cost": "Cost of a path"
        },
        "explanation": "These components describe the starting point, possible actions, goal condition and solution cost."
    },
    {
        "type": "Match the Following",
        "q": "Match each algorithm with its characteristic.",
        "left": ["Iterative Deepening", "Hill Climbing", "Best-First Search", "A* Search"],
        "matches": [
            "Increasing depth limits",
            "Improves the current state",
            "Selects a promising node",
            "Uses g(n) + h(n)"
        ],
        "correct": {
            "Iterative Deepening": "Increasing depth limits",
            "Hill Climbing": "Improves the current state",
            "Best-First Search": "Selects a promising node",
            "A* Search": "Uses g(n) + h(n)"
        },
        "explanation": "Each algorithm selects or explores states using a different strategy."
    },
    {
        "type": "Match the Following",
        "q": "Match each real-world task with its AI application.",
        "left": ["Spam email detection", "Movie suggestions", "Fraud detection", "Route planning"],
        "matches": [
            "Message classification",
            "Recommendation system",
            "Unusual transaction detection",
            "Search algorithms"
        ],
        "correct": {
            "Spam email detection": "Message classification",
            "Movie suggestions": "Recommendation system",
            "Fraud detection": "Unusual transaction detection",
            "Route planning": "Search algorithms"
        },
        "explanation": "These are examples of classification, recommendation, anomaly detection and search."
    },

    # 36–45: SCENARIO / APPLICATION-BASED
    {
        "type": "Scenario/Application",
        "q": "An email system automatically separates spam messages from useful emails. Which AI task is being performed?",
        "options": ["Classification", "Disk partitioning", "Screen calibration", "Cable management"],
        "answer": 0,
        "explanation": "The system classifies messages into categories such as spam and non-spam."
    },
    {
        "type": "Scenario/Application",
        "q": "A streaming platform suggests films based on a user's viewing history. Which application is this?",
        "options": ["Recommendation system", "File compression", "Operating system scheduling", "Image printing"],
        "answer": 0,
        "explanation": "Recommendation systems suggest items based on preferences and available data."
    },
    {
        "type": "Scenario/Application",
        "q": "A self-driving car uses sensors mainly to:",
        "options": [
            "Perceive roads and surrounding objects",
            "Decorate the dashboard",
            "Increase screen brightness",
            "Print maps"
        ],
        "answer": 0,
        "explanation": "Sensors provide information about roads, vehicles, pedestrians and other surroundings."
    },
    {
        "type": "Scenario/Application",
        "q": "A bank's fraud-detection AI may identify:",
        "options": [
            "Unusual transaction patterns",
            "Only the colour of banknotes",
            "The user's screen size",
            "The number of keyboard keys"
        ],
        "answer": 0,
        "explanation": "AI can identify suspicious or unusual transaction patterns."
    },
    {
        "type": "Scenario/Application",
        "q": "A medical decision-support system can use AI to:",
        "options": [
            "Analyse symptoms and support diagnosis",
            "Guarantee every diagnosis without error",
            "Replace all medical evidence",
            "Work without any input"
        ],
        "answer": 0,
        "explanation": "AI can assist healthcare professionals by analysing information; it cannot guarantee error-free diagnoses."
    },
    {
        "type": "Scenario/Application",
        "q": "A robot vacuum detects dirt and changes its movement to clean the floor. What does this demonstrate?",
        "options": [
            "An agent perceiving and acting on its environment",
            "A computer changing its wallpaper",
            "A printer formatting a document",
            "A database sorting filenames"
        ],
        "answer": 0,
        "explanation": "The vacuum uses sensor information to choose actions in its environment."
    },
    {
        "type": "Scenario/Application",
        "q": "A university must create a timetable without room clashes or overlapping exams for students. Which approach fits best?",
        "options": [
            "Constraint Satisfaction Problem",
            "Random file selection",
            "Screen brightness adjustment",
            "Image compression"
        ],
        "answer": 0,
        "explanation": "Timetabling can be formulated using variables, domains and scheduling constraints."
    },
    {
        "type": "Scenario/Application",
        "q": "A delivery robot must choose a route considering the distance travelled so far and the estimated distance remaining. Which algorithm fits this description?",
        "options": ["A* Search", "Random guessing", "Simple file sorting", "Wallpaper selection"],
        "answer": 0,
        "explanation": "A* combines the path cost so far with a heuristic estimate of the remaining cost."
    },
    {
        "type": "Scenario/Application",
        "q": "A chess program evaluates possible moves and chooses one expected to improve its position. Which idea does this illustrate?",
        "options": [
            "Rational action based on evaluation",
            "Ignoring the environment",
            "Choosing the longest route",
            "Randomly deleting states"
        ],
        "answer": 0,
        "explanation": "The program evaluates actions to select one expected to improve performance."
    },
    {
        "type": "Scenario/Application",
        "q": "A navigation system explores all locations one level away before exploring locations two levels away. Which search method is it using?",
        "options": ["BFS", "DFS", "Hill Climbing", "Random search"],
        "answer": 0,
        "explanation": "BFS explores nodes level by level."
    },

    # 46–50: PROBLEM-SOLVING / SEARCH QUESTIONS
    {
        "type": "Problem-Solving",
        "q": "A* Search has g(n) = 7 and h(n) = 4. Calculate f(n).",
        "options": ["3", "11", "28", "74"],
        "answer": 1,
        "explanation": "f(n) = g(n) + h(n) = 7 + 4 = 11."
    },
    {
        "type": "Problem-Solving",
        "q": "A search tree has root A, with children B and C. B has children D and E, and C has children F and G. With left-to-right traversal, what is the BFS order?",
        "options": [
            "A, B, C, D, E, F, G",
            "A, B, D, E, C, F, G",
            "A, C, G, F, B, E, D",
            "D, E, B, F, G, C, A"
        ],
        "answer": 0,
        "explanation": "BFS visits the root, then all nodes at depth one, then all nodes at depth two."
    },
    {
        "type": "Problem-Solving",
        "q": "Using the same tree (A has B and C; B has D and E; C has F and G), what is the DFS order when exploring left branches first?",
        "options": [
            "A, B, D, E, C, F, G",
            "A, B, C, D, E, F, G",
            "A, C, F, G, B, D, E",
            "D, E, F, G, A, B, C"
        ],
        "answer": 0,
        "explanation": "DFS explores the left branch deeply before backtracking to explore the next branch."
    },
    {
        "type": "Problem-Solving",
        "q": "A search begins at depth 0. Iterative Deepening first searches to depth 0, then depth 1, then depth 2. If the goal is at depth 2, at which limit can it first be found?",
        "options": ["0", "1", "2", "3 only"],
        "answer": 2,
        "explanation": "The goal at depth 2 can first be reached when the depth limit becomes 2."
    },
    {
        "type": "Problem-Solving",
        "q": "A route has three steps costing 2, 4 and 3. What is its total path cost?",
        "options": ["7", "8", "9", "12"],
        "answer": 2,
        "explanation": "Total path cost = 2 + 4 + 3 = 9."
    }
]

# --------------------------------------------------
# CHECK QUESTION COUNT
# --------------------------------------------------

assert len(QUESTIONS) == 50, f"Expected 50 questions, found {len(QUESTIONS)}"

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "quiz_questions" not in st.session_state:
    st.session_state.quiz_questions = random.sample(QUESTIONS, len(QUESTIONS))
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.submitted = False
    st.session_state.results = {}
    st.session_state.finished = False

quiz = st.session_state.quiz_questions

# --------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------

def normalise(text):
    text = text.strip().lower()
    text = re.sub(r"[^\w\s]", "", text)
    return re.sub(r"\s+", " ", text)

def evaluate_answer(question, response):
    qtype = question["type"]

    if qtype == "Match the Following":
        return all(
            response.get(item) == correct
            for item, correct in question["correct"].items()
        )

    if qtype == "Fill in the Blank":
        return normalise(response) in [
            normalise(answer) for answer in question["answers"]
        ]

    return response == question["answer"]

def show_question_input(question, q_index):
    qtype = question["type"]
    key = f"answer_{q_index}"

    if qtype == "Match the Following":
        st.write("Match each item on the left with its correct description.")
        response = {}
        for i, item in enumerate(question["left"]):
            response[item] = st.selectbox(
                item,
                ["-- Select a match --"] + question["matches"],
                key=f"{key}_{i}"
            )
        return response

    if qtype == "Fill in the Blank":
        return st.text_input(
            "Type your answer:",
            key=key,
            placeholder="Enter your answer here"
        )

    return st.radio(
        "Choose your answer:",
        question["options"],
        index=None,
        key=key
    )

# --------------------------------------------------
# APP HEADER
# --------------------------------------------------

st.title("🧠 AI Interactive Quiz Game")
st.subheader("Units I & II | Foundations and Search Techniques")

st.write(
    "Test your understanding of Artificial Intelligence, intelligent agents, "
    "problem formulation, state-space search, and heuristic methods."
)

st.info(
    "50 questions • Random order • 7 question formats • "
    "Instant feedback • Final score"
)

# --------------------------------------------------
# QUIZ SCREEN
# --------------------------------------------------

if not st.session_state.finished:
    index = st.session_state.current
    question = quiz[index]

    st.progress((index + 1) / len(quiz))
    st.caption(
        f"Question {index + 1} of {len(quiz)} | "
        f"Type: {question['type']}"
    )

    st.markdown(f"### {question['q']}")

    response = show_question_input(question, index)

    if not st.session_state.submitted:
        if st.button("Submit Answer", type="primary", use_container_width=True):
            if question["type"] == "Match the Following":
                if any(
                    value == "-- Select a match --"
                    for value in response.values()
                ):
                    st.warning("Please complete all the matches before submitting.")
                    st.stop()

            elif question["type"] == "Fill in the Blank":
                if not response.strip():
                    st.warning("Please type your answer before submitting.")
                    st.stop()

            elif response is None:
                st.warning("Please select an answer before submitting.")
                st.stop()

            is_correct = evaluate_answer(question, response)

            st.session_state.results[index] = {
                "question": question["q"],
                "type": question["type"],
                "response": response,
                "correct": is_correct,
                "explanation": question["explanation"],
                "question_data": question
            }

            if is_correct:
                st.session_state.score += 1

            st.session_state.submitted = True
            st.rerun()

    else:
        result = st.session_state.results[index]

        if result["correct"]:
            st.success("Correct! 🎉")
        else:
            st.error("Incorrect.")

        st.info(f"Explanation: {question['explanation']}")

        if question["type"] == "Match the Following":
            st.write("Correct matches:")
            for item, answer in question["correct"].items():
                st.write(f"- **{item}:** {answer}")

        elif question["type"] == "Fill in the Blank":
            st.write(f"**Accepted answer:** {question['answers'][0]}")

        else:
            st.write(f"**Correct answer:** {question['options'][question['answer']]}")

        if index + 1 < len(quiz):
            if st.button("Next Question ➜", type="primary", use_container_width=True):
                st.session_state.current += 1
                st.session_state.submitted = False
                st.rerun()
        else:
            if st.button("View Final Result 🏆", type="primary", use_container_width=True):
                st.session_state.finished = True
                st.rerun()

    st.divider()
    st.caption(f"Current score: {st.session_state.score} / {len(quiz)}")

# --------------------------------------------------
# FINAL RESULTS
# --------------------------------------------------

else:
    score = st.session_state.score
    total = len(quiz)
    percentage = score / total * 100

    st.balloons()
    st.success("🎉 Quiz completed!")

    st.metric("Your Score", f"{score} / {total}")
    st.metric("Percentage", f"{percentage:.1f}%")
    st.progress(score / total)

    if percentage >= 80:
        st.write("Excellent work! You have a strong understanding of these topics.")
    elif percentage >= 60:
        st.write("Good job! Review the questions you missed to improve further.")
    else:
        st.write("Keep practising! Review the explanations and try again.")

    st.subheader("📋 Review Your Answers")

    for i, question in enumerate(quiz):
        result = st.session_state.results.get(i)

        if result is None:
            continue

        with st.expander(
            f"Question {i + 1}: {question['q']} "
            f"{'✅' if result['correct'] else '❌'}"
        ):
            st.write(f"**Format:** {question['type']}")

            if question["type"] == "Match the Following":
                st.write("**Your matches:**")
                for item, answer in result["response"].items():
                    st.write(f"- {item}: {answer}")
                st.write("**Correct matches:**")
                for item, answer in question["correct"].items():
                    st.write(f"- {item}: {answer}")

            elif question["type"] == "Fill in the Blank":
                st.write(f"**Your answer:** {result['response']}")
                st.write(f"**Accepted answer:** {question['answers'][0]}")

            else:
                st.write(f"**Your answer:** {question['options'][result['response']]}")
                st.write(f"**Correct answer:** {question['options'][question['answer']]}")

            st.write(f"**Explanation:** {question['explanation']}")

    st.divider()

    if st.button("🔄 Restart Quiz", type="primary", use_container_width=True):
        for key in [
            "quiz_questions",
            "current",
            "score",
            "submitted",
            "results",
            "finished"
        ]:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

    st.caption("AI Interactive Quiz Game | Academic Assignment")
