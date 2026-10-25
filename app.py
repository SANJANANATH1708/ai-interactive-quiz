
import streamlit as st
import random

st.set_page_config(
    page_title="AI Interactive Quiz Game",
    page_icon="🧠",
    layout="centered"
)

# ---------------- QUESTION BANK: EXACTLY 50 QUESTIONS ----------------

QUESTIONS = [
    # 1–10: MCQs
    {
        "type": "MCQ",
        "question": "Who introduced the term Artificial Intelligence?",
        "options": ["Alan Turing", "John McCarthy", "Charles Babbage", "Marvin Minsky"],
        "answer": 1,
        "explanation": "John McCarthy introduced the term Artificial Intelligence."
    },
    {
        "type": "MCQ",
        "question": "The main aim of Artificial Intelligence is to:",
        "options": ["Store files only", "Perform tasks requiring intelligence", "Replace all hardware", "Create documents only"],
        "answer": 1,
        "explanation": "AI develops systems capable of performing tasks that normally require human intelligence."
    },
    {
        "type": "MCQ",
        "question": "The Turing Test was proposed by:",
        "options": ["John McCarthy", "Alan Turing", "Herbert Simon", "Charles Babbage"],
        "answer": 1,
        "explanation": "Alan Turing proposed the test to evaluate machine behaviour."
    },
    {
        "type": "MCQ",
        "question": "An intelligent agent perceives its environment using:",
        "options": ["Sensors", "Effectors", "Printers", "Compilers"],
        "answer": 0,
        "explanation": "Sensors allow an agent to receive information from its environment."
    },
    {
        "type": "MCQ",
        "question": "An agent acts on its environment through:",
        "options": ["Sensors", "Effectors or actuators", "Percepts", "Databases only"],
        "answer": 1,
        "explanation": "Effectors or actuators allow an agent to perform actions."
    },
    {
        "type": "MCQ",
        "question": "A rational agent chooses an action expected to:",
        "options": ["Maximise its performance measure", "Use the most memory", "Take the longest time", "Ignore its environment"],
        "answer": 0,
        "explanation": "A rational agent selects actions expected to maximise its performance measure."
    },
    {
        "type": "MCQ",
        "question": "The information an agent receives at a particular time is called:",
        "options": ["Percept", "Path cost", "Goal test", "Heuristic"],
        "answer": 0,
        "explanation": "A percept is the information received by an agent at a particular time."
    },
    {
        "type": "MCQ",
        "question": "Which is a basic component of problem formulation?",
        "options": ["Monitor wallpaper", "Initial state", "Screen brightness", "File name"],
        "answer": 1,
        "explanation": "Problem formulation includes the initial state, actions or successor function, goal test, and path cost."
    },
    {
        "type": "MCQ",
        "question": "An optimal solution is the solution with:",
        "options": ["The largest number of steps", "The lowest path cost among solutions", "The most branches", "No goal state"],
        "answer": 1,
        "explanation": "An optimal solution has the lowest path cost among the possible solutions."
    },
    {
        "type": "MCQ",
        "question": "Which data structure is commonly used by BFS?",
        "options": ["Stack", "Queue", "Spreadsheet", "Image file"],
        "answer": 1,
        "explanation": "Breadth-First Search uses a FIFO queue to explore nodes level by level."
    },

    # 11–16: True/False
    {
        "type": "True/False",
        "question": "DFS always finds the shortest path in every search problem.",
        "options": ["True", "False"],
        "answer": 1,
        "explanation": "DFS does not generally guarantee the shortest path."
    },
    {
        "type": "True/False",
        "question": "A deterministic environment has its next state determined by the current state and action.",
        "options": ["True", "False"],
        "answer": 0,
        "explanation": "In a deterministic environment, the current state and action determine the next state."
    },
    {
        "type": "True/False",
        "question": "A heuristic function estimates how close a state is to the goal.",
        "options": ["True", "False"],
        "answer": 0,
        "explanation": "A heuristic provides an estimate that helps guide the search."
    },
    {
        "type": "True/False",
        "question": "BFS explores the deepest available node before exploring other levels.",
        "options": ["True", "False"],
        "answer": 1,
        "explanation": "BFS explores nodes level by level; DFS explores deeper branches first."
    },
    {
        "type": "True/False",
        "question": "A Constraint Satisfaction Problem includes variables, domains, and constraints.",
        "options": ["True", "False"],
        "answer": 0,
        "explanation": "Variables, their possible domains, and constraints are the main components of a CSP."
    },
    {
        "type": "True/False",
        "question": "A rational agent should ignore its performance measure when choosing an action.",
        "options": ["True", "False"],
        "answer": 1,
        "explanation": "A rational agent selects actions based on the expected performance measure."
    },

    # 17–21: Assertion–Reason
    {
        "type": "Assertion–Reason",
        "question": "Assertion: A* search uses both path cost and a heuristic estimate. Reason: Its evaluation function is f(n) = g(n) + h(n).",
        "options": [
            "Both are true, and the reason explains the assertion",
            "Both are true, but the reason does not explain the assertion",
            "Assertion is true, reason is false",
            "Assertion is false, reason is true"
        ],
        "answer": 0,
        "explanation": "A* combines the cost already incurred, g(n), and estimated remaining cost, h(n)."
    },
    {
        "type": "Assertion–Reason",
        "question": "Assertion: BFS explores nodes level by level. Reason: BFS commonly uses a FIFO queue.",
        "options": [
            "Both are true, and the reason explains the assertion",
            "Both are true, but the reason does not explain the assertion",
            "Assertion is true, reason is false",
            "Assertion is false, reason is true"
        ],
        "answer": 0,
        "explanation": "FIFO processing expands earlier-discovered nodes first, producing level-order exploration."
    },
    {
        "type": "Assertion–Reason",
        "question": "Assertion: A percept is information received by an agent. Reason: Sensors help an agent perceive its environment.",
        "options": [
            "Both are true, and the reason explains the assertion",
            "Both are true, but the reason does not explain the assertion",
            "Assertion is true, reason is false",
            "Assertion is false, reason is true"
        ],
        "answer": 1,
        "explanation": "Both statements are true, but the second describes how an agent receives information rather than explaining the definition of a percept."
    },
    {
        "type": "Assertion–Reason",
        "question": "Assertion: Hill climbing evaluates neighbouring states. Reason: It always explores every possible path before moving.",
        "options": [
            "Both are true, and the reason explains the assertion",
            "Both are true, but the reason does not explain the assertion",
            "Assertion is true, reason is false",
            "Assertion is false, reason is true"
        ],
        "answer": 2,
        "explanation": "Hill climbing evaluates neighbouring states, but it does not systematically explore every possible path."
    },
    {
        "type": "Assertion–Reason",
        "question": "Assertion: A CSP is defined using variables, domains, and constraints. Reason: A CSP must use a stack to represent every variable.",
        "options": [
            "Both are true, and the reason explains the assertion",
            "Both are true, but the reason does not explain the assertion",
            "Assertion is true, reason is false",
            "Assertion is false, reason is true"
        ],
        "answer": 2,
        "explanation": "Variables, domains, and constraints define a CSP; a stack is not a required component."
    },

    # 22–26: Fill in the Blanks
    {
        "type": "Fill in the Blank",
        "question": "The state from which a search problem begins is called the ______.",
        "options": ["Goal state", "Initial state", "Final cost", "Heuristic state"],
        "answer": 1,
        "explanation": "The initial state is the starting point of a search problem."
    },
    {
        "type": "Fill in the Blank",
        "question": "The function that estimates the remaining cost to the goal is called the ______ function.",
        "options": ["Successor", "Heuristic", "Percept", "Performance"],
        "answer": 1,
        "explanation": "The heuristic function estimates the remaining cost or distance to the goal."
    },
    {
        "type": "Fill in the Blank",
        "question": "The information an agent receives at a particular time is called a ______.",
        "options": ["Percept", "Constraint", "Path", "Domain"],
        "answer": 0,
        "explanation": "A percept is the information received by an agent at a particular time."
    },
    {
        "type": "Fill in the Blank",
        "question": "Breadth-First Search commonly uses a ______ data structure.",
        "options": ["Queue", "Stack", "Tree only", "Table"],
        "answer": 0,
        "explanation": "BFS uses a queue to process nodes in the order they are discovered."
    },
    {
        "type": "Fill in the Blank",
        "question": "A set of rules and a control strategy are components of a ______ system.",
        "options": ["Production", "Percept", "Sensor", "Random"],
        "answer": 0,
        "explanation": "A production system commonly contains production rules and a control strategy, along with working memory."
    },

    # 27–30: Match the Following
    {
        "type": "Match the Following",
        "question": "Match each search method with its usual behaviour.",
        "options": [
            "BFS – level by level; DFS – deep branch first; A* – path cost plus heuristic",
            "BFS – deep branch first; DFS – level by level; A* – alphabetical order",
            "BFS – heuristic only; DFS – random order; A* – no cost",
            "BFS – stack only; DFS – queue only; A* – sensors"
        ],
        "answer": 0,
        "explanation": "BFS explores by levels, DFS explores deeper branches first, and A* combines path cost and heuristic estimate."
    },
    {
        "type": "Match the Following",
        "question": "Match each agent term with its meaning.",
        "options": [
            "Sensor – receives information; Effector – performs actions; Performance measure – evaluates success",
            "Sensor – performs actions; Effector – receives information; Performance measure – stores images",
            "Sensor – calculates path cost; Effector – defines the goal; Performance measure – creates variables",
            "Sensor – stores rules; Effector – defines domains; Performance measure – selects a file"
        ],
        "answer": 0,
        "explanation": "Sensors receive information, effectors carry out actions, and performance measures evaluate an agent's success."
    },
    {
        "type": "Match the Following",
        "question": "Match each problem-formulation component with its role.",
        "options": [
            "Initial state – starting point; Goal test – checks success; Path cost – cost of a path",
            "Initial state – final result; Goal test – stores sensors; Path cost – number of variables only",
            "Initial state – heuristic value; Goal test – selects a queue; Path cost – action name",
            "Initial state – domain; Goal test – production rule; Path cost – environment type"
        ],
        "answer": 0,
        "explanation": "These are the respective roles of the initial state, goal test, and path cost."
    },
    {
        "type": "Match the Following",
        "question": "Match each method with its main characteristic.",
        "options": [
            "Hill climbing – improves a state; Iterative deepening – increases depth limits; Greedy best-first – uses a heuristic",
            "Hill climbing – explores all paths; Iterative deepening – uses no limits; Greedy best-first – ignores heuristics",
            "Hill climbing – uses only a queue; Iterative deepening – removes goals; Greedy best-first – sorts files",
            "Hill climbing – stores percepts; Iterative deepening – defines domains; Greedy best-first – uses sensors"
        ],
        "answer": 0,
        "explanation": "Each method is associated with the behaviour described in the first option."
    },

    # 31–35: Scenario/Application-Based
    {
        "type": "Scenario/Application",
        "question": "A streaming platform suggests movies based on a user's viewing history. Which AI application is this?",
        "options": ["Recommendation system", "File compression", "Screen recording", "Word processing"],
        "answer": 0,
        "explanation": "Recommendation systems suggest items based on user preferences and behaviour."
    },
    {
        "type": "Scenario/Application",
        "question": "A bank's AI system flags transactions that differ greatly from a customer's usual spending. What is the application?",
        "options": ["Fraud detection", "Image cropping", "Text formatting", "File sorting"],
        "answer": 0,
        "explanation": "Fraud detection systems identify unusual transaction patterns."
    },
    {
        "type": "Scenario/Application",
        "question": "A medical system analyses symptoms and test results to help a doctor. Which AI application is being used?",
        "options": ["Medical decision support", "Music recommendation", "File management", "Screen brightness control"],
        "answer": 0,
        "explanation": "AI can analyse medical information to support diagnosis and clinical decisions."
    },
    {
        "type": "Scenario/Application",
        "question": "A self-driving car detects nearby vehicles using cameras and sensors. These devices mainly help the car to:",
        "options": ["Perceive its environment", "Calculate only its battery size", "Remove its goal state", "Create CSP domains"],
        "answer": 0,
        "explanation": "Sensors provide information about the surroundings so the agent can choose actions."
    },
    {
        "type": "Scenario/Application",
        "question": "A virtual assistant recognises a spoken request and responds to it. This is an example of:",
        "options": ["AI-based language interaction", "A deterministic file name", "A manual paper process", "A simple storage folder"],
        "answer": 0,
        "explanation": "Virtual assistants use AI techniques to interpret requests and generate responses."
    },

    # 36–40: Problem-Solving Questions
    {
        "type": "Problem-Solving",
        "question": "A search tree has a root at depth 0. The goal is at depth 2, and all nodes at depth 0 and depth 1 must be explored first. Which method follows this level-order approach?",
        "options": ["BFS", "DFS", "Hill climbing", "Random search"],
        "answer": 0,
        "explanation": "BFS explores nodes level by level, so it processes shallower levels before deeper ones."
    },
    {
        "type": "Problem-Solving",
        "question": "A* evaluates a node using g(n) = 5 and h(n) = 3. Given f(n) = g(n) + h(n), what is f(n)?",
        "options": ["2", "8", "15", "53"],
        "answer": 1,
        "explanation": "f(n) = 5 + 3 = 8."
    },
    {
        "type": "Problem-Solving",
        "question": "A delivery route has already cost 12 units. The heuristic estimates 7 more units to reach the goal. Using A* evaluation, what is the total estimated cost?",
        "options": ["5 units", "19 units", "84 units", "12 units"],
        "answer": 1,
        "explanation": "A* adds the cost so far and estimated remaining cost: 12 + 7 = 19."
    },
    {
        "type": "Problem-Solving",
        "question": "A timetable has 3 courses. Each course can be assigned one of 4 time slots, and there are no additional restrictions. How many possible assignments are there?",
        "options": ["7", "12", "64", "81"],
        "answer": 1,
        "explanation": "Each of the 3 courses has 4 choices, giving 4 × 4 × 4 = 64 assignments. The correct option should be 64.",
    },
    {
        "type": "Problem-Solving",
        "question": "A search problem has a path with costs 4, 3, and 2. What is the total path cost?",
        "options": ["5", "7", "9", "24"],
        "answer": 2,
        "explanation": "The total path cost is 4 + 3 + 2 = 9."
    },

    # 41–50: Additional varied questions
    {
        "type": "MCQ",
        "question": "Which search method repeatedly performs depth-limited search with increasing limits?",
        "options": ["Iterative deepening", "Greedy best-first", "Hill climbing", "Uniform random search"],
        "answer": 0,
        "explanation": "Iterative deepening increases the depth limit across repeated searches."
    },
    {
        "type": "MCQ",
        "question": "Best-First Search selects the next node using:",
        "options": ["An evaluation of how promising the node is", "Alphabetical order only", "The screen size", "The file name only"],
        "answer": 0,
        "explanation": "Best-First Search uses an evaluation function to select a promising node."
    },
    {
        "type": "MCQ",
        "question": "A search algorithm that uses no heuristic information is called:",
        "options": ["Uninformed search", "Informed search", "Neural search only", "Image search"],
        "answer": 0,
        "explanation": "Uninformed search does not use heuristic information about the goal."
    },
    {
        "type": "MCQ",
        "question": "Hill climbing chooses a move mainly based on:",
        "options": ["Improving the current state's evaluation", "Always returning to the initial state", "Ignoring neighbouring states", "Selecting a random file"],
        "answer": 0,
        "explanation": "Hill climbing moves towards a neighbouring state with a better evaluation."
    },
    {
        "type": "MCQ",
        "question": "A Constraint Satisfaction Problem consists of:",
        "options": ["Variables, domains, and constraints", "Only images and videos", "Only a goal test", "Only a queue"],
        "answer": 0,
        "explanation": "A CSP is defined by variables, their domains, and constraints."
    },
    {
        "type": "Scenario/Application",
        "question": "A university creates an examination timetable without overlapping exams for students. Which technique is suitable?",
        "options": ["Constraint Satisfaction Problem", "Image enhancement", "Random file selection", "Text compression"],
        "answer": 0,
        "explanation": "Timetabling can be modelled as a CSP with courses, time slots, and conflict constraints."
    },
    {
        "type": "Scenario/Application",
        "question": "A robot must find a route while considering the distance already travelled and the estimated distance remaining. Which algorithm fits?",
        "options": ["A* Search", "Random guessing", "Simple file sorting", "Text formatting"],
        "answer": 0,
        "explanation": "A* combines the path cost so far with a heuristic estimate of the remaining cost."
    },
    {
        "type": "Problem-Solving",
        "question": "A node has g(n) = 6 and h(n) = 4. Using A* evaluation f(n) = g(n) + h(n), calculate f(n).",
        "options": ["2", "10", "24", "64"],
        "answer": 1,
        "explanation": "f(n) = 6 + 4 = 10."
    },
    {
        "type": "Fill in the Blank",
        "question": "A search tree node generally represents a ______ in the search process.",
        "options": ["State", "Printer setting", "File name", "Programming language"],
        "answer": 0,
        "explanation": "A search tree node represents a state reached during the search process."
    },
    {
        "type": "MCQ",
        "question": "Means-End Analysis works by:",
        "options": ["Reducing the difference between the current state and goal state", "Ignoring the goal", "Selecting actions randomly", "Removing all constraints"],
        "answer": 0,
        "explanation": "Means-End Analysis identifies differences between the current and goal states and selects actions to reduce them."
    }
]

