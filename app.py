import streamlit as st
import random

st.set_page_config(
    page_title="AI Interactive Quiz",
    page_icon="🧠",
    layout="centered"
)

# -------------------- QUESTION BANK --------------------
# Each question contains: question, options, correct answer index,
# explanation, and question type.

QUESTIONS = [
    ("Who introduced the term Artificial Intelligence?",
     ["Alan Turing", "John McCarthy", "Charles Babbage", "Bill Gates"],
     1, "John McCarthy introduced the term Artificial Intelligence.", "MCQ"),

    ("Artificial Intelligence mainly aims to create machines that can:",
     ["Only store files", "Perform tasks requiring intelligence", "Only calculate sums", "Replace computer hardware"],
     1, "AI focuses on tasks that normally require human intelligence.", "MCQ"),

    ("The Turing Test was proposed by:",
     ["John McCarthy", "Alan Turing", "Herbert Simon", "Marvin Minsky"],
     1, "Alan Turing proposed the test to evaluate machine behaviour.", "MCQ"),

    ("True or False: AI systems can be designed to learn from data.",
     ["True", "False"], 0,
     "AI systems can use data to learn patterns and improve performance.", "True/False"),

    ("An AI system that understands spoken commands uses:",
     ["Natural Language Processing", "Disk formatting", "File compression", "Screen resolution"],
     0, "Natural Language Processing helps computers process human language.", "Real-world application"),

    ("A rational agent chooses an action expected to:",
     ["Maximise its performance measure", "Use the most memory", "Take the longest time", "Ignore its environment"],
     0, "A rational agent selects actions that are expected to perform best based on available information.", "MCQ"),

    ("An agent receives information from its environment through:",
     ["Actuators", "Sensors", "Printers", "Compilers"],
     1, "Sensors allow an agent to perceive its environment.", "MCQ"),

    ("An agent acts upon its environment through:",
     ["Sensors", "Percepts", "Actuators", "Databases"],
     2, "Actuators or effectors are used to perform actions.", "MCQ"),

    ("The information an agent receives at a particular time is called a:",
     ["Percept", "Path cost", "Goal test", "Heuristic"],
     0, "A percept is the input received by an agent through its sensors.", "Fill in the blank"),

    ("A sequence of all percepts received by an agent is called:",
     ["Action sequence", "Percept sequence", "Search tree", "State space"],
     1, "The percept sequence includes the percepts received so far.", "MCQ"),

    ("Which is an example of an intelligent agent?",
     ["A thermostat that responds to temperature", "A blank notebook", "A chair", "A switched-off monitor"],
     0, "A thermostat senses temperature and takes action based on it.", "Real-world application"),

    ("A self-driving car uses sensors mainly to:",
     ["Decorate the dashboard", "Perceive roads and surrounding objects", "Increase screen brightness", "Print maps"],
     1, "Sensors help the car detect lanes, obstacles, and other road users.", "Real-world application"),

    ("Which is a performance measure for a vacuum-cleaning agent?",
     ["Amount of dust removed", "Colour of the vacuum", "Brand of the battery", "Size of its packaging"],
     0, "The performance measure evaluates how well the agent cleans.", "Scenario-based"),

    ("Which environment is fully observable?",
     ["An environment where all relevant state information is available", "An environment with no information", "An environment that changes randomly only", "An environment with no states"],
     0, "In a fully observable environment, the agent can access all relevant information about the state.", "MCQ"),

    ("A chess-playing AI usually operates in a:",
     ["Single-agent environment only", "Multi-agent environment", "Environment without actions", "Environment without states"],
     1, "Chess involves two competing agents: the players.", "Real-world application"),

    ("A changing traffic environment is best described as:",
     ["Static", "Dynamic", "Empty", "Fully predictable in every situation"],
     1, "Traffic changes while the driving agent is operating.", "Scenario-based"),

    ("An environment in which the next state is completely determined by the current state and action is:",
     ["Stochastic", "Deterministic", "Partially observable", "Unknown"],
     1, "In a deterministic environment, the current state and action determine the next state.", "MCQ"),

    ("Which is an example of an AI recommendation system?",
     ["A streaming platform suggesting movies", "A plain wall clock", "An empty folder", "A paper notebook"],
     0, "Recommendation systems suggest content based on user data and preferences.", "Real-world application"),

    ("Which is an example of a problem-solving agent?",
     ["A route-planning system finding a path to a destination", "A keyboard with no software", "A blank screen", "A disconnected cable"],
     0, "A route planner searches for a sequence of actions leading to a destination.", "Real-world application"),

    ("Which is NOT a basic component of problem formulation?",
     ["Initial state", "Successor function", "Goal test", "Monitor wallpaper"],
     3, "Problem formulation includes the initial state, actions/successor function, goal test, and path cost.", "MCQ"),

    ("The state from which a search problem begins is called the:",
     ["Goal state", "Initial state", "Final cost", "Heuristic state"],
     1, "The initial state is the starting point of the problem.", "Fill in the blank"),

    ("The goal test determines whether:",
     ["The current state satisfies the goal", "The computer is switched on", "The search has a colourful interface", "The file is saved"],
     0, "The goal test checks whether a state meets the objective.", "MCQ"),

    ("Path cost represents:",
     ["The cost of a path from the initial state", "The colour of a node", "The size of the monitor", "The number of files on a computer"],
     0, "Path cost measures the total cost of the actions along a path.", "MCQ"),

    ("An optimal solution is a solution with:",
     ["The lowest path cost among solutions", "The largest number of steps", "No goal state", "The most branches"],
     0, "An optimal solution has the minimum path cost.", "MCQ"),

    ("The collection of possible states and transitions in a problem is called the:",
     ["State space", "Operating system", "Data type", "Memory card"],
     0, "The state space represents possible states and transitions.", "Fill in the blank"),

    ("A production system commonly consists of:",
     ["Production rules, working memory, and a control strategy", "Only a monitor and keyboard", "Only a database table", "Only a network cable"],
     0, "These are common components of a production system.", "MCQ"),

    ("In a search tree, a node generally represents:",
     ["A state in the search process", "Only the computer screen", "A printer setting", "A programming language"],
     0, "Nodes represent states reached during search.", "MCQ"),

    ("Breadth-First Search (BFS) explores nodes:",
     ["Level by level", "Only at the deepest level", "In random order only", "Without visiting nodes"],
     0, "BFS explores all nodes at one depth before moving deeper.", "Search problem"),

    ("Depth-First Search (DFS) explores:",
     ["A branch deeply before backtracking", "All levels simultaneously", "Only the initial node", "Only the goal node"],
     0, "DFS follows a branch as deeply as possible before backtracking.", "Search problem"),

    ("Which data structure is commonly used by BFS?",
     ["Queue", "Stack only", "Spreadsheet", "Image file"],
     0, "BFS commonly uses a FIFO queue.", "Search problem"),

    ("Which data structure is commonly associated with iterative DFS?",
     ["Stack", "Queue only", "Printer buffer", "Audio file"],
     0, "DFS can be implemented using a stack or recursion.", "Search problem"),

    ("Iterative Deepening Search repeatedly:",
     ["Runs depth-limited search with increasing limits", "Removes the goal state", "Uses no depth limit at all", "Stops before searching"],
     0, "The depth limit increases in successive iterations.", "Search problem"),

    ("If the shallowest goal is at depth 2, BFS explores nodes in which order?",
     ["Depth 0, then depth 1, then depth 2", "Depth 2 before depth 0", "Deepest nodes first", "Random depth order"],
     0, "BFS searches level by level, so shallower levels are explored first.", "Problem-solving"),

    ("A search algorithm that uses no heuristic information is called:",
     ["Uninformed search", "Informed search", "Neural search only", "Image search"],
     0, "Uninformed search does not use extra heuristic knowledge about the goal.", "MCQ"),

    ("A heuristic function h(n) estimates:",
     ["The cost or distance from a node to the goal", "The colour of a node", "The computer's battery level", "The number of users online"],
     0, "A heuristic estimates how close a state is to the goal.", "MCQ"),

    ("Best-First Search selects the next node using:",
     ["An evaluation of how promising the node is", "Alphabetical order only", "The screen size", "The file name only"],
     0, "Best-First Search expands a node considered most promising according to its evaluation.", "Search problem"),

    ("Greedy Best-First Search commonly evaluates a node using:",
     ["h(n)", "Only the depth of the node", "Only the file size", "The number of letters in its name"],
     0, "Greedy Best-First Search uses the heuristic estimate h(n).", "Search problem"),

    ("In A* search, the evaluation function is:",
     ["f(n) = g(n) + h(n)", "f(n) = g(n) - h(n)", "f(n) = g(n) × h(n)", "f(n) = g(n) only"],
     0, "A* combines the cost so far g(n) with the estimated remaining cost h(n).", "Search problem"),

    ("Hill Climbing chooses a move based mainly on:",
     ["Improving the current state's evaluation", "Always returning to the initial state", "Ignoring neighbouring states", "Selecting a random file"],
     0, "Hill Climbing moves toward a neighbouring state with a better evaluation.", "Search problem"),

    ("A common problem with Hill Climbing is:",
     ["Getting stuck at a local maximum", "Always finding every possible solution", "Never examining a neighbour", "Requiring no evaluation"],
     0, "Local maxima can prevent Hill Climbing from reaching the global optimum.", "MCQ"),

    ("A Constraint Satisfaction Problem (CSP) consists of:",
     ["Variables, domains, and constraints", "Only images and videos", "Only a goal test", "Only a queue"],
     0, "CSPs are defined by variables, their domains, and constraints on assignments.", "MCQ"),

    ("Which is a real-world example of a CSP?",
     ["Creating a timetable without time clashes", "Changing wallpaper", "Opening a music player", "Taking a screenshot"],
     0, "Timetabling involves variables, possible time slots, and constraints.", "Real-world application"),

    ("Means-End Analysis works by:",
     ["Comparing the current state with the goal and reducing the difference", "Ignoring the goal", "Choosing actions without considering results", "Removing all states"],
     0, "Means-End Analysis identifies differences and selects actions to reduce them.", "MCQ"),

    ("A medical diagnosis system can use AI to:",
     ["Analyse symptoms and support diagnosis", "Guarantee every diagnosis without error", "Replace all medical evidence", "Work without any input"],
     0, "AI can help analyse patient information and support clinical decisions.", "Real-world application"),

    ("A bank's fraud-detection AI may identify:",
     ["Unusual transaction patterns", "Only the colour of banknotes", "The user's screen size", "The number of keyboard keys"],
     0, "Fraud detection systems look for suspicious patterns in transactions.", "Real-world application"),

    ("An email spam filter is an example of AI used for:",
     ["Classifying messages", "Driving a vehicle", "Controlling room temperature only", "Creating a state-space tree manually"],
     0, "Spam filters classify messages as spam or legitimate.", "Real-world application"),

    ("An online shopping website recommending products is using AI for:",
     ["Personalised recommendations", "Disk partitioning", "Screen calibration", "Cable management"],
     0, "Recommendation systems use information about users and products to suggest items.", "Real-world application"),

    ("Assertion: BFS explores nodes level by level. Reason: BFS commonly uses a FIFO queue.",
     ["Both are true, and the reason explains the assertion", "Both are true, but the reason does not explain the assertion", "Assertion is true, reason is false", "Assertion is false, reason is true"],
     0, "A FIFO queue processes earlier-added, shallower nodes first in standard BFS.", "Assertion–Reason"),

    ("Assertion: A* uses both the path cost so far and a heuristic estimate. Reason: Its evaluation is f(n) = g(n) + h(n).",
     ["Both are true, and the reason explains the assertion", "Both are true, but the reason does not explain the assertion", "Assertion is true, reason is false", "Assertion is false, reason is true"],
     0, "A* adds the cost already incurred to the estimated remaining cost.", "Assertion–Reason"),

    ("Match the following: BFS, DFS, and CSP.",
     ["BFS–level order; DFS–deep branch first; CSP–variables and constraints",
      "BFS–deep branch first; DFS–level order; CSP–only path costs",
      "BFS–heuristic only; DFS–no states; CSP–only sensors",
      "BFS–random order; DFS–goal test; CSP–only actuators"],
     0, "BFS explores levels, DFS explores deeply before backtracking, and CSPs use variables, domains, and constraints.", "Match the following"),

    ("A delivery robot must find a route while considering distance already travelled and estimated distance remaining. Which algorithm fits this description?",
     ["A* Search", "Random guessing", "Simple file sorting", "Image cropping"],
     0, "A* combines g(n), the cost so far, and h(n), the estimated remaining cost.", "Scenario-based"),

    ("A robot has several possible next moves and always chooses the neighbour that looks best immediately. Which method is it using?",
     ["Hill Climbing", "Breadth-First Search", "Iterative Deepening", "Constraint Satisfaction"],
     0, "Hill Climbing repeatedly selects an improving neighbouring state.", "Scenario-based"),
]

