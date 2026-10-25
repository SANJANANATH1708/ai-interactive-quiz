
import streamlit as st
import random

st.set_page_config(
    page_title="AI Interactive Quiz Game",
    page_icon="🧠",
    layout="centered"
)

QUESTIONS = [
    # UNIT I: FOUNDATIONS OF AI

    {
        "q": "Who introduced the term Artificial Intelligence?",
        "type": "MCQ",
        "options": ["Alan Turing", "John McCarthy", "Charles Babbage", "Bill Gates"],
        "answer": 1,
        "explanation": "John McCarthy introduced the term Artificial Intelligence."
    },
    {
        "q": "Artificial Intelligence mainly aims to create machines that can:",
        "type": "MCQ",
        "options": ["Only store files", "Perform tasks requiring intelligence",
                    "Only calculate sums", "Replace computer hardware"],
        "answer": 1,
        "explanation": "AI enables machines to perform tasks that normally require human intelligence."
    },
    {
        "q": "The Turing Test was proposed by:",
        "type": "MCQ",
        "options": ["John McCarthy", "Alan Turing", "Herbert Simon", "Marvin Minsky"],
        "answer": 1,
        "explanation": "Alan Turing proposed the test to evaluate machine behaviour."
    },
    {
        "q": "True or False: AI systems can be designed to learn from data.",
        "type": "True/False",
        "options": ["True", "False"],
        "answer": 0,
        "explanation": "Machine learning allows AI systems to learn patterns from data."
    },
    {
        "q": "The branch of AI that enables computers to understand human language is:",
        "type": "MCQ",
        "options": ["Disk formatting", "Natural Language Processing",
                    "File compression", "Screen resolution"],
        "answer": 1,
        "explanation": "Natural Language Processing deals with human language."
    },
    {
        "q": "An AI recommendation system is used by:",
        "type": "Real-world application",
        "options": ["A streaming platform suggesting movies",
                    "A plain wall clock", "An empty folder", "A paper notebook"],
        "answer": 0,
        "explanation": "Recommendation systems suggest content based on preferences and behaviour."
    },
    {
        "q": "A bank's fraud-detection AI may identify:",
        "type": "Real-world application",
        "options": ["Unusual transaction patterns", "Only banknote colours",
                    "The user's screen size", "The number of keyboard keys"],
        "answer": 0,
        "explanation": "AI can detect unusual patterns that may indicate fraudulent transactions."
    },
    {
        "q": "An email spam filter uses AI for:",
        "type": "Real-world application",
        "options": ["Classifying messages", "Driving a vehicle",
                    "Controlling room temperature only", "Creating a search tree manually"],
        "answer": 0,
        "explanation": "Spam filters classify messages as spam or legitimate."
    },
    {
        "q": "A medical diagnosis system can use AI to:",
        "type": "Real-world application",
        "options": ["Analyse symptoms and support diagnosis",
                    "Guarantee every diagnosis without error",
                    "Replace all medical evidence", "Work without any input"],
        "answer": 0,
        "explanation": "AI can assist healthcare professionals by analysing medical information."
    },
    {
        "q": "A self-driving car uses sensors mainly to:",
        "type": "Real-world application",
        "options": ["Decorate the dashboard",
                    "Perceive roads and surrounding objects",
                    "Increase screen brightness", "Print maps"],
        "answer": 1,
        "explanation": "Sensors help the car perceive its environment."
    },
    {
        "q": "An online shopping website recommending products uses AI for:",
        "type": "Real-world application",
        "options": ["Personalised recommendations", "Disk partitioning",
                    "Screen calibration", "Cable management"],
        "answer": 0,
        "explanation": "Recommendation systems personalise products for users."
    },
    {
        "q": "Which is an example of AI in education?",
        "type": "Real-world application",
        "options": ["A system adapting questions to a student's progress",
                    "A blank notebook", "A manual stapler", "A plain ruler"],
        "answer": 0,
        "explanation": "Adaptive learning systems can adjust learning material to student performance."
    },
    {
        "q": "A voice assistant understanding spoken commands uses:",
        "type": "Real-world application",
        "options": ["Natural Language Processing", "Disk formatting",
                    "File compression", "Screen resolution"],
        "answer": 0,
        "explanation": "Language processing helps systems interpret spoken commands."
    },
    {
        "q": "A rational agent chooses an action expected to:",
        "type": "MCQ",
        "options": ["Maximise its performance measure", "Use the most memory",
                    "Take the longest time", "Ignore its environment"],
        "answer": 0,
        "explanation": "A rational agent selects actions expected to maximise its performance measure."
    },
    {
        "q": "The information an agent receives from its environment at a particular time is called a:",
        "type": "Fill in the blank",
        "answer": "percept",
        "explanation": "A percept is the information an agent receives through its sensors."
    },
    {
        "q": "An agent perceives its environment through ______ and acts through effectors.",
        "type": "Fill in the blank",
        "answer": "sensors",
        "explanation": "Sensors receive information and effectors carry out actions."
    },
    {
        "q": "The goal test determines whether:",
        "type": "MCQ",
        "options": ["The current state satisfies the goal",
                    "The computer is switched on",
                    "The search has a colourful interface",
                    "The file is saved"],
        "answer": 0,
        "explanation": "The goal test checks whether a state meets the goal condition."
    },
    {
        "q": "True or False: An agent's performance measure helps evaluate its success.",
        "type": "True/False",
        "options": ["True", "False"],
        "answer": 0,
        "explanation": "The performance measure specifies how the agent's success is evaluated."
    },
    {
        "q": "Which is a performance measure for a vacuum-cleaning agent?",
        "type": "Scenario/Application",
        "options": ["Amount of dust removed", "Colour of the vacuum",
                    "Brand of the battery", "Size of its packaging"],
        "answer": 0,
        "explanation": "The amount of dirt removed is relevant to the agent's cleaning performance."
    },
    {
        "q": "An environment in which the next state is completely determined by the current state and action is:",
        "type": "MCQ",
        "options": ["Stochastic", "Deterministic", "Partially observable", "Unknown"],
        "answer": 1,
        "explanation": "In a deterministic environment, the current state and action determine the next state."
    },
    {
        "q": "True or False: A partially observable environment gives an agent complete information about its state.",
        "type": "True/False",
        "options": ["True", "False"],
        "answer": 1,
        "explanation": "A partially observable environment does not provide complete state information."
    },
    {
        "q": "A robot vacuum cannot detect dirt in every corner of a room. This is an example of:",
        "type": "Scenario/Application",
        "options": ["A partially observable environment",
                    "A fully observable environment", "A programming language", "A goal test"],
        "answer": 0,
        "explanation": "The vacuum does not have complete information about its environment."
    },
    {
        "q": "Match the following: Sensors, Effectors, Percept.",
        "type": "Match the following",
        "options": [
            "Sensors–receive information; Effectors–perform actions; Percept–information received",
            "Sensors–perform actions; Effectors–receive information; Percept–path cost",
            "Sensors–goal test; Effectors–heuristic; Percept–initial state",
            "Sensors–path cost; Effectors–goal state; Percept–queue"
        ],
        "answer": 0,
        "explanation": "Sensors perceive, effectors act, and a percept is the information received."
    },
    {
        "q": "A chatbot answers customer questions based on the text it receives. Its text input is an example of:",
        "type": "Scenario/Application",
        "options": ["A percept", "A path cost", "A state-space tree", "A depth limit"],
        "answer": 0,
        "explanation": "The text received by the chatbot is a percept."
    },
    {
        "q": "Which statement best describes an intelligent agent?",
        "type": "MCQ",
        "options": ["It perceives its environment and takes actions",
                    "It only stores information", "It never uses sensors",
                    "It always follows random actions"],
        "answer": 0,
        "explanation": "An intelligent agent perceives its environment and acts to achieve objectives."
    },

    # UNIT I: PROBLEM FORMULATION

    {
        "q": "The state from which a search problem begins is called the:",
        "type": "MCQ",
        "options": ["Goal state", "Initial state", "Final cost", "Heuristic state"],
        "answer": 1,
        "explanation": "The initial state is the starting point of a search problem."
    },
    {
        "q": "The collection of possible states and transitions in a problem is called the:",
        "type": "Fill in the blank",
        "answer": "state space",
        "explanation": "The state space contains the possible states and their transitions."
    },
    {
        "q": "Which is NOT a basic component of problem formulation?",
        "type": "MCQ",
        "options": ["Initial state", "Successor function", "Goal test", "Monitor wallpaper"],
        "answer": 3,
        "explanation": "Problem formulation includes an initial state, actions or successor function, goal test and path cost."
    },
    {
        "q": "An optimal solution is a solution with:",
        "type": "MCQ",
        "options": ["The lowest path cost among solutions",
                    "The largest number of steps", "No goal state", "The most branches"],
        "answer": 0,
        "explanation": "An optimal solution has the minimum path cost among valid solutions."
    },
    {
        "q": "A delivery robot must travel from a warehouse to a customer's home. The warehouse is the:",
        "type": "Problem-solving",
        "options": ["Initial state", "Goal test", "Heuristic value", "Final cost"],
        "answer": 0,
        "explanation": "The warehouse is the starting state of the delivery problem."
    },
    {
        "q": "A delivery robot has two valid routes. Route A costs 12 units and Route B costs 8 units. Which is cheaper?",
        "type": "Problem-solving",
        "options": ["Route A", "Route B", "Both cost the same", "Neither route"],
        "answer": 1,
        "explanation": "Route B has the lower cost: 8 units compared with 12."
    },
    {
        "q": "A problem-solving agent needs to know whether it has reached its destination. Which component checks this?",
        "type": "Scenario/Application",
        "options": ["Goal test", "Sensor colour", "Memory size", "Production rule name"],
        "answer": 0,
        "explanation": "The goal test checks whether the destination or goal condition has been reached."
    },
    {
        "q": "A production system commonly consists of:",
        "type": "MCQ",
        "options": ["Production rules, working memory and a control strategy",
                    "Only images and videos", "Only a keyboard", "Only a goal state"],
        "answer": 0,
        "explanation": "Production systems use rules, working memory and a control strategy."
    },
    {
        "q": "True or False: A state-space search explores states to find a path to a goal.",
        "type": "True/False",
        "options": ["True", "False"],
        "answer": 0,
        "explanation": "Search algorithms explore possible states to find a solution."
    },
    {
        "q": "Match the following: Initial state, Goal test, Path cost.",
        "type": "Match the following",
        "options": [
            "Initial state–starting point; Goal test–checks goal; Path cost–cost of a path",
            "Initial state–final answer; Goal test–queue; Path cost–sensor",
            "Initial state–heuristic; Goal test–screen; Path cost–effectors",
            "Initial state–random node; Goal test–file; Path cost–keyboard"
        ],
        "answer": 0,
        "explanation": "These are the standard meanings of the three problem-formulation components."
    },

    # UNIT II: SEARCH ALGORITHMS

    {
        "q": "Which data structure is commonly used by BFS?",
        "type": "Search problem",
        "options": ["Queue", "Stack only", "Spreadsheet", "Image file"],
        "answer": 0,
        "explanation": "Breadth-First Search commonly uses a FIFO queue."
    },
    {
        "q": "Depth-First Search commonly uses a:",
        "type": "MCQ",
        "options": ["Stack", "Queue only", "Spreadsheet", "Hash of images"],
        "answer": 0,
        "explanation": "DFS uses a stack or recursion to explore a branch deeply."
    },
    {
        "q": "Breadth-First Search explores nodes:",
        "type": "MCQ",
        "options": ["Level by level", "Only at maximum depth",
                    "In random order", "Only using heuristic values"],
        "answer": 0,
        "explanation": "BFS explores all nodes at one depth before moving to the next."
    },
    {
        "q": "Depth-First Search explores:",
        "type": "MCQ",
        "options": ["One branch deeply before backtracking",
                    "All nodes level by level", "Only the cheapest path", "No states"],
        "answer": 0,
        "explanation": "DFS follows a branch as far as possible before backtracking."
    },
    {
        "q": "Match the following: BFS, DFS, and CSP.",
        "type": "Match the following",
        "options": [
            "BFS–level order; DFS–deep branch first; CSP–variables and constraints",
            "BFS–deep branch first; DFS–level order; CSP–only path costs",
            "BFS–heuristic only; DFS–no states; CSP–only sensors",
            "BFS–random order; DFS–goal test; CSP–only actuators"
        ],
        "answer": 0,
        "explanation": "BFS explores by levels, DFS explores deeply, and CSP uses variables, domains and constraints."
    },
    {
        "q": "Iterative Deepening Search repeatedly:",
        "type": "Search problem",
        "options": ["Runs depth-limited search with increasing limits",
                    "Removes the goal state", "Uses no depth limit at all",
                    "Stops before searching"],
        "answer": 0,
        "explanation": "It increases the depth limit after each depth-limited search."
    },
    {
        "q": "A search algorithm that uses no heuristic information is called:",
        "type": "MCQ",
        "options": ["Uninformed search", "Informed search",
                    "Neural search only", "Image search"],
        "answer": 0,
        "explanation": "Uninformed search does not use heuristic guidance."
    },
    {
        "q": "A heuristic function h(n) estimates:",
        "type": "MCQ",
        "options": ["The cost or distance from a node to the goal",
                    "The colour of a node", "The computer's battery level",
                    "The number of users online"],
        "answer": 0,
        "explanation": "h(n) estimates the remaining cost from node n to the goal."
    },
    {
        "q": "Best-First Search selects the next node using:",
        "type": "Search problem",
        "options": ["An evaluation of how promising the node is",
                    "Alphabetical order only", "The screen size", "The file name only"],
        "answer": 0,
        "explanation": "Best-First Search expands the node that appears most promising according to its evaluation."
    },
    {
        "q": "A delivery robot considers the path cost so far and the estimated distance remaining. Which algorithm fits this description?",
        "type": "Problem-solving",
        "options": ["A* Search", "Random guessing", "Simple file sorting", "Disk formatting"],
        "answer": 0,
        "explanation": "A* uses f(n) = g(n) + h(n), combining path cost and heuristic estimate."
    },
    {
        "q": "A* Search evaluates a node using:",
        "type": "MCQ",
        "options": ["f(n) = g(n) + h(n)", "f(n) = g(n) - h(n)",
                    "f(n) = g(n) × h(n)", "f(n) = g(n) only"],
        "answer": 0,
        "explanation": "A* adds the cost already travelled, g(n), to the estimated remaining cost, h(n)."
    },
    {
        "q": "Assertion: A* uses the path cost so far and a heuristic estimate. Reason: Its evaluation is f(n) = g(n) + h(n).",
        "type": "Assertion–Reason",
        "options": [
            "Both are true, and the reason explains the assertion",
            "Both are true, but the reason does not explain the assertion",
            "Assertion is true, reason is false",
            "Assertion is false, reason is true"
        ],
        "answer": 0,
        "explanation": "The A* evaluation function adds g(n) and h(n)."
    },
    {
        "q": "Hill Climbing chooses a move based mainly on:",
        "type": "Search problem",
        "options": ["Improving the current state's evaluation",
                    "Always returning to the initial state",
                    "Ignoring neighbouring states", "Selecting a random file"],
        "answer": 0,
        "explanation": "Hill Climbing moves to a neighbouring state with a better evaluation."
    },
    {
        "q": "A possible limitation of Hill Climbing is getting stuck at a:",
        "type": "MCQ",
        "options": ["Local maximum", "Keyboard", "File extension", "Screen resolution"],
        "answer": 0,
        "explanation": "A local maximum can prevent Hill Climbing from reaching the global optimum."
    },
    {
        "q": "A Constraint Satisfaction Problem (CSP) consists of:",
        "type": "MCQ",
        "options": ["Variables, domains, and constraints",
                    "Only images and videos", "Only a goal test", "Only a queue"],
        "answer": 0,
        "explanation": "CSPs are defined using variables, their possible domains and constraints."
    },
    {
        "q": "Which is a real-world example of a CSP?",
        "type": "Real-world application",
        "options": ["Creating a timetable without time clashes",
                    "Changing wallpaper", "Opening a music player", "Taking a screenshot"],
        "answer": 0,
        "explanation": "Timetabling assigns classes to slots while satisfying constraints."
    },
    {
        "q": "A university must schedule exams so that students do not have overlapping exams. This is an example of:",
        "type": "Scenario/Application",
        "options": ["Constraint Satisfaction Problem",
                    "Image compression", "Random search only", "Disk formatting"],
        "answer": 0,
        "explanation": "Exam scheduling is a CSP because time-slot assignments must satisfy constraints."
    },
    {
        "q": "A search tree has a root node with two children. Each child has two children. How many nodes are there up to depth 2, including the root?",
        "type": "Problem-solving",
        "options": ["5", "6", "7", "8"],
        "answer": 2,
        "explanation": "There are 1 root + 2 nodes at depth 1 + 4 nodes at depth 2 = 7."
    },
    {
        "q": "A search tree has branching factor 3. How many children does each fully expanded node generate?",
        "type": "Problem-solving",
        "options": ["1", "2", "3", "6"],
        "answer": 2,
        "explanation": "The branching factor is the number of successors generated per node."
    },
    {
        "q": "Which search method uses a heuristic to guide exploration toward a goal?",
        "type": "MCQ",
        "options": ["Informed search", "Uninformed search only",
                    "Random file search", "Linear file deletion"],
        "answer": 0,
        "explanation": "Informed search uses additional knowledge, such as a heuristic."
    },
    {
        "q": "A* selects a node with g(n) = 4 and h(n) = 6. What is f(n)?",
        "type": "Problem-solving",
        "options": ["2", "10", "24", "46"],
        "answer": 1,
        "explanation": "f(n) = g(n) + h(n) = 4 + 6 = 10."
    },
    {
        "q": "A route-finding problem has path costs 5, 7 and 9 for three complete routes. Which route is optimal?",
        "type": "Problem-solving",
        "options": ["Cost 5", "Cost 7", "Cost 9", "All are equally optimal"],
        "answer": 0,
        "explanation": "The route with cost 5 has the lowest path cost."
    },
    {
        "q": "Means-End Analysis works by:",
        "type": "MCQ",
        "options": ["Comparing the current state with the goal and reducing the difference",
                    "Ignoring the goal", "Choosing actions without considering results",
                    "Removing all states"],
        "answer": 0,
        "explanation": "Means-End Analysis identifies differences between the current state and goal and chooses actions to reduce them."
    },
    {
        "q": "A robot must reach a target through connected locations. The locations and connections can be represented as a:",
        "type": "Scenario/Application",
        "options": ["State-space graph", "Wallpaper", "Text font", "File extension"],
        "answer": 0,
        "explanation": "A state-space graph represents states and transitions between them."
    },
    {
        "q": "True or False: BFS always explores the deepest node first.",
        "type": "True/False",
        "options": ["True", "False"],
        "answer": 1,
        "explanation": "DFS explores deeply first; BFS explores level by level."
    },
    {
        "q": "True or False: DFS may use less memory than BFS in a large search tree.",
        "type": "True/False",
        "options": ["True", "False"],
        "answer": 0,
        "explanation": "DFS often stores a path and unexplored alternatives, while BFS stores a potentially large frontier."
    },
    {
        "q": "A* uses g(n) to represent the ______ cost from the start node to n.",
        "type": "Fill in the blank",
        "answer": "path",
        "explanation": "g(n) is the cost accumulated from the initial state to node n."
    },
    {
        "q": "In a CSP, the possible values that a variable can take are called its:",
        "type": "Fill in the blank",
        "answer": "domain",
        "explanation": "A variable's domain is the set of values available to it."
    },
    {
        "q": "Which is a key issue when designing a search program?",
        "type": "MCQ",
        "options": ["Avoiding repeated states and managing the search efficiently",
                    "Choosing a colourful wallpaper", "Changing the keyboard layout",
                    "Increasing the font size"],
        "answer": 0,
        "explanation": "Search design must consider efficiency, repeated states, memory and solution quality."
    },
    {
        "q": "A maze-solving program explores one corridor until it reaches a dead end, then returns to try another. Which search strategy does this resemble?",
        "type": "Scenario/Application",
        "options": ["Depth-First Search", "Breadth-First Search",
                    "Only A* Search", "Random file sorting"],
        "answer": 0,
        "explanation": "DFS follows a branch deeply and backtracks when necessary."
    },
    {
        "q": "Match the following: BFS, DFS, Iterative Deepening.",
        "type": "Match the following",
        "options": [
            "BFS–level by level; DFS–deep branch; Iterative Deepening–increasing depth limits",
            "BFS–heuristic only; DFS–level by level; Iterative Deepening–no limits",
            "BFS–random guessing; DFS–queue only; Iterative Deepening–no search",
            "BFS–goal test; DFS–path cost; Iterative Deepening–sensors"
        ],
        "answer": 0,
        "explanation": "These descriptions distinguish the three search strategies."
    },
    {
        "q": "A route planner needs the shortest path in a graph where every edge has the same cost. Which search method is suitable?",
        "type": "Problem-solving",
        "options": ["Breadth-First Search", "Depth-First Search",
                    "Hill Climbing only", "Random guessing"],
        "answer": 0,
        "explanation": "BFS finds a shortest path in an unweighted graph when each edge has equal cost."
    },
    {
        "q": "A heuristic estimates a distance of 3 from one node and 8 from another to the same goal. If the search chooses the smaller estimate, which node is preferred by Greedy Best-First Search?",
        "type": "Problem-solving",
        "options": ["The node with h(n) = 3", "The node with h(n) = 8",
                    "Both must be ignored", "A random node only"],
        "answer": 0,
        "explanation": "Greedy Best-First Search prefers the node with the lower heuristic estimate."
    },
    {
        "q": "An AI game agent evaluates possible moves and selects the move that improves its position. This is an example of:",
        "type": "Scenario/Application",
        "options": ["Search and decision-making", "File compression",
                    "Screen calibration", "Disk partitioning"],
        "answer": 0,
        "explanation": "The agent evaluates possible states and chooses an action based on the evaluation."
    },
    {
        "q": "A robot is at state S and can move to A or B. A costs 3 units and B costs 6 units. If both reach the goal directly, which path has the lower cost?",
        "type": "Problem-solving",
        "options": ["S to A to goal", "S to B to goal",
                    "Both have equal cost", "There is no solution"],
        "answer": 0,
        "explanation": "The route through A costs less when its total cost is 3 rather than 6."
    },
    {
        "q": "Which statement about an optimal solution is correct?",
        "type": "MCQ",
        "options": ["It has the lowest cost among valid solutions",
                    "It always contains the most steps",
                    "It never reaches the goal", "It is always found by random guessing"],
        "answer": 0,
        "explanation": "Optimality concerns solution cost, not the number of steps alone."
    }
]