# Correct the timetable calculation item: 4 choices for each of 3 courses = 64.
QUESTIONS[38]["options"] = ["7", "12", "64", "81"]
QUESTIONS[38]["answer"] = 2
QUESTIONS[38]["explanation"] = "Each of the 3 courses has 4 choices, so the number of assignments is 4 × 4 × 4 = 64."

# ---------------- SESSION STATE ----------------

if "started" not in st.session_state:
    st.session_state.started = False

if "finished" not in st.session_state:
    st.session_state.finished = False

if "question_order" not in st.session_state:
    st.session_state.question_order = []

if "current" not in st.session_state:
    st.session_state.current = 0

if "answers" not in st.session_state:
    st.session_state.answers = {}

if "submitted" not in st.session_state:
    st.session_state.submitted = False


def start_quiz():
    st.session_state.question_order = list(range(len(QUESTIONS)))
    random.shuffle(st.session_state.question_order)
    st.session_state.current = 0
    st.session_state.answers = {}
    st.session_state.submitted = False
    st.session_state.finished = False
    st.session_state.started = True


def restart_quiz():
    st.session_state.started = False
    st.session_state.finished = False
    st.session_state.question_order = []
    st.session_state.current = 0
    st.session_state.answers = {}
    st.session_state.submitted = False


