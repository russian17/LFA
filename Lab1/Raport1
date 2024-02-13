# Regular Grammars & Finite Automata
### Course: Formal Languages & Finite Automata
### Author: Cuzmin Simion
----

## Theory
**Automata theory** is the study of abstract computational devices (abstract state machine). An automaton is an abstract model of a digital computer. As such, every automaton includes some essential features. It has a mechanism for reading input. It will be
assumed that the input is a string over a given alphabet. The input mechanism can read theinput string from left to right, one symbol at a time and it can be detected the end of the string. The automaton can produce the output of some form and has a control unit, which
can be in any one of a finite number of internal states, and which can change state in some defined manner based on transition functions.

The finite automata (FA) is characterized by the finite number
of states and it is known the following types of the FA:
- Deterministic finite automata (DFA).
- Nondeterministic finite automata (NFA).
- ε -Nondeterministic finite automata (ε –NFA).

Regular grammars, also known as Type-3 grammars in the Chomsky hierarchy, can be represented by finite automata. Regular grammars have productions of the form A → aB or A → a, where A and B are non-terminal symbols, and a is a terminal symbol.

## Objectives:

1. Discover what a language is and what it needs to have in order to be considered a formal one;
   
2. Provide the initial setup for the evolving project that you will work on during this semester. You can deal with each laboratory work as a separate task or project to demonstrate your understanding of the given themes, but you also can deal with labs as stages of making your own big solution, your own project. Do the following:
    - Create GitHub repository to deal with storing and updating your project;
    - Choose a programming language. Pick one that will be easiest for dealing with your tasks, you need to learn how to solve the problem itself, not everything around the problem (like setting up the project, launching it correctly and etc.);
    - Store reports separately in a way to make verification of your work simpler
   
3. According to your variant number, get the grammar definition and do the following:
    - Implement a type/class for your grammar;
    - Add one function that would generate 5 valid strings from the language expressed by your given grammar;
    - Implement some functionality that would convert and object of type Grammar to one of type Finite Automaton;
    - For the Finite Automaton, please add a method that checks if an input string can be obtained via the state transition from it;

## Implementation description
#### 1. Grammar Class:
  The Grammar class represents a context-free grammar (CFG).
  - Attributes:
    - VN: Set of non-terminal symbols.
    - VT: Set of terminal symbols.
    - P: Production rules, where each non-terminal symbol maps to a list of production rules.
    - S: Start symbol.
  - Methods:
    - generateValidStrings(count): Generates valid strings based on the grammar rules. It recursively generates strings by replacing non-terminals with their corresponding productions until terminal symbols are reached.
    - toFiniteAutomaton(): Converts the grammar to an equivalent finite automaton (FA). It constructs the states, alphabet, transition function, initial state, and set of final states of the FA based on the grammar rules.
#### 2. FiniteAutomaton Class:
  The FiniteAutomaton class represents a finite automaton (FA).
  - Attributes:
    - Q: Set of states.
    - Sigma: Alphabet (set of symbols).
    - Delta: Transition function, which maps a state and a symbol to a set of states.
    - q0: Initial state.
    - F: Set of final states.
  - Methods:
    - stringBelongToLanguage(w): Determines whether a given string w belongs to the language accepted by the automaton. It simulates the state transitions based on the input string and returns True if the final state after processing the string is one of the final states, otherwise returns False.
## Results
![Screenshot 2024-02-12 180258](https://github.com/russian17/LFA/assets/120457811/b03acb4a-ca17-4137-932f-007c634aa112)

## Conclusions
In conclusion, this project has provided an exploration into the realm of formal languages and finite automata. We have delved into the fundamental concepts of automata theory, understanding the abstract computational devices known as automata, which serve as models for digital computers. Through this study, we have gained insights into deterministic and nondeterministic finite automata, as well as ε-NFA, each with its own characteristics and capabilities.

Furthermore, we have implemented a Grammar class to represent context-free grammars and a FiniteAutomaton class to represent finite automata. These implementations have allowed us to bridge the gap between theoretical concepts and practical applications, enabling us to generate valid strings from grammar rules and determine language acceptance through state transitions.

By completing the objectives outlined in this project, we have laid the foundation for further exploration and experimentation in formal language theory and its applications. Through continued learning and experimentation, we can deepen our understanding of formal languages and their role in computer science and beyond.