# -------------------- SESSION STATE --------------------

if "order" not in st.session_state:
    st.session_state.order = list(range(len(QUESTIONS)))
    random.shuffle(st.session_state.order)
    st.session_state.current = 0
    st.session_state.answers = {}
    st.session_state.submitted = {}
    st.session_state.started = False

def restart_quiz():
    st.session_state.order = list(range(len(QUESTIONS)))
    random.shuffle(st.session_state.order)
    st.session_state.current = 0
    st.session_state.answers = {}
    st.session_state.submitted = {}
    st.session_state.started = False

# -------------------- APP HEADER --------------------

st.title("🧠 AI Interactive Quiz Game")
st.subheader("Units I & II | Foundations and Search Techniques")
st.write(
    "Test your understanding of Artificial Intelligence, intelligent agents, "
    "problem formulation, state-space search, and heuristic methods."
)

st.info("50 questions • Random order • Instant feedback • Final score")

if not st.session_state.started:
    st.markdown("### Ready to test your AI knowledge?")
    st.write("Choose an answer for each question and submit it to see feedback.")
    if st.button("🚀 Start Quiz", type="primary", use_container_width=True):
        st.session_state.started = True
        st.rerun()
    st.stop()

# -------------------- QUIZ --------------------

total = len(st.session_state.order)
current = st.session_state.current