# ---------------- PAGE DESIGN ----------------

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

# ---------------- START SCREEN ----------------

if not st.session_state.started:
    st.markdown("### Welcome to the AI Quiz!")
    st.write("Read the following instructions before starting:")

    st.markdown("""
    - The quiz contains exactly **50 questions**.
    - Questions appear in a random order.
    - Select one answer for each question.
    - Click **Submit Answer** to check your answer.
    - Feedback and an explanation appear after submission.
    - Click **Next Question** to continue.
    - Your final score and answer review appear at the end.
    """)

    st.markdown("**Question formats included:**")
    st.write(
        "MCQ, True/False, Assertion–Reason, Fill in the Blanks, "
        "Match the Following, Scenario/Application-based, and Problem-solving."
    )

    st.divider()

    if st.button("🚀 Start Quiz", type="primary", use_container_width=True):
        start_quiz()
        st.rerun()

# ---------------- QUIZ SCREEN ----------------

elif not st.session_state.finished:

    current = st.session_state.current
    question_index = st.session_state.question_order[current]
    question = QUESTIONS[question_index]

    total = len(QUESTIONS)
    answered_count = len(st.session_state.answers)

    st.progress((current + 1) / total)
    st.caption(
        f"Question {current + 1} of {total} | Type: {question['type']}"
    )

    st.markdown(f"### {question['question']}")
    st.write("**Choose your answer:**")

    choice_key = f"choice_{current}"

    if not st.session_state.submitted:
        selected = st.radio(
            "Options",
            question["options"],
            index=None,
            key=choice_key,
            label_visibility="collapsed"
        )

        if st.button("Submit Answer", type="primary", use_container_width=True):
            if selected is None:
                st.warning("Please select an answer before submitting.")
            else:
                selected_index = question["options"].index(selected)
                st.session_state.answers[current] = {
                    "question_index": question_index,
                    "selected": selected_index,
                    "correct": selected_index == question["answer"]
                }
                st.session_state.submitted = True
                st.rerun()

    else:
        result = st.session_state.answers[current]
        selected_index = result["selected"]
        correct_index = question["answer"]

        st.write(f"**Your answer:** {question['options'][selected_index]}")
        st.write(f"**Correct answer:** {question['options'][correct_index]}")

        if result["correct"]:
            st.success("Correct answer! 🎉")
        else:
            st.error("Not quite. Review the correct answer above.")

        st.info(f"**Explanation:** {question['explanation']}")

        if current + 1 < total:
            if st.button("Next Question ➡️", type="primary", use_container_width=True):
                st.session_state.current += 1
                st.session_state.submitted = False
                st.rerun()
        else:
            if st.button("View Final Result 🏆", type="primary", use_container_width=True):
                st.session_state.finished = True
                st.rerun()

    # Live score
    score = sum(
        1 for answer in st.session_state.answers.values()
        if answer["correct"]
    )
    st.divider()
    st.write(f"**Score so far:** {score} / {total}")
    st.write(f"**Questions answered:** {answered_count} / {total}")