# NORMALISE AND SHUFFLE QUESTIONS

if "quiz_order" not in st.session_state:
    st.session_state.quiz_order = random.sample(
        range(len(QUESTIONS)), len(QUESTIONS)
    )
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.answers = {}
    st.session_state.submitted = False
    st.session_state.started = False


def restart_quiz():
    st.session_state.quiz_order = random.sample(
        range(len(QUESTIONS)), len(QUESTIONS)
    )
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.answers = {}
    st.session_state.submitted = False
    st.session_state.started = False


def check_answer(question, selected):
    if question["type"] == "Fill in the blank":
        return selected.strip().lower() == question["answer"].strip().lower()
    return selected == question["answer"]


def submit_answer():
    idx = st.session_state.current
    question = QUESTIONS[st.session_state.quiz_order[idx]]
    selected = st.session_state.get(f"answer_{idx}")

    if selected is None or str(selected).strip() == "":
        st.warning("Please choose or enter an answer before submitting.")
        return

    is_correct = check_answer(question, selected)
    st.session_state.answers[idx] = {
        "selected": selected,
        "correct": is_correct
    }

    if is_correct:
        st.session_state.score += 1

    st.session_state.submitted = True


# PAGE DESIGN

st.title("🧠 AI Interactive Quiz Game")
st.subheader("Units I & II | Foundations and Search Techniques")