if current >= total:
    score = sum(st.session_state.answers.values())
    percentage = score / total * 100

    st.success("🎉 Quiz completed!")
    st.metric("Your Score", f"{score} / {total}")
    st.metric("Percentage", f"{percentage:.1f}%")
    st.progress(percentage / 100)

    if percentage >= 80:
        st.balloons()
        st.write("Excellent work! You have a strong understanding of these topics.")
    elif percentage >= 50:
        st.write("Good effort! Revise the explanations and try again.")
    else:
        st.write("Keep practising. Review the concepts and attempt the quiz again.")

    with st.expander("Review your answers"):
        for position, question_index in enumerate(st.session_state.order):
            q, options, correct, explanation, qtype = QUESTIONS[question_index]
            user_correct = st.session_state.answers.get(position, False)
            chosen = st.session_state.submitted.get(position, None)

            st.markdown(f"**Question {position + 1}: {q}**")
            if chosen is not None:
                st.write(f"Your answer: {options[chosen]}")
            st.write(f"Correct answer: {options[correct]}")
            st.caption(explanation)
            st.divider()

    if st.button("🔄 Restart Quiz", type="primary"):
        restart_quiz()
        st.rerun()
    st.stop()

question_index = st.session_state.order[current]
question, options, correct_index, explanation, qtype = QUESTIONS[question_index]