# ---------------- FINAL RESULT SCREEN ----------------

else:
    total = len(QUESTIONS)
    score = sum(
        1 for answer in st.session_state.answers.values()
        if answer["correct"]
    )
    percentage = (score / total) * 100

    st.balloons()
    st.success("🎉 Quiz completed!")

    st.metric("Your Score", f"{score} / {total}")
    st.metric("Percentage", f"{percentage:.1f}%")
    st.progress(score / total)

    if percentage >= 80:
        st.write("Excellent work! You have a strong understanding of these topics.")
    elif percentage >= 60:
        st.write("Good job! Review the incorrect answers to improve further.")
    else:
        st.write("Keep practising. Review the explanations and try again.")

    st.divider()
    st.subheader("📋 Review Your Answers")

    for number, order_index in enumerate(st.session_state.question_order):
        answer_data = st.session_state.answers.get(number)

        if answer_data is None:
            continue

        question = QUESTIONS[answer_data["question_index"]]
        selected_index = answer_data["selected"]
        correct_index = question["answer"]

        with st.expander(
            f"Question {number + 1}: {question['question']}"
        ):
            st.write(f"**Format:** {question['type']}")
            st.write(f"**Your answer:** {question['options'][selected_index]}")
            st.write(f"**Correct answer:** {question['options'][correct_index]}")
            st.write(f"**Explanation:** {question['explanation']}")

            if answer_data["correct"]:
                st.success("Correct")
            else:
                st.error("Incorrect")

    st.divider()

    if st.button("🔄 Restart Quiz", type="primary", use_container_width=True):
        restart_quiz()
        st.rerun()

# ---------------- FOOTER ----------------

st.divider()
st.caption("AI Interactive Quiz Game | Academic Assignment")