st.write(
    "Test your understanding of Artificial Intelligence, intelligent agents, "
    "problem formulation, state-space search, and heuristic methods."
)

st.info(
    f"{len(QUESTIONS)} questions • Random order • Instant feedback • Final score"
)

if not st.session_state.started:
    st.markdown("### Ready to test your AI knowledge?")
    st.write("The quiz includes multiple question formats and real-world scenarios.")
    st.write("Each correct answer earns 1 mark.")
    if st.button("🚀 Start Quiz", use_container_width=True):
        st.session_state.started = True
        st.rerun()

elif st.session_state.current < len(QUESTIONS):

    idx = st.session_state.current
    question = QUESTIONS[st.session_state.quiz_order[idx]]

    st.progress((idx + 1) / len(QUESTIONS))
    st.caption(
        f"Question {idx + 1} of {len(QUESTIONS)} | Type: {question['type']}"
    )
    st.markdown(f"### {question['q']}")
    st.write("**Choose your answer:**")

    if question["type"] == "Fill in the blank":
        st.text_input(
            "Enter your answer",
            key=f"answer_{idx}",
            disabled=st.session_state.submitted
        )
    else:
        st.radio(
            "Options",
            question["options"],
            index=None,
            key=f"answer_{idx}",
            disabled=st.session_state.submitted,
            label_visibility="collapsed"
        )

    if not st.session_state.submitted:
        if st.button("Submit Answer", use_container_width=True):
            selected = st.session_state.get(f"answer_{idx}")

            if selected is None or str(selected).strip() == "":
                st.warning("Please choose or enter an answer first.")
            else:
                is_correct = check_answer(question, selected)
                st.session_state.answers[idx] = {
                    "selected": selected,
                    "correct": is_correct
                }

                if is_correct:
                    st.session_state.score += 1

                st.session_state.submitted = True
                st.rerun()

    else:
        result = st.session_state.answers[idx]

        if result["correct"]:
            st.success("✅ Correct answer!")
        else:
            st.error("❌ Incorrect answer.")

            if question["type"] == "Fill in the blank":
                correct_answer = question["answer"]
            else:
                correct_answer = question["options"][question["answer"]]

            st.info(f"**Correct answer:** {correct_answer}")

        st.write(f"**Explanation:** {question['explanation']}")
        st.write(f"**Current score:** {st.session_state.score}")

        if idx + 1 < len(QUESTIONS):
            if st.button("Next Question ➡️", use_container_width=True):
                st.session_state.current += 1
                st.session_state.submitted = False
                st.rerun()
        else:
            if st.button("View Final Results 🏆", use_container_width=True):
                st.session_state.current += 1
                st.rerun()

    st.caption("AI Interactive Quiz Game | Academic Assignment")