st.progress(current / total)
st.caption(f"Question {current + 1} of {total}  |  Type: {qtype}")

st.markdown(f"### {question}")

if current not in st.session_state.submitted:
    selected = st.radio(
        "Choose your answer:",
        options,
        index=None,
        key=f"choice_{current}"
    )

    if st.button("Submit Answer", type="primary", use_container_width=True):
        if selected is None:
            st.warning("Please select an answer first.")
        else:
            selected_index = options.index(selected)
            st.session_state.submitted[current] = selected_index
            st.session_state.answers[current] = (
                selected_index == correct_index
            )
            st.rerun()
else:
    selected_index = st.session_state.submitted[current]

    if selected_index == correct_index:
        st.success("✅ Correct answer!")
    else:
        st.error("❌ Incorrect answer.")

    st.write(f"**Your answer:** {options[selected_index]}")
    st.write(f"**Correct answer:** {options[correct_index]}")
    st.info(f"💡 Explanation: {explanation}")

    score_so_far = sum(st.session_state.answers.values())
    st.metric("Score so far", f"{score_so_far} / {current + 1}")

    if st.button("Next Question ➡️", type="primary", use_container_width=True):
        st.session_state.current += 1
        st.rerun()

st.caption("AI Interactive Quiz Game | Academic Assignment")