else:
    total = len(QUESTIONS)
    score = st.session_state.score
    percentage = (score / total) * 100

    st.balloons()
    st.success("🎉 Quiz completed!")

    st.metric("Your Score", f"{score} / {total}")
    st.metric("Percentage", f"{percentage:.1f}%")
    st.progress(percentage / 100)

    if percentage >= 80:
        st.write("Excellent work! You have a strong understanding of these topics.")
    elif percentage >= 60:
        st.write("Good job! Review the questions you missed to improve further.")
    else:
        st.write("Keep practising! Review the concepts and try again.")

    st.markdown("### Review your answers")

    for i, question_index in enumerate(st.session_state.quiz_order):
        question = QUESTIONS[question_index]
        response = st.session_state.answers.get(i)

        with st.expander(f"Question {i + 1}: {question['q']}"):
            if response:
                st.write(f"**Your answer:** {response['selected']}")
                if question["type"] == "Fill in the blank":
                    correct_answer = question["answer"]
                else:
                    correct_answer = question["options"][question["answer"]]

                st.write(f"**Correct answer:** {correct_answer}")
                st.write(
                    "**Result:** " +
                    ("Correct ✅" if response["correct"] else "Incorrect ❌")
                )
                st.write(f"**Explanation:** {question['explanation']}")

    if st.button("🔄 Restart Quiz", use_container_width=True):
        restart_quiz()
        st.rerun()
